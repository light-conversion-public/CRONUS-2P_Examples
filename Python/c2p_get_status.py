#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""c2pcontrol - CRONUS-2P remote control Python API.

This example shows how to get the status of a CRONUS-2P laser.

Copyright 2020-2023 Light Conversion
Contact: support@lightcon.com
"""
from lightcon.cronus2p import C2PControl
import pprint

c2p = C2PControl(ip_address='127.0.0.1')

if c2p.connected:
    print("\nCRONUS-2P Status:")
    pprint.pprint(c2p.get_status())

input("Press ENTER to close this window")
