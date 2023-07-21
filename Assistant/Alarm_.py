from datetime import datetime
import threading
from Speak import Speak
from playsound import playsound


def checkalarm():
    al = True
    with open("Database\\setalarm.txt", "r") as r:
        data = r.read()
        mint = int(data.split(" ")[1])
        hou = int(data.split(" ")[0])
    while al == True:
        data = str(datetime.now().strftime('%H:%M:%S'))
        hour = int(data.split(":")[0])
        minute = int(data.split(":")[1])
        if (hour == hou):
            if (minute == mint):
                playsound("Database\\alarm.mp3")
                al = False


def setalarm(strn=""):
    try:
        data = str(datetime.now().strftime('%H:%M:%S'))
        hour = data.split(":")[0]
        minute = data.split(":")[1]
        Speak("Alarm is set")
        newmin = ""
        newhou = ""
        li = [i for i in strn.split(" ")]
        i = 0
        while i < len(li):
            if (li[i].isnumeric()):
                if ("h" in li[i+1]):

                    newhou = int(hour)+int(li[i])
                    newmin = int(minute)
                    with open("Database\\setalarm.txt", "w") as w:
                        w.write(str(newhou)+" "+str(newmin))
                    runne = threading.Thread(target=checkalarm, args=())
                    runne.start()
                    return

                else:
                    newmin = int(minute)+int(li[i])
                    newhou = int(hour)
                    timer = newmin

                    if (newmin >= 60):
                        while (timer >= 60):
                            timer = timer-60
                            newhou = newhou+1
                        settime = timer
                        with open("Database\\setalarm.txt", "w") as w:
                            w.write(str(newhou)+" "+str(settime))
                    else:
                        with open("Database\\setalarm.txt", "w") as w:
                            w.write(str(newhou)+" "+str(newmin))

                    runne = threading.Thread(target=checkalarm, args=())
                    runne.start()
                    return
            i = i+1
        Speak("You are not speaking in valid format")
        Speak("Speak like , set alarm for time minutes and hours")

    except:
        Speak("An unknown error occurred, Sorry sir try again")
