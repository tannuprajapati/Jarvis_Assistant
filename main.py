import speech_recognition as sr
import pyttsx3
import webbrowser
import openai 
import datetime
import pywhatkit as kit 
from index import *


def say(text):
    text = str(text)
    engine = pyttsx3.init('sapi5') #microsoft default voice
    voices = engine.getProperty('voices') #change the voice 
    engine.setProperty('voice' , voices[1].id) #take the 2nd voice , and default voice is devid voice
    engine.setProperty('rate', 174) #slow down the speaking rate , 174 is default speed, that's why they speak normally
    #print(voices)
    engine.say(text)
    engine.runAndWait()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing......")
            query = r.recognize_google(audio,language = "en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occured. really sorry"
#playing on tbe a particular song
def play_song_on_youtube(song_name):
    try:
        # Play the song on YouTube
        kit.playonyt(song_name)
        print(f"Playing {song_name} on YouTube...")
    except Exception as e:
        print(f"An error occurred: {e}")
        


if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("HEllO I am Jarvis AI")
    while True:
        print("Listening.........")
        query = takeCommand()
    
        if "Jarvis".lower() in query.lower():
            create(query)
        if "Playing".lower() in query.lower():
            say(query)
            play_song_on_youtube(query)
        sites= [["youtube", "https://www.youtube.com"],["wikipedia", "https://www.wikipedia.com"] ,["canva", "https://www.canva.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"opening {site[0]} sir...")
                webbrowser.open(site[1])
         
                
            elif "time" in query:
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"ma'am the time is {strfTime}")
       # say(query)