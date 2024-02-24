import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

# Initialize the speech recognition engine
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for voice commands
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            print(f"User said: {query}\n")
        except Exception as e:
            print("Sorry, I didn't catch that. Please try again.")
            return None

        return query.lower()

# Function to execute voice commands
def execute_command(command):
    if 'wikipedia' in command:
        speak('Searching Wikipedia...')
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in command:
        webbrowser.open("https://www.youtube.com")
    elif 'open google' in command:
        webbrowser.open("https://www.google.com")
    elif 'play music' in command:
        music_dir = 'C:\\Music'  # Replace with your music directory
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif 'exit' in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I don't know how to do that.")

# Main program loop
while True:
    command = listen()
    if command:
        execute_command(command)