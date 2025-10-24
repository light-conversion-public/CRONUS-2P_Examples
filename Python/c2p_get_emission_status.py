#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""c2pcontrol - CRONUS-2P remote control Python API.

Get the emission status of the a CRONUS-2P laser.

Copyright 2020-2025 Light Conversion
Contact: support@lightcon.com
"""
from lightcon.cronus2p import C2PControl
from time import sleep
from datetime import datetime

try:
    import tkinter as tk
    import queue
    import threading
    with_gui = True
except ImportError:
    print("Could not import TkInter, GUI disabled")
    with_gui = False


c2p = C2PControl(ip_address='127.0.0.1')

if not c2p.connected:
    print("Could not connect to CRONUS-2P")
    input("Press ENTER to close this window")
    raise RuntimeError("Could not connect to CRONUS-2P")

print("=== CRONUS-2P Emission State Monitor ===")
print("This program will continuously poll the CRONUS-2P emission state.")
print("\tEmission - laser pump diodes are active, but output beams are bloked by shutters and contained inside the laser enclosure.")
print("\tShutter open - one or more of the output shutters is open, beams are exiting the laser enclosure.")
print("Press Ctrl+C to stop the monitor")

if with_gui:
    gui_queue = queue.Queue()

    def shutter_state_gui():
        root = tk.Tk()
        root.title("CRONUS-2P Shutter State Monitor")

        label = tk.Label(root, text="CRONUS-2P", bg="gray", fg="white", font=("Arial", 40), width=25)
        label.pack(padx=10, pady=10)

        # Function to check for updates from the queue
        def check_queue():
            try:
                while True:
                    task = gui_queue.get_nowait()
                    if task == "change_bg_green":
                        label.config(bg="green")
                        label.config(text="Shutters closed")
                    elif task == "change_bg_red":
                        label.config(bg="red")
                        label.config(text="Shutters open")
            except queue.Empty:
                pass
            root.after(100, check_queue)

        check_queue()
        root.mainloop()

    gui_thread = threading.Thread(target=shutter_state_gui, daemon=True)
    gui_thread.start()


while True:
    try:
        emission = False
        mode = c2p.get_status().get('Mode')
        if mode in ['Run', 'Standby']:
            emission = True

        shutter_open = any(c2p.get_shutter_states())

        time_str = datetime.now().strftime('%Y.%m.%d %H:%M:%S')
        if not emission:
            print(f"{time_str}: Laser OFF")
        elif emission and not shutter_open:
            print(f"{time_str}: Laser emission ON, shutters CLOSED")
            if with_gui:
                gui_queue.put("change_bg_green")
        elif emission and shutter_open:
            print(f"{time_str}: Laser emission ON, shutters OPEN")
            if with_gui:
                gui_queue.put("change_bg_red")

        sleep(1)
    except KeyboardInterrupt:
        print("Monitoring stopped by user")
        break
    except Exception as excpt:
        print(f"Error: {excpt}")

input("Press ENTER to close this window")
