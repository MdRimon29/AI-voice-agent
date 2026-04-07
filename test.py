# import sounddevice as sd
# print(sd.default.device)       # shows (input, output) default
# print(sd.query_devices())      # lists all devices
# import sounddevice as sd
# print(sd.query_devices())


import sounddevice as sd
import numpy as np

duration = 3  # seconds
mic_index = 1  # your default mic
print("Recording...")
audio = sd.rec(int(duration * 44100), samplerate=44100, channels=1, device=mic_index)
sd.wait()
print("Captured max/min:", np.max(audio), np.min(audio))

