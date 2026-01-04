"""
import sounddevice as sd
import numpy as np

SAMPLE_RATE = 16000

print("🎤 Speak now for 5 seconds...")

audio = sd.rec(
    int(5 * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=1,
    dtype="int16"
)

sd.wait()

volume = np.abs(audio).mean()

print("Average volume:", volume)

if volume < 50:
    print("❌ Mic NOT working or extremely quiet")
else:
    print("✅ Mic is working")
"""

import sounddevice as sd
print(sd.query_devices())
