import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import requests.exceptions
import webbrowser
import os

print("Hello world Programmer!")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices)
engine.setProperty("voice", voices[0].id)
print(voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis How would you like to start the day?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-IN")
        print("User Said:", query)
    except Exception as e:
        # print(e)
        print("Please say that again!")
        return "None"
    return query

def handleNameOfMic():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"{index}) {name}")

if __name__ == "__main__":
    wishMe()

    def get_wikipedia_summary(query, sentences=2):
        max_retries = 3
        retry_count = 0

        while retry_count < max_retries:
            try:
                return wikipedia.summary(query, sentences=sentences)
            except requests.exceptions.ConnectTimeout as e:
                print(f"Connection timeout. Retrying... ({retry_count + 1}/{max_retries})")
                retry_count += 1

        print("Max retries exceeded. Unable to fetch Wikipedia data.")
        return None

    if 1:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = get_wikipedia_summary(query)
            speak("According to Wikipedia")
            if results:
                print(results)
                speak(results)
            else:
                speak("NO Results found!")

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "play music" in query:
            music_dir = "D:\\MyPrograms\\You Tube"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the current time is {strTime}")
