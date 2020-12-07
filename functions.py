import speech_recognition as sr #speech to text
from gtts import gTTS #text to speech
import wikipedia #for wikipedia data
from ecapture import ecapture as ec #clicking pictures from the camera
import datetime #date and time
import os #system and platform oriented commands
from time import ctime #for providing time
import time #for taking pauses
import webbrowser #extracting data from the web
import subprocess #commands like logoff shutdown
import json #storing and retrieving data
import requests #handles all the http requessts



def speak(text):
    """
    Speaks the text parameter out loud
    """
    print(text)
    tts = gTTS(text=text, lang='en-in')
    tts.save("speech.mp3")
    os.system("mpg321 speech.mp3")



def listen():
    """
    listens to what the user is saying
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) #listen for 1 second to calibrate the energy threshold for ambient noise levels
        print("\nSay...")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio) #actual code should be like data = r.recognize_google(ausio, GOOGLE_API_KEY)
        print("Simran: " + data)
    except sr.UnknownValueError:
        speak("Google Speech Recognition did not understand audio")
        return ""
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
        return ""
    except e:
        print(e)
        return ""
    return data



def greet():
    """
    Greets the user with respect to time
    """
    speak("This is your personal assistant, Priya")
    hour=datetime.datetime.now().hour
    if hour >= 0 and hour < 4:
        speak("Hello Simran, I hope you know it is pretty late to be on your device. How may I help you?")
    elif hour >= 4 and hour < 10:
        speak("Hello Simran, Good Morning. How may I help you?")
    elif hour >= 10 and hour < 16:
        speak("Hello Simran, Good Afternoon. How may I help you?")
    elif hour >= 16 and hour < 22:
        speak("Hello Simran, Good Evening. How may I help you?")
    else:
        speak("Hello Simran. How may I help you?")


def assistant(statement):
    """
    here is where the assistant answers or responds to what the user has said
    """
    questions = 0

    if statement == "":
        listening = True
        print("\nSay...")
        return listening

    if "movie" in statement or "song" in statement:
        pass

    if "bye" in statement or "stop" in statement:
        listening = False
        speak("Bye Simran, It was nice talking to you")
        return listening

    if questions == 0:
        listening = True
        speak("I am sorry, I cannot answer that")

    return listening
