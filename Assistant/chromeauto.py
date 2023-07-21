import pyautogui as pa
import pyautogui
from Listening import Listening
from Speak import Speak
# from Youtubeauto import YouTubeAuto
from time import sleep
def ChromeAuto():
    try:
        Speak("Now you are in automation mode")
        while 1:
            sleep(2)
            query = Listening()

            if 'new tab' in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("t")
                pyautogui.keyUp("ctrl")

            elif 'close tab' in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("w")
                pyautogui.keyUp("ctrl")

            elif 'new window' in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("n")
                pyautogui.keyUp("ctrl")

            elif 'history' in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("h")
                pyautogui.keyUp("ctrl")

            elif 'download' in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("j")
                pyautogui.keyUp("ctrl")

            elif 'bookmark' in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("")
                pyautogui.keyUp("ctrl")
                pyautogui.press('enter')

            elif 'incognito' in query:
                pyautogui.keyDown("ctrl")
                pyautogui.keyDown("Shift")
                pyautogui.press("n")
                pyautogui.keyUp("Shift")
                pyautogui.keyUp("ctrl")

            elif 'switch tab' in query:
                tab = query.replace("switch tab ", "")
                Tab = tab.replace("to", "")
                num = Tab
                pyautogui.keyDown("ctrl")
                pyautogui.press(f"{num}")
                pyautogui.keyUp("ctrl")

            elif "exit" in query and "chrome" in query:

                pyautogui.keyDown("alt")
                pyautogui.press("f4")
                pyautogui.keyUp("alt")
                Speak("Automation mode stop")
                sleep(3)
                return

            elif "search" in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("E")
                pyautogui.keyUp("ctrl")
                str = query.replace("search", "")
                pyautogui.write(str)
                pyautogui.press("enter")
                # if "youtube" in query:
                #     Speak("Do you want automation ")
                #     j=1
                #     while j<=2:
                #         j=j+1
                #         sent=Listening()
                #         if "yes" in sent:
                #             YouTubeAuto()
                        



            elif "stop" in query and "auto" in query:
                Speak("Automation mode stop")
                sleep(3)
                return
            elif len(query) <=3:
                pass
            else :
                Speak("That function is not their")

    except:
        Speak("An unknown error occurred, Sorry sir try again")
# ChromeAuto()