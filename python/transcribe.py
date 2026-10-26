"""Transcribe an audio file with Whisper through /v1/audio/transcriptions.

    export CLOUDGPU_API_KEY=sk-...
    python transcribe.py recording.mp3
"""
import os
import sys

from openai import OpenAI

client = OpenAI(base_url="https://cloudgpu.app/v1", api_key=os.environ["CLOUDGPU_API_KEY"])

path = sys.argv[1]
with open(path, "rb") as audio:
    # Transcription models: whisper-v3-turbo and whisper-v3. whisper-v3 is the more accurate of the two.
    text = client.audio.transcriptions.create(model="whisper-v3-turbo", file=audio)
print(text.text)
