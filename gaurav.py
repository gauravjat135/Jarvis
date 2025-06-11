import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Use text-to-speech to speak the provided text."""
    engine.say(text)
    engine.runAndWait()



def process_command(command):
    """Process recognized commands."""
    command = command.lower()

    if "search" in command:
        search_query = command.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
        speak(f"Searching for {search_query}")

    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "open" in command:
        website = command.replace("open", "").strip()
        webbrowser.open(f"https://{website}.com")
        speak(f"Opening {website}")

    elif "hello" in command:
        speak("Hello! How can I assist you today?")

    elif "bye" in command:
        speak("Goodbye!")
        exit()  # Exit the program

if __name__ == "__main__":
    speak("Initializing jarvis....")
    while True:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
            print("Listening...")
            try:
                # Listen for audio with a timeout to avoid hanging
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio)  # Use Google Web Speech API
                print(f"Command recognized: {command}")
                
                # Check if the wake word "jarvis" is in the command 
                if "jarvis" in command.lower():
                    # Remove the wake word and process the rest of the command
                    command = command.lower().replace("jarvis", "").strip()
                    process_command(command)
                else:
                    print("Wake word 'jarvis' not detected.")
            
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Google Speech Recognition error; {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")





