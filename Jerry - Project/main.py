import speech_recognition as sr
import webbrowser 
import pyttsx3 # For Personal use
import musicLibrary
import requests
from gtts import gTTS  # For Professional use
from openai import OpenAI
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id) 
engine.setProperty('voice', voices[0].id)
newsapi = "ENTER YOUR OWN API KEY"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
# def speak(text):
#     tts = gTTS(text)
#     tts.save('temp.mp3')
    
#     # Initialize Pygame mixer
#     pygame.mixer.init()
    
#     # Load the MP3 file
#     pygame.mixer.music.load('temp.mp3')
    
#     # Play file
#     pygame.mixer.music.play()
    
#     # keep the program running until the music stops
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)
        
#     pygame.mixer.music.unload()
#     os.remove('temp.mp3')
        
    
def aiProcess(command):
    client = OpenAI(api_key="ENTER YOUR OWN API KEY",) 
 
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jerry skilled in general tasks like Alexa and Google Cloud. Give short responses."},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content
    
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")     
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")     
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")     
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")     
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")  
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        speak("Okay!...Here are the top headlines from India")
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles',[])
            
            # Print the  headlines
            for article in articles:
                speak(article['title'])
    else:
        #Let OpenAI handle the request
        output = aiProcess(c.lower())
        speak(output)
        
if __name__ == "__main__" :
    speak("Initializing Jerry...")
    
    while True:

        # Listen for the wake word "Jerry"    
        r = sr.Recognizer()
        
        # Recognize speech using Google
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            # print(word)
            
            if "jerry" in word.lower():
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jerry Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                     
                    processCommand(command)
        except Exception as e:
            print("Error;{0}".format(e))
        