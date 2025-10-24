#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""c2pcontrol - CRONUS-2P remote control Python API.

Control a CRONUS-2P shutter remotely.

Copyright 2020-2025 Light Conversion
Contact: support@lightcon.com
"""
from lightcon.cronus2p import C2PControl
from time import sleep
from datetime import datetime
import random

import tkinter as tk
import queue
import threading

C2P_IP = '10.1.240.11'
CHAN_ID = 2
DRY_RUN = False
GUI_SIZE = 40

if not DRY_RUN:
    c2p = C2PControl(ip_address=C2P_IP)

    if not c2p.connected:
        print("Could not connect to CRONUS-2P")
        input("Press ENTER to close this window")
        raise RuntimeError("Could not connect to CRONUS-2P")

print("=== CRONUS-2P Remote Shutter Control ===")
print("This program will open and close a CRONUS-2P shutter remotely over network.")

gui_queue = queue.Queue()
wavl_power_queue = queue.Queue()

def shutter_control_gui():
    root = tk.Tk()
    root.title("CRONUS-2P Shutter Control")

    if DRY_RUN:
        sim_label = tk.Label(root, text=f"SIMULATION", bg="#191e5a", fg="white", font=("Arial", int(GUI_SIZE/2)), width=int(GUI_SIZE/2.5))
        sim_label.pack(padx=10, pady=10)
        print("Simulated GUI interaction, no connection to a real laser device")
        
    status_label = tk.Label(root, text=f"CRONUS-2P Ch {CHAN_ID}", bg="#191e5a", fg="white", font=("Arial", GUI_SIZE), width=int(GUI_SIZE/2.5))
    status_label.pack(padx=10, pady=10)
    #wavl_power_label = tk.Label(root, text="N/A nm   N/A W", bg="gray", fg="white", font=("Arial", GUI_SIZE), width=int(GUI_SIZE/2.5))
    #wavl_power_label.pack(padx=10, pady=10)
    

    shutter_button = tk.Button(root, command=lambda: on_button_click(shutter_button), text="Shutter", bg="gray", fg="white", font=("Arial", GUI_SIZE), width=int(GUI_SIZE/2.5))
    shutter_button.pack(padx=10, pady=10)

    # Function to check for updates from the queue
    def check_queue():
        try:
            while True:
                task = gui_queue.get_nowait()
                if task == "shutter_is_closed":
                    shutter_button.config(bg="#5a9b28")
                    shutter_button.config(text="Shutter closed")
                elif task == "shutter_is_open":
                    shutter_button.config(bg="#f08c00")
                    shutter_button.config(text="Shutter open")
        except queue.Empty:
            pass

        #try:
        #    while True:
        #        wavl_power = wavl_power_queue.get_nowait()
        #        wavl_power_label.config(text=wavl_power)
        #except queue.Empty:
         #   pass

        root.after(100, check_queue)

    check_queue()
    root.mainloop()

def on_button_click(btn):
    if 'closed' in btn['text']:
        print(f"Opening shutter {CHAN_ID}")
        if not DRY_RUN:
            c2p.open_shutter(CHAN_ID)
        else:
            gui_queue.put("shutter_is_closed")
    elif 'open' in btn['text']:
        print(f"Closing shutter {CHAN_ID}")
        if not DRY_RUN:
            c2p.close_shutter(CHAN_ID)
        else:
            gui_queue.put("shutter_is_open")
    
gui_thread = threading.Thread(target=shutter_control_gui, daemon=True)
gui_thread.start()

if DRY_RUN:
    gui_queue.put("shutter_is_closed")

while True:
    try:
        emission = False
        if not DRY_RUN:
            mode = c2p.get_status().get('Mode')
            #wavl = c2p.get_wavelength(CHAN_ID)
            #power = c2p._get(f"Ch{CHAN_ID}/Power")
            #wavl_power_queue.put(f"{wavl:.0f} nm   {power*1E-3:2f} W")
        else:
            mode = 'Run'
            wavl_power_queue.put(f"{920 + random.randint(-5, 5)} nm   {1.0 + (random.random()-0.5)/10:.2f} W")

        if mode in ['Run', 'Standby']:
                emission = True

        if not DRY_RUN:
            # TODO: This does not work
            # shutter_open = c2p.get_shutter_states()
            shutter_open = c2p._get('Ch1/Status')['IsShutterOpen']
            time_str = datetime.now().strftime('%Y.%m.%d %H:%M:%S')
            if not emission:
                print(f"{time_str}: Laser OFF")
            elif emission and not shutter_open:
                print(f"{time_str}: Laser emission ON, shutter {CHAN_ID} CLOSED")
                gui_queue.put("shutter_is_closed")
            elif emission and shutter_open:
                print(f"{time_str}: Laser emission ON, shutter {CHAN_ID} OPEN")
                gui_queue.put("shutter_is_open")

        sleep(1)
    except KeyboardInterrupt:
        print("Monitoring stopped by user")
        break
    except Exception as excpt:
        print(f"Error: {excpt}")

input("Press ENTER to close this window")
