import pyautogui as p
import time
import pyperclip
from Speak import Speak


def textreader():
    try:
        Speak("Sir i am reading selected text")
        p.keyDown("ctrl")
        p.press("c")
        p.keyUp("ctrl")
        s2 = pyperclip. paste()
        if len(s2) > 1:
            Speak(s2)

        else:
            Speak("Nothing is selected")
        time.sleep(2)
    except:
        Speak("An unknown error occurred, Sorry sir try again ")
        time.sleep(2)
