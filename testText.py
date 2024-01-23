import openai
import requests
import config

openai.api_key=config.api_key

def get_transcription():
    audio_file = open("testSpeechDec.m4a", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript["text"]
