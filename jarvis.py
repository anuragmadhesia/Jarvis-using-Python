import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install SpeechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #query=input("command : ")
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'hi jarvis' in query:
            speak('hello sir')
            speak('how may i help you')

        elif 'go online' in query:
            speak('ok sir')
            speak('starting all system applications')
            speak('installing all drivers')
            speak('every driver is installed')
            speak('all systems have been started')
            speak('now i am online sir')

        elif 'go offline' in query:
            speak('ok sir')
            speak('closing all systems')
            speak('disconnecting to servers')
            speak('going offline')
            quit()

        elif 'open youtube' in query:
            speak('ok sir opening youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('ok sir opening google')
            webbrowser.open("google.com")

        elif 'open instagram' in query:
            speak('ok sir opening instagram')
            webbrowser.open("instagram.com")

        elif 'open facebook' in query:
            speak('ok sir opening facebook')
            webbrowser.open("facebook.com")

        elif 'open twitter' in query:
            speak('ok sir opening twitter')
            webbrowser.open("twitter.com")

        elif 'open stackoverflow' in query:
            speak('ok sir opening stackoverflow')
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            speak('ok sir opening music')
            try:
                music_dir = 'E:\\Music\\My Best'
                songs = os.listdir(music_dir)
                # print(songs)
                speak('ok sir playing music '+songs[4])
                os.startfile(os.path.join(music_dir, songs[4]))
            except:
                speak('Some sir unable to play music')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open chess' in query:
            speak('ok sir opening chess for you')
            try:
                codePath = "C:\\Program Files\\Microsoft Games\\Chess\\chess.exe"
                os.startfile(codePath)
            except:
                speak('Chess loading failed')