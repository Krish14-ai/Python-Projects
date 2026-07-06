import speech_recognition as sr
import webbrowser as wb
import datetime as dt
import pyjokes as pj

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
         