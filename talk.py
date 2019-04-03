import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import requests
import wikipedia
import smtplib

def speak(audio_string):
    print(audio_string)
    tts = gTTS(text=audio_string, lang='en')



def sesKaydet():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)


    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print(" Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Haci Speech Recognition service; {0}".format(e))

    return data

def assistant(data):
    if "how are you" in data:
        speak("I am fine")

    if "what time is it" in data:
        speak(ctime())

    if "tell me location" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on , I will show you where " + location + " is.")
        os.system("chrome-browser https://www.google.tr/maps/place/" + location + "/&amp;")


    if "tell me EURO DOLAR  currency":
            #url = "http://data.fixer.io/api/latest?access_key=95cf25c181c820a7f7dad306af9ea4f7&"
            response = requests.get("http://data.fixer.io/api/latest?access_key=95cf25c181c820a7f7dad306af9ea4f7&")
            json_data = response.json()
            print(json_data["rates"])

    if "what is " in data or  "where is" in data:
            data = data.split(" ")
            question= data[2:]
            question = wikipedia.page(data)
            var = question.content
            print(question.content)
    



time.sleep(2)
speak("Hi Boss, what can I do for you?")
while 1:
    data = sesKaydet()
    assistant(data)
