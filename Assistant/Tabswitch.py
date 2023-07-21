import pyautogui as pa
import time


def tabswitch():
    pa.keyDown('alt')
    pa.press('tab')
    time.sleep(0.2)
    pa.keyUp('alt')
    time.sleep(2)
