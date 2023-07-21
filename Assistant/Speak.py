from Name_ import name_
import pyttsx3


def Speak(Text):
    try:
        with open("Database\\output.txt", 'a') as a:
            a.write(f"{name_()} : {Text}.\n")
        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 170)
        engine.say(Text)
        engine.runAndWait()
    except:
        print(1)
