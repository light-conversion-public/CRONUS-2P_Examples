#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""c2pcontrol - a Python library for controlling CRONUS-2P.

This example shows how to determine the GDD tuning range as a function of
wavelength for both channels.

Copyright 2020-2023 Light Conversion
Contact: support@lightcon.com
"""
import numpy as np
import matplotlib.pyplot as plt

from lightcon.cronus2p import C2PControl

c2p = C2PControl(ip_address='127.0.0.1')
num_wavl_pts = 20

if c2p.connected:
    for ch in [1, 2]:
        wavl_rng = c2p.get_wavelength_range(ch)
        wavl_arr = np.linspace(wavl_rng[0], wavl_rng[1], num_wavl_pts)

        gdd_rng_arr = []
        for wavl in wavl_arr:
            gdd_rng_arr.append(c2p.get_gdd_range(ch, wavl))

        gdd_rng_arr = np.array(gdd_rng_arr)

        plt.figure()
        plt.fill_between(wavl_arr, gdd_rng_arr[:, 0], gdd_rng_arr[:, 1])
        plt.grid('on')
        plt.xlim(wavl_rng)
        plt.xlabel('Wavelength, nm')
        plt.ylabel('GDD, fs²')
        plt.title("CRONUS-2P GDD Tuning Range Ch {:d}".format(ch))
        plt.tight_layout()

plt.show()
