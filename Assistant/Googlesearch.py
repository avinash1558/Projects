
import pywhatkit
from Speak import Speak
import wikipedia
from time import sleep
import webbrowser
def info(str):
    try:
        data = wikipedia.summary(str, sentences=1)
        Speak(data)
    except:
        print()
# info("rohit sharma")



    

def searchonWIKI(str=""):
    str = str.replace("search", "")
    if "on wikipedia" in str:
        str = str.replace("on wikipedia", "")
    if "in wikipedia" in str:
        str = str.replace("in wikipedia", "")
    try:
        Speak(f"I am searching {str} on Wikipeadia")
        pywhatkit.search(str)
        webbrowser.open(f"https://en.wikipedia.org/wiki/{str}")
        sleep(2)
        info(str)
    except:
        Speak("An unknown error occurred, Sorry sir try again ")
    
   


def searchongoogle(str=""):
    str = str.replace("search", "")
    if "on google" in str:
        str = str.replace("on google", "")
    if "in google" in str:
        str = str.replace("in google", "")

    try:
        Speak(f"I am searching {str} on google")
        pywhatkit.search(str)
        sleep(2)
        info(str)

    except:
        Speak("An unknown error occurred, Sorry sir try again ")
# searchongoogle("search app on google")