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

def listen():
    """
    listens to what the user is saying
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) #listen for 1 second to calibrate the energy threshold for ambient noise levels
        print("\nSay...")
        speak("Say")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio) #actual code should be like data = r.recognize_google(ausio, GOOGLE_API_KEY)
        print("Simran: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition did not understand audio")
        speak("Google Speech Recognition did not understand audio")
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
    except e:
        print(e)
    return data



def speak(text):
    """
    Speaks the text parameter out loud
    """
    if text != "Say":
        print(text)
    tts = gTTS(text=text, lang='en')
    tts.save("speech.mp3")
    os.system("mpg321 speech.mp3")



def assistant(parameter_list):
    """
    here is where the assistant answers or responds to what the user has said
    """
    
