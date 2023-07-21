import smtplib
import json
from Listening import Listening
from Speak import Speak
import time
from time import sleep

def Jsondata(mainname):
    """
    is give language code from json file
    """
    jscode = {}
    with open("DataBase\\email.json", "r") as r:
        jscode = json.load(r)
        return jscode[mainname]


def Mail(str):
    """
    send to rohit
    is use to send mail
    """
    try:
        data = Jsondata("email")
        to = ""
        li = [i for i in data.keys()]
        for i in li:
            if i in str:
                to = i
        sendmail = data[to]
        sentence = ""
        
        smtps = "smtp.gmail.com"
        smtphost = 587
        Speak(f"Preparing To Send a Mail To {to}")
        server = smtplib.SMTP(smtps, smtphost)
        server.ehlo()

        server.starttls()
        server.login("deskassitant@gmail.com", "tbmolfkiypqhqfiz")
        Speak("Tell me subject and body of mail")
        time.sleep(0.3)
        Speak("First tell me subject")
        
        i = 0
        while i <= 1:
            i = i+1
            sentence = Listening()
            if sentence != "none" and len(sentence) >= 2:
                subject = sentence
                j = 0
                while j <= 1:
                    j = j+1
                    Speak("Now tell me body of mail ")
                    sentence = Listening()
                    if sentence != "none" and len(sentence) >= 2:
                        body = sentence
                        message = f"Subject : {subject}\n\n{body}"
                        Speak(f"I am sending {message} to {sendmail}")
                        Speak("It is correct ")
                        k = 1
                        while k <= 2:
                            sentence = Listening()
                            k = k+1
                            if "yes" in sentence or "correct" in sentence and "no" not in sentence or "right" in sentence or "write" in sentence:
                                server.sendmail(
                                    "deskassitant@gmail.com", sendmail, message)
                                Speak("Mail is send..")
                                sleep(2)
                                return 0
                            if "correct" in sentence and "yes" not in sentence or "no" in sentence or "wrong" in sentence:
                                Speak("Okay sir try again")
                                return
                    else:
                        Speak("Tell again")
            else:
                Speak("Tell again")
        server.close()
        Speak("i am terminating you command")
        sleep(2)
    except:
        Speak("An unknown error occurred, Sorry sir try again")
        sleep(2)
# Mail("send mail to me")