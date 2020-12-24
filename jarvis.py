import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good After Noon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please Tell me How may I help You.")

def takeCommand():
    #It takes microphone input and returns string output!

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        #r.record(source, duration = 10)
        #r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en_IN")
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"

    return query

def takeC():
    #It takes microphone input and returns string output!

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening Email Sir...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing Email Sir...")
        query = r.recognize_google(audio, language="en_IN")
        print(f"Email: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"

    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ahsanmuz@iul.ac.in','9935683925')
    server.sendmail('ahsanmuz@iul.ac.in',to,content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening Youtube Sir")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google Sir")
            webbrowser.open("google.com")

        elif 'open chrome' in query:
            speak("Opening Google Sir")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Opening Stackoverflow Sir")
            webbrowser.open("stackoverflow.com")

        elif 'open stackover flow' in query:
            speak("Opening Stackoverflow Sir")
            webbrowser.open("stackoverflow.com")

        elif 'open stack overflow' in query:
            speak("Opening Stackoverflow Sir")
            webbrowser.open("stackoverflow.com")

        elif 'open stack over flow' in query:
            speak("Opening Stackoverflow Sir")
            webbrowser.open("stackoverflow.com")

        elif 'open hacker rank' in query:
            speak("Opening Hackerrank Sir")
            webbrowser.open("hackerrank.com")

        elif 'open hackerrank' in query:
            speak("Opening Hackerrank Sir")
            webbrowser.open("hackerrank.com")

        elif 'play music' in query:
            speak("Playing Music Sir")
            music_dir='S:\\New Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[5]))

        elif 'the time' in query:
            strTime =datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir , the time is {strTime}")
            speak(f"Sir , the time is {strTime}")

        elif 'open code' in query:
            speak("Opening Visual Studio Code")
            codePath = "C:\\Users\\Ahsan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'quit' in query:
            speak("Shutting down Sir!")
            exit(0)
        
        elif 'email to muzammil' in query:
            try:
                speak("What should I say?")
                content = takeC()
                to = "muzammilahsan8@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am unable to send email!")

        else:
            speak("Sorry Sir ! I didn't get you.")
        
        


