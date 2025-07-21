import speech_recognition as sr
import pyttsx3
import wikipedia
from duckduckgo_search import ddg
import keyboard
import time

# Initialize TTS
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print("You said:", query)
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Network issue.")
        return ""

def web_search(query):
    try:
        results = ddg(query, max_results=1)
        if results:
            return results[0]['body'] or results[0]['href']
        else:
            return ""
    except Exception as e:
        return ""

def search_wikipedia(query):
    try:
        return wikipedia.summary(query, sentences=2)
    except:
        return ""

def type_text(text):
    keyboard.write(text)

# Main loop
speak("Hello! Internet search assistant ready.")
while True:
    command = listen()
    if "exit" in command or "stop" in command:
        speak("Goodbye!")
        break
    elif "type" in command:
        speak("What should I type?")
        to_type = listen()
        type_text(to_type)
        speak("Typed successfully.")
    elif command:
        result = web_search(command)
        if result:
            speak(result)
        else:
            wiki_result = search_wikipedia(command)
            if wiki_result:
                speak(wiki_result)
            else:
                speak("Sorry, I could not find an answer.")