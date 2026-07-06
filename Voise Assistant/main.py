import speech_recognition as sr
import webbrowser as wb
import datetime as dt
import pyjokes as pj
import pyttsx3 

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
           print("Recognizing...")
           data = recognizer.recognize_google(audio)
           return data
        except sr.UnknownValueError :
            print("Can't Understand")
            return None


def txt_to_speech(text):
    engine = pyttsx3.init()
    ## Setting Voice, 0 = female, 1 = male
    voice = engine.getProperty('voices')
    engine.setProperty('voice',voice[0].id)

    rate = engine.getProperty('rate')
    engine.setProperty('rate',100)

    engine.say(X)



data = sptext()
print(data)