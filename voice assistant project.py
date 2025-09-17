import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import pyjokes
import pyaudio
import pipwin

# Safe Speak Function (engine re-initialized every time)
def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # 0 = Male, 1 = Female
    engine.setProperty('rate', 150)
    engine.say(str(text))
    engine.runAndWait()

# Take command from microphone
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception:
        print("Say that again please...")
        return "none"
    return query.lower()

# Greet user
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Vaishnavi, I am your assistant. How can I help you?")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Vaishnavi, I am your assistant. How can I help you?")
    else:
        speak("Good Evening Vaishnavi, I am your assistant. How can I help you?")
    speak("I am your assistant. How can I help you?")

# Main Program
if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command()

        # Time
        if 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("The time is " + strTime)

        # Date
        elif 'date' in query:
            strDate = datetime.datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + strDate)

        # Open YouTube
        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        # Open Google
        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        # Jokes
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        # Exit
        elif 'exit' in query or 'quit' in query:
            speak("Goodbye Vaishnavi, have a great day!")
            break
