import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Voice engine setup
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
    except Exception:
        speak("Sorry, say that again")
        return "None"
    return query.lower()

# Main
if _name_ == "_main_":
    speak("Hello, I am Jarvis")
    while True:
        command = take_command()

        if "time" in command:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")

        elif "youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "stop" in command or "exit" in command:
            speak("Goodbye")
            break
