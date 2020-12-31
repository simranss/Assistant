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
import wolframalpha


app_id = 'AKYPAP-T3RA5J5H3Y'
client = wolframalpha.Client(app_id)

#to add more items in the dictionary add the below text at the end of the dictionary
#, "": ""
websites = {"gmail": "gmail.com", "youtube": "youtube.com", "google": "google.com", "stack overflow": "stackoverflow.com", "github": "github.com", "udacity": "udacity.com", "udemy": "udemy.com", "firebase": "console.firebase.google.com", "edx": "courses.edx.org/dashboard", "spotify": "open.spotify.com", "a new tab": "chrome://newtab", "new tab": "chrome://newtab", "teams": "http://teams.microsoft.com/", "microsoft teams": "http://teams.microsoft.com/", "whatsapp": "https://web.whatsapp.com/"}
apps = {"android studio": "android-studio", "visual studio code": "code", "vs code": "code", "visual studio": "code", "virtual box": "virtualbox", "slack": "slack-desktop", "files": "nautilus", "software center": "snap-store", "app store": "snap-store", "snap store": "snap-store", "calculator": "gnome-calculator", "characters": "gnome-characters"}


def listenForWakeWord():
    """
    constantly listens for the wake word "priya" and activates if the word found
    """

    wake_word = "priya"

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) #listen for 1 second to calibrate the energy threshold for ambient noise levels
        audio = r.listen(source)
    try:
        data = r.recognize_google(audio) #actual code should be like data = r.recognize_google(ausio, GOOGLE_API_KEY)
        if wake_word in data.lower():
            return True
    except sr.UnknownValueError:
        return False
    except sr.RequestError as e:
        return False
    except:
        return False


def speak(text, lang):
    """
    Speaks the text parameter out loud
    """
    print(text)
    tts = gTTS(text=text, lang=lang)
    tts.save("speech.mp3")
    os.system("mplayer speech.mp3")


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
    except:
        print("Error")
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


def getDate():
    """
    returns the current date to the user
    """
    dayNum = int(datetime.datetime.now().strftime("%d")) 
    lastDigit = dayNum % 10
    if lastDigit > 3 and lastDigit <= 9:
        romanLetter = "th"
    elif lastDigit > 0 and lastDigit <= 3:
        romanLetter = {1: "st", 2: "nd", 3: "rd"}.get(lastDigit)
    day = datetime.datetime.now().strftime("%A")
    month = datetime.datetime.now().strftime("%B")
    return ("Today is " + str(day) + ", " + str(dayNum) + romanLetter + " " + str(month))


def getTime():
    time = datetime.datetime.now().strftime("%I:%M %p.")
    return ("It is " + time)


def inApp(app):
    """
    Tells if what the user wants to open is an app or a website.
    """
    
    if app in apps:
        return True
    elif app in websites:
        return False
    else:
        return None


def assistant(questions):
    """
    here is where the assistant answers or responds to what the user has said
    """
    answerCount = 0
    
    print(questions)

    for question in questions:
        if question == "": #if question is null
            listening = True
            answerCount = answerCount + 1
            break
        
        if question.startswith("say ") or question.startswith("se "): #repeat something
            listening = True
            answerCount = answerCount + 1
            lang = "en-in"
            if question.startswith("say that "):
                newQuestion = question[9:]
                lang = "en-in"
            elif question.startswith("say "):
                newQuestion = question[4:]
                lang = "en-in"
            elif question.startswith("se "):
                newQuestion = question[3:]
                lang = "en-in"
            speak(newQuestion, "en-in")
        else:
            if " time" in question or question.startswith("time"): #ask for time
                listening = True
                time = getTime()
                speak(time, "en-in")
                answerCount = answerCount + 1

            if " day" in question or question.startswith("day") or question.startswith("de"): #ask for the day of the week
                listening = True
                answerCount = answerCount + 1
                day = getDate()
                speak(day, "en-in")

            if "open " in question: #open a software or a website
                listening = True
                answerCount = answerCount + 1
                newQuestion = question.replace("open ", "", 1)
                if inApp(newQuestion) == False:
                    speak("Opening " + newQuestion, "en-in")
                    webbrowser.open_new_tab(websites.get(newQuestion))
                elif inApp(newQuestion):
                    speak("Opening " + newQuestion, "en-in")
                    os.system(apps.get(newQuestion))
                else:
                    speak("I do not know how to open " + newQuestion, "en-in")

            if "movie" in question or "song" in question or "anime" in question or "who is " in question: #search on wikipedia
                listening = True
                answerCount = answerCount + 1
                print("Searching on wikipedia...")
                if "anime" in question:
                    newQuestion = question
                elif " song" in question:
                    newQuestion = question
                    if "movie" in question:
                        newQuestion = newQuestion.replace("movie", "", 1)
                elif "movie" in question:
                    newQuestion = question
                elif "who is " in question:
                    newQuestion = question.replace("who is ", "", 1)
                try:
                    print("Searching for " + newQuestion)
                    results = wikipedia.summary(newQuestion, auto_suggest=True, sentences=3)
                    speak(("According to Wikipedia, " + results), "en-in")
                except:
                    speak("I am sorry, data not found about " + newQuestion)

            if "bye" in question or "stop" in question or "exit" in question: #stop listening for commands
                listening = False
                answerCount = answerCount + 1
                speak("Bye Simran, It was nice talking to you", "en-in")
                break

    if answerCount == 0:
        listening = True
        speak("I am sorry, I cannot answer that", "en-in")

    return listening
