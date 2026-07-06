import speech_recognition as sr
import webbrowser as wb
import datetime as dt
import pyjokes as pj
import pyttsx3
import os

##-------------------------------------
## initializing voice engine 
engine = pyttsx3.init()

## Setting Voice, 0 = female, 1 = male
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)

## Setting rate of Speech
rate = engine.getProperty('rate')
engine.setProperty('rate',150)

##------------------------------------


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

    ## to speak
    engine.say(text)
    engine.runAndWait()



if __name__ == '__main__':
    name = 'hello! my name is jarvis'
    txt_to_speech(name)
    
    greeting = "how may i help you today"
    print(greeting)

    txt_to_speech(greeting)
    dt.sleep(2)
    command = ''

    while True:
        command = sptext()

        if command is None:
            continue

        command = command.lower()

        if "good bye" in command:
            txt_to_speech("Goodbye!")
            break

        elif "time" in command:
            current_time = dt.datetime.now().strftime("%I:%M %p")
            txt_to_speech(f"The time is {current_time}")

        elif "date" in command:
            current_date = dt.datetime.now().strftime("%d %B %Y")
            txt_to_speech(f"Today's date is {current_date}")

        elif "tell me a joke" in command:
            joke = pj.get_joke(language='en')
            txt_to_speech(joke)
        elif "youtube" in command:
            wb.open('https://www.youtube.com')
        
        else:
            txt_to_speech(command)