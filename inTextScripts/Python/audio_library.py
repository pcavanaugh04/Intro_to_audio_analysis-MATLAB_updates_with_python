# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:56:27 2024

Introduction to Audio Analysis, a MATLAB Apporach (2014)
Theodoros Giannakopoulous and Aggelos Pikrakis

Chapter 2 Script 4 Implement read_wav_file function

@author: pcavana
"""

import numpy as np
import wave
from scipy.io import wavfile
from typing import Optional
import time
import os


def read_wav_file(file_name: str,
                  block_duration: Optional[float] = 0,
                  save_dir: Optional[str] = "") -> float:
    """Demonstrate block based audio processing.

    """
    # Start Counter
    start_time = time.perf_counter()
    # Get information about the file
    with wave.open(file_name, 'rb') as wav_file:
        sample_rate = wav_file.getframerate()
        n_channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        n_frames = wav_file.getnframes()
        current_pos = 0
        section_count = 0

        if block_duration:
            block_size = block_duration * sample_rate

            while current_pos < n_frames:

                # Check if block size exceeds file end
                if current_pos + block_size > n_frames:
                    block_size = n_frames - current_pos

                # Read data block
                temp_data = wav_file.readframes(block_size)
                # Convert to numpy array
                temp_data = np.frombuffer(temp_data, dtype=np.int16)

                # # Save segment as new wav file
                # if save_dir:
                #     save_name = f"{int(block_duration/60)}min_section_{section_count}.wav"
                #     save_path = os.path.join(save_dir, save_name)
                #     with wave.open(save_path, 'wb') as wav_file_write:
                #         # Set save params
                #         wav_file_write.setnchannels(n_channels)
                #         wav_file_write.setsampwidth(sample_width)
                #         wav_file_write.setframerate(sample_rate)

                #         # Write audio data
                #         wav_file_write.writeframes(temp_data.tobytes())

                # Update current position
                current_pos = wav_file.tell()
                section_count += 1
            end_time = time.perf_counter()

        else:
            data = wav_file.readframes(n_frames)
            # Convert to numpy array
            data = np.frombuffer(data, dtype=np.int16)
            # Do some operation to data
            #
            #

            end_time = time.perf_counter()

    # Track execution time
    return end_time - start_time
    # print(f"Elapsed Time: {exec_time}")

# with wave.open(test_file, 'rb') as wav_file:
#     sample_rate = wav_file.getframerate()
#     n_channels = wav_file.getnchannels()
#     sampwidth = wav_file.getsampwidth()
#     n_frames = wav_file.getnframes()
#     data = wav_file.readframes(n_frames)

#     # Convert to numpy array
#     data = np.frombuffer(data, dtype=np.int16)

#     if n_channels == 2:
#         data = data.reshape((-1, 2))


if __name__ == "__main__":
    test_dir = r"C:\Users\pcavana\Git Repos\Intro_to_audio_analysis-MATLAB_updates_with_python\data\Example Load and Segment"
    test_file_name = "2023_11_01_09_37_46-chain-char-42_17-mic0_data.wav"
    test_file_path = os.path.join(test_dir, test_file_name)

    whole_duration = read_wav_file(test_file_path)
    one_min_segs = read_wav_file(test_file_path, block_duration=1 * 60)
    five_min_segs = read_wav_file(test_file_path, block_duration=5 * 60)
    ten_min_segs = read_wav_file(
        test_file_path, block_duration=10 * 60, save_dir=test_dir)
    print(f"Elapsed time for: \n\tWhole File: {whole_duration}")
    print(f"\t1-min Segments: {one_min_segs}")
    print(f"\t5-min Segments: {five_min_segs}")
    print(f"\t10-min Segments: {ten_min_segs}")
