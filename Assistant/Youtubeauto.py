import pyautogui
from pyautogui import press
from Listening import Listening
from Speak import Speak
import pywhatkit


def SearchYou(str=""):
    try:
        str = str.replace("search ", "")
        str = str.replace("search ", "")
        if "on youtube" in str:
            str = str.replace("on youtube ", "")
        if "in yputube" in str:
            str = str.replace("on youtube ", "")
        pywhatkit.playonyt(str)
        Speak(f"I am searching {str} in youtube")
        # Speak("Do you want youtube automation mode ")
        # i = 1
        # while i <= 2:
        #     i = i+1
        #     sentence = Listening()
        #     if "no" in sentence:
        #         return
        #     if "yes" in sentence:
        #         YouTubeAuto()
    except:
        Speak("An unknown error occurred, Sorry sir try again")

