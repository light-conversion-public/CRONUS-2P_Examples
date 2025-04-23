#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""c2pcontrol - CRONUS-2P remote control Python API.

--- LASER HAZARD WARNING ---
This script will open one or more laser shutters. Make sure that the beam
leaving the output aperture is properly terminated and that laser safety
precautions are in place.

--- REMOTE CONTROL WARNING ---
This script controls laser devices on the local network and may result in
inadvertent remote control including opening one or more laser shutters. This
can occur if the device IP address is set incorrectly. Running the script with
a localhost IP address (127.0.0.1) should be safe.

This example shows how to open and close the shutters on a CRONUS-2P laser
system. The program will ask the user to press ENTER to open all three shutters
one by one, and then to close them all at once.

Copyright 2020-2023 Light Conversion
Contact: support@lightcon.com
"""
from lightcon.cronus2p import C2PControl

c2p = C2PControl(ip_address='127.0.0.1')

if c2p.connected:
    for chan in [1, 2, 3]:
        input("Press ENTER to OPEN Ch {} shutter...".format(chan))
        c2p.open_shutter(chan)

    input("Press ENTER to CLOSE all shutters...")
    for chan in [1, 2, 3]:
        c2p.close_shutter(chan)

input("Press ENTER to close this window")
