import pyautogui
import webbrowser
from time import sleep
from Speak import Speak
from Listening import Listening
from chromeauto import ChromeAuto


def OpenApp(Name):
    try:
        if "open" in Name:
            Nameoftheapp = Name.replace("open ", "")
        elif "start" in Name:
            Nameoftheapp = Name.replace("start ", "")
        elif "launch" in Name:
            Nameoftheapp = Name.replace("launch", "")

        if "application" in Nameoftheapp:
            Nameoftheapp = Nameoftheapp.replace("application", "")
        if "app" in Nameoftheapp:
            Nameoftheapp = Nameoftheapp.replace("app", "")

        Speak(f"i am opening {Nameoftheapp}")
        pyautogui.press('win')
        sleep(0.2)
        pyautogui.write(Nameoftheapp)
        sleep(0.3)
        pyautogui.press('enter')
        sleep(0.2)
        if ("chrome" in Nameoftheapp):
            Speak("Do you want chrome automation mode ")
            i = 1
            while i <= 2:
                i = i+1
                sentence = Listening()
                if "no" in sentence:
                    return
                if "yes" in sentence:
                    ChromeAuto()
            Speak("i am terminating you command")
    except Exception as e:
        Speak("Sorry for inconvenient , Try again")
        sleep(2)
# OpenApp("open chrome")

def closeapp():
    pyautogui.keyDown("alt")
    pyautogui.press("f4")
    pyautogui.keyUp("alt")
    pyautogui.press("enter")
    sleep(2)


def closeall():
    Speak("some time error is  occurred so press alt key")
    i = 1
    while i <= 6:
        i = i+1
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        sleep(0.2)
        pyautogui.keyUp("alt")
        sleep(0.5)
        pyautogui.keyDown("alt")
        pyautogui.press("f4")
        sleep(0.2)
        pyautogui.keyUp("alt")
        sleep(0.2)


def OpenSite(Name):
    try:
        if "open" in Name:
            Nameofweb = Name.replace("open ", "")
        elif "launch" in Name:
            Nameofweb = Name.replace("launch ", "")
        Speak(f"i am opening {Nameofweb}")

        if ".com" in Nameofweb:
            Link = f"https://www.{Nameofweb}"

        elif ".in" in Nameofweb:
            Link = f"https://www.{Nameofweb}"

        elif ".co" in Nameofweb:
            Link = f"https://www.{Nameofweb}"

        elif ".edu" in Nameofweb:
            Link = f"https://www.{Nameofweb}"
        elif ".org" in Nameofweb:
            Link = f"https://www.{Nameofweb}"
        else:
            Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        sleep(2)
    except Exception as e:
        Speak("Sorry for inconvenient , Try again")
        sleep(2)
