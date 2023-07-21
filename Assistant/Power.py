import psutil
from Speak import Speak
from time import sleep

def power():
    try:
        battery = psutil.sensors_battery()
        perT = battery.percent
        Speak(f"sir our system have {perT} percent battery")
        if perT <= 85 and perT >= 60:
            Speak("we have enough power to continue our work")
        elif perT >= 30 and perT <= 60:
            Speak("we should connect our system to charging point to charge our battery")
        elif perT > 15 and perT <= 30:
            Speak("we don't have enough poer to work, please connect to charging")
        elif perT <= 15:
            Speak(
                "we have very low power, please connect to charging the system will shutdown very soon")
        sleep(2)
            
    except:
        Speak("An unknown error occurred, Sorry sir try again")
        sleep(2)
