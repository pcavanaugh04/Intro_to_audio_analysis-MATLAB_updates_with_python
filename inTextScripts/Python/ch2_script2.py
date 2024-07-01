# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 11:20:19 2024

@author: pcavana
"""
import numpy as np
import math as m
import matplotlib.pyplot as plt
import sounddevice as sd

# Define Sampling Rates and Times
Fs = 16000
Ts = 1 / Fs
time = np.arange(0, 2, Ts)

# Construct Signal
xLeft = np.array([m.cos(2 * m.pi * 250 * x) for x in time])
xRight = np.array([m.cos(2 * m.pi * 450 * x) for x in time])

# Create Stereo Signal from Transposed Channels
stereo_signal = np.column_stack((xLeft, xRight))

# Plot Outputs
fig, axs = plt.subplots(2, 1)
# Samples for 0.1s window
window = int(0.1 * Fs)

axs[0].plot(time[:window], xLeft[:window])
axs[0].set_xlabel("Time [s]")
axs[0].set_ylabel("Amplitude")
axs[0].set_title("Left Channel")

axs[1].plot(time[:window], xRight[:window])
axs[1].set_xlabel("Time [s]")
axs[1].set_ylabel("Amplitude")
axs[1].set_title("Right Channel")

plt.tight_layout(rect=[0, 0, 1, 0.95])

plt.show()

# Play Sound on Sounddevice
sd.play(stereo_signal, Fs)
