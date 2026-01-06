from openai import OpenAI
import os
from gtts import gTTS
import json
import time
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play


def ask_fishy(user_input):
  client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)
  completion = client.chat.completions.create(
    extra_body={},
    model="tngtech/deepseek-r1t2-chimera:free",
    messages=[
      {
        "role": "user",
        "content": user_input + " CONTEXT: YOU ARE A FISH NAMED FISHY. FUN, MOTIVATING, ENTHUSIASTIC, SOMETIMES AGGRESSIVE. SIMPLE ENGLISH BUT FORM COMPLETE SENTENSES. SHORT MESSAGE BUT MEANINGFUL. NO EMOJI"
      }
    ]
  )
  return completion.choices[0].message.content


"""
language = "en"
text = completion.choices[0].message.content + " *blub blub*"

speech = gTTS(text=text, lang="en", tld="com.ng")
speech.save("audio.mp3")
playsound("audio.mp3")
"""