import speech_recognition as sr #speech to text
from gtts import gTTS #text to speech
import wikipedia #for wikipedia data
from ecapture import ecapture as ec #clicking pictures from the camera
import datetime #date and time
import os #system and platform oriented commands
import time #for taking pauses
import webbrowser #extracting data from the web
import subprocess #commands like logoff shutdown
import json #storing and retrieving data
import requests #handles all the http requessts
import random #to make random choices
import calendar #to get the day of the week



def wakeWord(text):
    WAKE_WORDS = ['hai priya', 'priya'] 
    text = text
     
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
  
    return False



def speak(text, lang):
    """
    Speaks the text parameter out loud
    """
    print(text)
    tts = gTTS(text=text, lang=lang)
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
        speak("Google Speech Recognition did not understand audio", "en-in")
        return ""
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
        return ""
    except e:
        print(e)
        return ""
    return data.lower()



def greet():
    """
    Greets the user with respect to time
    """
    speak("This is your personal assistant, Priya", "en-in")
    hour=datetime.datetime.now().hour
    if hour >= 0 and hour < 4:
        speak("Hello Simran, I hope you know it is pretty late to be on your device. How may I help you?", "en-in")
    elif hour >= 4 and hour < 10:
        speak("Hello Simran, Good Morning. How may I help you?", "en-in")
    elif hour >= 10 and hour < 16:
        speak("Hello Simran, Good Afternoon. How may I help you?", "en-in")
    elif hour >= 16 and hour < 22:
        speak("Hello Simran, Good Evening. How may I help you?", "en-in")
    else:
        speak("Hello Simran. How may I help you?", "en-in")


def getTime():
    now = datetime.datetime.now()
    meridiem = ''
    if now.hour >= 12:
        meridiem = 'p.m' #PM
        hour = now.hour - 12
    else:
        meridiem = 'a.m' #AM
        hour = now.hour
    # Convert minute into a proper string
    if now.minute < 10:
        minute = '0' + str(now.minute)
    else:
        minute = str(now.minute)
    return ("It is " + str(hour) + ':' + minute + ' ' + meridiem + '.')



def assistant(questions):
    """
    here is where the assistant answers or responds to what the user has said
    """
    answerCount = 0
    
    print(questions)

    for question in questions:
        if question == "":
            listening = True
            answerCount = answerCount + 1
            break
        
        if question.startswith("say ") or question.startswith("se "):
            listening = True
            answerCount = answerCount + 1
            lang = "en-in"
            if question.startswith("say "):
                question = question[4:]
                lang = "en-in"
            if question.startswith("say that "):
                question = question[9:]
                lang = "en-in"
            if question.startswith("se "):
                question = question[3:]
                lang = "en-in"
            speak(question, "en-in")

        if "time" in question:
            listening = True
            time = getTime()
            speak(time, "en-in")
            answerCount = answerCount + 1

        if "day" in question:
            listening = True
            answerCount = answerCount + 1
            pass

        if "movie" in question or "song" in question:
            listening = True
            answerCount = answerCount + 1
            pass

        if "bye" in question or "stop" in question:
            listening = False
            answerCount = answerCount + 1
            speak("Bye Simran, It was nice talking to you", "en-in")
            break

    if answerCount == 0:
        listening = True
        speak("I am sorry, I cannot answer that", "en-in")

    return listening
