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
            if "dear" in command:
                command = command.replace("dear","")        
    except:
        pass
    return command

def talk(command):  
    alexa.say(command)
    alexa.runAndWait()

def hello_dear():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%m:%p')
        print(time)
        talk(time)
    elif 'play' in command:
        print(command)
        command = command.replace('play','')
        pywhatkit.playonyt(command)
    elif 'about' in command or 'search' in command:
        print(command)
        command = command.replace('search','').replace('about','')
        pywhatkit.search(command)


if __name__ == "__main__":
    print("Hello")
    while(True):
        hello_dear()