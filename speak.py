import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang="en", tld="ie")
    filename = "audio.mp3"
    tts.save(filename)
    playsound.playsound(filename)



def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_vosk(audio_data="vosk-model-small-en-us-0.15")
            print(said)
        except Exception as e:
            print(f"Exception {e}")

speak("HELLO. HOW ARE YOU DOING?")
get_audio()