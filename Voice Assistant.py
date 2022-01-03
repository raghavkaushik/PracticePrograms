#Mini Project - Voice Assistant
#This project contains basic commands which could be called using voice commands, commands like opening a file, browsing the web, emails etc.

#The libraries used -
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

#Setting up the assistant voice
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print("The available voices in the system are:",voices)
engine.setProperty('voice',voices[1].id)


# Function to send audio to Voice Assistant
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<=17:
        speak("Good Afternoon")
    elif hour>=17 and hour<=20:
        speak("Good Evening")
    elif hour>=20 and hour<=24:
        speak("Good Night")
    speak("Hi this is your voice assistant, how may I help you")

#Taking input from the user using microphone and output as string.
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing")
        query=r.recognize_google(audio, language='en-in')
        print(f"User Command{query}\n")
    except Exception as e:
        print(e)
        speak("Kindly repeat")
        return None
    return query


if __name__=='__main__':
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query , sentences=2)
            print(results)
            speak("according to wikipedia")
            speak(results)

        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        if 'open google' in query:
            webbrowser.open("Google.com")

        if 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtime}")

        if 'close assistant' in query:
            break

























