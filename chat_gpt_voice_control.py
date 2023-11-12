import openai 
import requests
import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()

r = sr.Recognizer()

client = openai.Client(api_key='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')

engine.say("Pergunte Me Qualquer coisa.")
engine.runAndWait()

with sr.Microphone() as source:
    audio = r.listen(source)

try:
    text = r.recognize_google(audio, language='pt-BR')
    print("Você disse: {}".format(text))
except sr.UnknownValueError:
    print("Não foi possível reconhecer o áudio.")
except sr.RequestError as e:
    print("Erro ao solicitar o serviço de reconhecimento de fala; {0}".format(e))

def txt_chatgpt (text):
  openai.api_key = "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"

#   url = "https://api.openai.com/v1/completions"
  prompt= text

  response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={ "type": "json_object" },
    messages=[
      {"role": "system", "content": "You are a helpful assistant designed to output short phrases in brazilian Portuguese"},
      {"role": "user", "content": prompt}
    ]
  )

  if response.status_code != 200:
      print(f"Erro ao gerar resposta: {response.text}")
  else:
      data = response.json()
      text = data["choices"][0]["message"]
      engine.say(text)
      engine.runAndWait()

txt_chatgpt(text)
