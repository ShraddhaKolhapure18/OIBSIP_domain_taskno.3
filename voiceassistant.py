import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit

# Initialize recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speech rate

def talk(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(f"You said: {command}")
            return command
    except sr.UnknownValueError:
        talk("Sorry, I didn't catch that.")
        return ""
    except Exception as e:
        print(f"Error: {e}")
        return ""

def run_assistant():
    talk("How can I help you?")
    while True:
        command = take_command()

        if 'hello' in command:
            talk("Hello! How can I assist you today?")
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"The current time is {time}")
        elif 'date' in command:
            date = datetime.datetime.now().strftime('%B %d, %Y')
            talk(f"Today's date is {date}")
        elif 'search' in command:
            query = command.replace('search', '')
            talk(f"Searching for {query}")
            pywhatkit.search(query)
        elif 'exit' in command or 'bye' in command:
            talk("Goodbye! Have a great day.")
            break
        elif command:
            talk("I didn't understand that. Can you repeat?")

if __name__ == "__main__":
    run_assistant()
