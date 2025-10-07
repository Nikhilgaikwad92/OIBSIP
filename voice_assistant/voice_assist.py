import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # You can change this to voices[1].id for a female voice

def speak(audio):
    """Converts text to speech."""
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    """Wishes the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
speak("I am your voice assistant. How can I help you today?")

def take_command():
    """Listens for user's voice command and converts it to text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again, please...")
        return "None"
    return query.lower()

if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.PageError:
                speak("Sorry, I could not find anything on that topic.")
            except wikipedia.exceptions.DisambiguationError as e:
                speak(f"There are multiple results for {query}. Please be more specific.")
                print(e.options)

        elif 'open youtube' in query:
            speak("Opening YouTube.")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google.")
            webbrowser.open("google.com")
            
        elif 'open gmail' in query:
            speak("Opening Gmail.")
            webbrowser.open("gmail.com")
            
        elif 'open instagram' in query:
            speak("Opening instagram.")
            webbrowser.open("instagram.com")         

        elif 'open whatsapp' in query:
            speak("Opening whatsappl.")
            webbrowser.open("whatsapp.com") 
  
        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the current time is {str_time}")

        elif 'open code' in query:
            speak("Opening VS Code.")
            code_path = "C:\\Users\\YourUsername\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" # Replace with your VS Code path
            os.startfile(code_path)

        elif 'exit' in query or 'quit' in query or 'bye' in query:
            speak("Goodbye! Have a great day.")
            break