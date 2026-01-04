import sounddevice as sd
import numpy as np
import whisper
import time

# ---------------- SETTINGS ----------------
SAMPLE_RATE = 16000
SILENCE_THRESHOLD = 0.01   # audio energy
SILENCE_DURATION = 1.5    # seconds
MIC_DEVICE = 0            # MacBook Air Microphone
# ------------------------------------------

sd.default.device = MIC_DEVICE
sd.default.samplerate = SAMPLE_RATE
sd.default.channels = 1

print("🎤 Speak now (will auto-stop after silence)...")

audio_chunks = []
last_sound_time = time.time()

def callback(indata, frames, time_info, status):
    global last_sound_time

    # indata is float32 already
    volume = np.sqrt(np.mean(indata**2))

    if volume > SILENCE_THRESHOLD:
        last_sound_time = time.time()
        audio_chunks.append(indata.copy())

    # Stop if silence too long
    if time.time() - last_sound_time > SILENCE_DURATION:
        raise sd.CallbackStop()

# ---------------- RECORD ----------------
with sd.InputStream(
    dtype="float32",
    callback=callback,
    blocksize=1024
):
    while True:
        sd.sleep(100)

# ---------------- PROCESS ----------------
if not audio_chunks:
    print("❌ No audio captured")
    exit()

audio = np.concatenate(audio_chunks).flatten()

print("🧠 Transcribing...")

model = whisper.load_model("small")  # medium also fine
result = model.transcribe(
    audio,
    fp16=False,
    language="en"
)

text = result["text"].strip()

print("\n✅ Transcribed Text:")
print(text)
