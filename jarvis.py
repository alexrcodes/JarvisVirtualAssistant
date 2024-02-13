from http import server
import re
from winreg import QueryValue
from bs4 import ResultSet
from numpy import take
import pyttsx3
from pytz import HOUR
import speech_recognition as sr
import datetime
import random
import requests
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib 
import sys
import os
import pyjokes 
import pyautogui
import json

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)


#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to convert voice into text
def takecommand():  #listens for audio commands
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...") #uses googles api to recognize the audio commands
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}")

    except Exception as e:
        speak("Sir, say that again please...")
        return "none"
    return query

#to wish
def wish(): 
    hour = int(datetime.datetime.now().hour)
    #allows jarvis to tell me the current time, depending on the hour
    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening") 
    speak("i am jarvis your ai sir, please tell me how can i assist you")   

#for news updates
def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch$apiKey=17b38d0b7ff243c19a72d4805252f6b3"

    main_page = requests.get(main_url.json)
    #print(main_page)
    articles = main_page["articles"]
    #print(artices)
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        #print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: , {head[i]}")

#allows me to run all the functions
if __name__ == '__main__':
    wish()
    while True:
    #if 1:

        query = takecommand().lower()

#logic building for tasks
        if  "open google" in query:
            speak("sir, what should i search")
            cm = takecommand()
            webbrowser.open(f"https://www.google.com/search?q={cm}")

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube sir")

        elif "check email" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            speak("checking email inbox sir")
        
        elif "send email" in query:
            #server = smtplib.SMTP('smtp.gmail.com',587)
            #server.starttls()
            #server.login("alexander123thomas@gmail.com", "alexthomas14")
            #server.sendmail("alexander123thomas@gmail.com", "test@mail.google", "Mail sent from python code")
            #speak("mail sent successfully")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")
            speak("setting up new email message sir...")

        elif "play song" in query:
            cm = takecommand()
            kit.playonyt(f"{cm}")

        elif "according to wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)

#
##
###
####
#####
######
####### MANY MORE COMMMANDS TO COME
                                    #######
                                     ######
                                      #####
                                       ####
                                        ###
                                         ##
                                          #
            
# to sleep jarvis
        elif "you can sleep" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()


#to close any application
        elif "close notepad" in query:  
            speak("okay sir, closing notepad")
            os.system("taskkill /f / im notepad.exe")

        elif "close command prompt" in query:  
            speak("okay sir, closing command prompt")
            os.system("taskkill /f / im cmd.exe")


# to set an alarm 
        elif "set alarm" in query:
            n = int(datetime.datetime.now().hour)
            if n==22:
                music_dir = "C:\\music"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[3]))

# to tell a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
        elif "that was not funny" in query:
            speak("You aren't either, hahaha")
        elif "good one" in query:
            speak("thanks sir, it's an original!")

#################################################################################################
#################################################################################################
        
        elif "tell me the news" in query:
            speak("please wait sir, fetching the latest news")
            news()


# system commands 
        elif "shut down the system" in query:
            os.system("shutdown /r /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rund1132.exe powrprof.d11,SetSuspendState 0,1,0")
        
        # speak(".......do you have any other work")    
