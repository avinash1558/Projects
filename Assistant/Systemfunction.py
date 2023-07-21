import os
from Speak import Speak
import pyautogui as pa
from time import sleep

def hidefile():
    os.system("attrib +h /s /d")
    Speak("Sir all the files in this folder are now hidden")


def visiblefile():
    os.system("attrib -h /s /d")
    Speak("Sir all the files in this folder are now visible to every one ")


def Restart():
    Speak("Sir i am restarting the pc")
    Speak("And i am stop")
    os.system("shutdown /r /t 15")
    sleep(15)


def Shutdown():
    Speak("Sir i am shutdown the pc")
    Speak("And i am also shutdown")

    os.system("shutdown /s /t 15")
    sleep(15)
    


def Logout():
    Speak("Sir i am logout the pc")
    os.system("shutdown -l")


def VolUp():
    Speak("Sir i am increasing the volume to 10")

    for i in range(5):
        pa.press("volumeup")


def VolDown():
    Speak("Sir i am decreasing the volume to 10")
    for i in range(5):
        pa.press("volumedown")


def VolMute():
    Speak("pc on mute mode")

    pa.press("volumemute")
