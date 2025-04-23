#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""c2pcontrol - CRONUS-2P remote control Python API.

--- REMOTE CONTROL WARNING ---
This script controls laser devices on the local network and may result in
inadvertent remote control including opening one or more laser shutters. This
can occur if the device IP address is set incorrectly. Running the script with
a localhost IP address (127.0.0.1) should be safe.

This example shows how to set the GDD of Channel 1 of a CRONUS-2P laser system.

Copyright 2020-2023 Light Conversion
Contact: support@lightcon.com
"""
from lightcon.cronus2p import C2PControl

chan = 1
target_gdd = -5000
c2p = C2PControl(ip_address='127.0.0.1')

if c2p.connected:
    curr_gdd = c2p.get_gdd(chan)
    print("Current GDD is: {:.0f} fs2".format(curr_gdd))

    print("Setting GDD to {:.0f} fs2".format(target_gdd))
    c2p.set_gdd(chan, target_gdd)

input("Press ENTER to close this window")
