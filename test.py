import openai
import config
import requests
from testText import get_transcription

openai.api_key=config.api_key

article = get_transcription()

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "assistant", "content": "Write a summary of this text"},
        {"role": "user", "content": article}
    ]
)

summary = response["choices"][0]["message"]["content"]
file=open("test.html", "w")
file.write(f"<p>Summary: {summary} </p>")
file.write(f"<p>Originial: {article}</p>")
file.close()
