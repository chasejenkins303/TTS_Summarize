import openai
import requests

openai.api_key='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'

def get_transcription():
    audio_file = open("testSpeechDec.m4a", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript["text"]
