
from Speak import Speak
import speech_recognition as sp  # pip install speechrecognition
from googletrans import Translator  # pip install googletrans==3.1.0a0


def Listening():
    query = ""
    r = sp.Recognizer()
    with sp.Microphone() as source:
        Speak("Speak Please...")
        audio = r.listen(source, 0, 8)

    try:
        text = r.recognize_google(audio, language="en-hi")
        query = str(text)
    except:
        query = "none"
    with open("Database\\output.txt", 'a') as a:
        a.write(f"You : {query}.\n")
    return query.lower()

