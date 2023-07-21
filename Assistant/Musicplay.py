import os
from Speak import Speak
import time
import pyautogui

def playmusic():
    try:
        Speak("playing music ")
        musicDir = "C:\\Users\\avina\\OneDrive\\Desktop\\Music"
        song = os.listdir(musicDir)
        os.startfile(os.path.join(musicDir, song[0]))
        pyautogui.press("space bar")
        time.sleep(2)

    except:
        Speak("An unknown error occurred, Sorry sir try again")
        time.sleep(2)



def playvideo():
    try:
        Speak("playing music video")
        musicDir = "C:\\Users\\avina\\OneDrive\\Desktop\\Video"
        song = os.listdir(musicDir)
        os.startfile(os.path.join(musicDir, song[0]))
        time.sleep(4)
        pyautogui.press("space")

        time.sleep(2)
    except:
        Speak("An unknown error occurred, Sorry sir try again")
        time.sleep(2)

# playvideo()
# pyautogui.press("space")