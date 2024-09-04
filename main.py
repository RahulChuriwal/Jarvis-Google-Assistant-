import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import google.generativeai as genai

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = <API_KEY>  # Replace with your actual News API key

def speak(text):
    """Function to convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    import google.generativeai as genai

    API_KEY = <API_KEY>
    genai.configure(api_key=API_KEY)

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(command)
    return (response.text)

def processCommand(c):
    """Function to process commands from the user and execute appropriate actions."""
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("http://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("http://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song {song}.")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
        else:
            speak("Failed to fetch news.")
    else:
        # Use Gemini API to generate a response
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            word = recognizer.recognize_google(audio)
            
            if word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    
                    processCommand(command)
            
        except Exception as e:
            print(f"Error: {e}")
