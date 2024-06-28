# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 11:47:09 2024

Introduction to Audio Analysis, a MATLAB Apporach (2014)
Theodoros Giannakopoulous and Aggelos Pikrakis

Chapter 2 Script 3 Reading and Writing Audio Files

@author: pcavana
"""

import numpy as np
import wave
from scipy.io import wavfile

# Test file to read
test_file = r"C:\Users\pcavana\Git Repos\Intro_to_audio_analysis-MATLAB_updates_with_python\data\3WORDS.wav"

# Read audio data
# Implementation with wavfile
Fs_wavfile, data_wavfile = wavfile.read(test_file)

# Implementation with wave
"""Wave gives more flexible + accessible information abou the file through
   various methods contained in the file object"""
with wave.open(test_file, 'rb') as wav_file:
    sample_rate = wav_file.getframerate()
    n_channels = wav_file.getnchannels()
    sampwidth = wav_file.getsampwidth()
    n_frames = wav_file.getnframes()
    data = wav_file.readframes(n_frames)

    # Convert to numpy array
    data = np.frombuffer(data, dtype=np.int16)

    if n_channels == 2:
        data = data.reshape((-1, 2))

# Read audio data in segments
block_width_s = 1  # Data block width in seconds

with wave.open(test_file, 'rb') as wav_file:
    sample_rate = wav_file.getframerate()
    block_width_frames = block_width_s * sample_rate

    n_channels = wav_file.getnchannels()
    sampwidth = wav_file.getsampwidth()
    n_frames = wav_file.getnframes()

    data_block_1 = wav_file.readframes(block_width_frames)
    data_block_2 = wav_file.readframes(block_width_frames)
    data_block_3 = wav_file.readframes(block_width_frames)
    data_block_4 = wav_file.readframes(block_width_frames)

    # Convert to numpy array
    data_block_1 = np.frombuffer(data_block_1, dtype=np.int16)
    data_block_2 = np.frombuffer(data_block_2, dtype=np.int16)
    data_block_3 = np.frombuffer(data_block_3, dtype=np.int16)
    data_block_4 = np.frombuffer(data_block_4, dtype=np.int16)

    if n_channels == 2:
        data = data.reshape((-1, 2))
