from datetime import datetime
import pywhatkit
import json
from Listening import Listening
from Speak import Speak
from time import sleep

def Jsondata(mainname):
    jscode = {}
    with open("DataBase\\whatsapp.json", "r") as r:
        jscode = json.load(r)
        return jscode[mainname]


def Sendwhatsapp(str):
    data = Jsondata("contact")
    sendNo = ""
    to = "none"
    li = [i for i in data.keys()]
    for i in li:
        if i in str:
            to = i
            break

    if to != "none":
        sendNo = data[to]
        sentence = ""
        Speak(f"Preparing To Send a Message To {to}")

        while True:
            Speak("tell me what i have to send")
            sentence = Listening()
            if sentence != "none":
                Speak(f"Sir i have to send {sentence} to {to}")
                Speak("it is correct or not")
                i = 1
                while i <= 2:
                    senten = Listening()
                    i = i+1

                    if ("yes" in senten or "ok" in senten or "correct" in senten):
                        Speak("Wait a second")
                        try:
                            data = datetime.now().strftime('%H:%M')
                            hour = data.split(":")[0]
                            minute = data.split(":")[1]
                            newmin = int(minute)+2
                            newhou = int(hour)

                            if (newmin >= 60):
                                newmin = newmin-60
                                newhou = newhou+1
                            pywhatkit.sendwhatmsg(
                                sendNo, sentence, int(newhou), newmin, 12)
                            return 
                        except:
                            Speak("Invalid Number")
                            sleep(2)
                            return
                        break
                    if ("no" in senten):
                        break
                
    else:
        Speak("Sorry sir that name is not mention document")
        Speak("Sir please add in document")
# Sendwhatsapp("send message to me")