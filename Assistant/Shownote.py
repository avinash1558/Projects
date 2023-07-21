from Speak import Speak
from Listening import Listening
import datetime
# from Numberlist import NumListening
# import threading
from time import sleep

def impnote():
    try:
        Speak("What should i write, sir")
        i = 1
        while i <= 2:
            i = i+1
            note = Listening()
            if note != "none":
                file = open('Database\\jarvisimp.txt', 'w')
                note = note+"\n"
                strTime = datetime.datetime.now().strftime("@%Y/%m/%d:-\n")
                file.write(strTime)
                file.write(note)
                Speak("Writing done")
                sleep(2)

                return
            else:
                if i == 3:
                    Speak("Sorry Sir try next time")

                else:
                    Speak("What should i write sir, tell again")
        Speak("i am terminating you command")
        sleep(2)
    except:
        Speak("An unknown error occurred, Sorry sir try again")
        sleep(2)


def reminder():
    try:
        Speak("What should i write, sir")
        i = 1
        while i <= 2:
            i = i+1
            note = Listening()
            if note != "none":
                file = open('Database\\jarvisre.txt', 'w')
                note = note+"\n"
                strTime = datetime.datetime.now().strftime("@%Y/%m/%d:-\n")
                file.write(strTime)
                file.write(note)
                Speak("Writing done")
                sleep(2)

                with open("Database\\count.txt", "w") as w:
                    w.write("1")
                return
            else:
                if i == 3:
                    Speak("Sorry Sir try next time")
                else:
                    Speak("What should i write sir, tell again")
        Speak("i am terminating you command")
        sleep(2)
    except:
        Speak("An unknown error occurred, Sorry sir try again")
        sleep(2)


def readimp():
    try:
        Speak("Important notes is ")
        file = open("Database\\jarvisimp.txt", "r")

        Speak(file.read())
        Speak("reading done")
        sleep(2)
    except:
        Speak("An unknown error occurred, Sorry sir try again")


def speakrem():
    try:
        Speak("Today reminder is ")
        file = open("Database\\jarvisre.txt", "r")
        Speak(file.read())
    except:
        Speak("An unknown error occurred, Sorry sir try again")


def writenote():
    try:
        Speak("What should i write, sir")
        i = 1
        while i <= 2:
            i = i+1
            note = Listening()
            if note != "none":
                file = open('Database\\writenote.txt', 'a')
                note = note+"\n"
                strTime = datetime.datetime.now().strftime("@%Y/%m/%d  =  %H:%M:%S  :-\n")
                file.write(strTime)
                file.write(note)
                Speak("Writing done")
                return
            else:
                if i == 3:
                    Speak("Sorry Sir try next time")
                else:
                    Speak("What should i write sir, tell again")
        Speak("i am terminating you command")
        
    except:
        Speak("An unknown error occurred, Sorry sir try again")


def readnote():
    Speak("Tell me day and month")
    Speak("Tell month first ")
    i = 1
    try:
        while i <= 2:
            i = i+1
            mon = Listening()
            if mon != "none":
                resm = [int(i) for i in mon.split() if i.isdigit()]
                if resm:
                    Speak("Tell day ")
                    j = 1
                    while j <= 2:
                        j = j+1
                        day = Listening()
                        if day != "none":
                            resd = [int(i) for i in day.split() if i.isdigit()]
                            file = open("Database\\writenote.txt", "r")
                            pat = file.read()
                            data = pat.split('@')
                            check = str(resm[0])+"/"+str(resd[0])
                            for c in data:
                                if check in c:
                                    Speak(c)
                                    Speak("reading done")
                                    sleep(2)
                                    return
                            Speak("day is not proper")
                            return

                        else:
                            if j == 3:
                                Speak("Sorry Sir try next time")
                            else:
                                Speak("Tell again")
                else:
                    if i == 3:
                        Speak("Sorry Sir try next time")
                    else:
                        Speak("Tell again")
            else:
                if i == 3:
                    Speak("Sorry Sir try next time")
                else:
                    Speak("Tell again")
        Speak("i am terminating you command")
        

    except:
        Speak("An unknown error occurred, Sorry sir try again")
