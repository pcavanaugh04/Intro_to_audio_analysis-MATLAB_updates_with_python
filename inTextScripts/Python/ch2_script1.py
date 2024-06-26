"""
Created on Wed Jun 26 15:36:42 2024

@author: pcavana
"""
import numpy as np
import math as m
import matplotlib.pyplot as plt
import sounddevice as sd

# Script 1 Chapter 2
# Demonstrate generation of synthetic tones

Fs = 16000    # Sampling Frequency
Ts = 1 / Fs     # Sampling Period
Freqs = [261.63, 329.63, 392]

# Optional syntax to raise tones by an octave
# Freqs = [x*2 for x in Freqs]

plot_time = np.arange(0, 0.1, Ts)
play_time = np.arange(0, 2, Ts)

plot_Xs = []
play_Xs = plot_Xs.copy()

# Generate tones as sine function
for freq in Freqs:
    plot_Xs.append(np.array([m.cos(2 * m.pi * freq * x) for x in plot_time]))
    play_Xs.append(np.array([m.cos(2 * m.pi * freq * x) for x in play_time]))

# Sum all tones for resultant signal
plot_x = plot_Xs[0] + plot_Xs[1] + plot_Xs[2]
play_x = play_Xs[0] + play_Xs[1] + play_Xs[2]

# Normalize Values
max_plot_x = max(plot_x)
max_play_x = max(play_x)
plot_x = [x / max_plot_x for x in plot_x]
play_x = [x / max_play_x for x in play_x]

# Visualize The Signals
# Create a figure and subplots
fig, axs = plt.subplots(4, 1, figsize=(10, 10))

# First subplot
axs[0].plot(plot_time, plot_Xs[0])
axs[0].set_xlabel('Time (sec)')
axs[0].set_ylabel('Signal Amplitude')
axs[0].set_title(f"{Freqs[0]} Hz Signal")

# Second subplot
axs[1].plot(plot_time, plot_Xs[1])
axs[1].set_xlabel('Time (sec)')
axs[1].set_ylabel('Signal Amplitude')
axs[1].set_title(f"{Freqs[1]} Hz Signal")

# Third subplot
axs[2].plot(plot_time, plot_Xs[2])
axs[2].set_xlabel('Time (sec)')
axs[2].set_ylabel('Signal Amplitude')
axs[2].set_title(f"{Freqs[2]} Hz Signal")

# Fourth subplot
axs[3].plot(plot_time, plot_x)
axs[3].axis([0, plot_time[-1], -1, 1])
axs[3].set_xlabel('Time (sec)')
axs[3].set_ylabel('Signal Amplitude')
axs[3].set_title("Resulting Signal")

# Add a super title
fig.suptitle("3-toned audio signals", fontsize=16)

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Show the plot
plt.show()

# Play the signal
sd.play(play_x, Fs)
sd.wait()
