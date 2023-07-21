from Wish import welcome
from Speak import Speak
import pyautogui as p
from Shownote import speakrem
from Name_ import name_
import time


def starting():
    time.sleep(1)
    Speak(f"{welcome()} Sir")
    try:
        p.press("esc")

        with open("Database\\count.txt", "r") as r:
            read = r.read()
        read = int(read)
        write = read+1
        with open("Database\\count.txt", "w") as w:
            w.write(str(write))

        if (read <= 3):
            Speak("Wait sir let me check first reminder")
            speakrem()
    except:
        print()
    Speak(f"I'm {name_()}, I'm Ready To Assist You Sir.")
