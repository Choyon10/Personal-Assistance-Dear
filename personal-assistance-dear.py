import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit

listner = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice',voices[1].id)

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listner.listen(source)
            command = listner.recognize_google(voice).lower()
            if "alexa" in command:
                command = command.replace("alexa","")        
    except:
        pass
    return command