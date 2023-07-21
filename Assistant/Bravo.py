from Listening import Listening
from QuesReply import QuestionsAnswer
from ReplyBrain import ReplyBrain
from Speak import Speak
from OpenApp import OpenApp
from OpenApp import closeapp
from OpenApp import closeall
from OpenApp import OpenSite
from Jokes_ import E_Jokes
from Jokes_ import H_Jokes
from Email import Mail
from Speedtest import Speedtesting
from Power import power
from Newsreader import readnews
from Findlocation import location
from Googlesearch import searchongoogle,searchonWIKI
from Textreader import textreader
from Systemfunction import *
from Musicplay import *
from Tabswitch import tabswitch
from Howto import howto
from Shownote import *
from Handwriting import Seltexttohand
from Whatsapp import Sendwhatsapp
import winshell
from Name_ import name_
from Starting import starting
from Alarm_ import setalarm
import time
import pyautogui
from Changename import namechange
from Youtubeauto import SearchYou

def MainLoop():
    # starting()
    sentence = ""
    i = 2
    while True:
        with open("Database\\run.txt", 'r') as r:
            run = r.read()
        if "1" in run:
            # print("ywy")
            return
        else:
            sentence = Listening()
            if i == 1:
                pass
            elif "none" in sentence:
                pass

            elif len(sentence) < 4:
                pass


            elif "send" in sentence and "message" in sentence :
                Sendwhatsapp(sentence)
                Speak("message is send")

            elif "send" in sentence and "mail" in sentence:
                # send mail to user
                Mail(sentence)

            



            elif ("create" in sentence and "important" in sentence and "note" in sentence) or ("take" in sentence and "note" in sentence and "important" in sentence) or ("write" in sentence and "important" in sentence and "note" in sentence or "right" in sentence and "important" in sentence and "note" in sentence):
                impnote()

            elif "read" in sentence and "important" in sentence and "note" in sentence or "tell" in sentence and "important" in sentence and "note" in sentence:
                readimp()

            elif "create" in sentence and "reminder" in sentence or "take" in sentence and "reminder" in sentence or ("write" in sentence and "reminder" in sentence and "note" in sentence) or "right" in sentence and "reminder" in sentence and "note" in sentence:
                reminder()


            elif "read" in sentence and "reminder" in sentence or "tell" in sentence and "reminder" in sentence:
                speakrem()
                Speak("reading done")
                sleep(2)

            elif "read" in sentence and "note" in sentence or "tell" in sentence and "note" in sentence:
                # read note
                readnote()

            elif ("create" in sentence and "note" in sentence) or ("take" in sentence and "note" in sentence) or ("write" in sentence and "note" in sentence or "right" in sentence and "note" in sentence):
                # take note
                writenote()
                sleep(2)

        
            elif "read" in sentence and "pdf" in sentence or "read" in sentence and "document" in sentence or "read" in sentence and "file" in sentence:
                # read pdf 
                # C:/Users/avina/OneDrive/Desktop/College/tyit.pdf to 30
                exe = ""
                Speak("Enter path and page number into input box.")
                with open("Database\\pdf.txt", "w") as w:
                    w.write('read')
                with open("Database\\execontrol.txt", "w") as w:
                    w.write("1")
                with open("Database\\execontrol.txt", "r") as r:
                    exe = r.read()
                while exe == "1":
                    with open("Database\\execontrol.txt", "r") as r:
                        exe = r.read()

            elif "create" in sentence and "audio" in sentence and "file" in sentence or "convert" in sentence and "audio" in sentence and "file" in sentence:
                # create audio file convert 
                # C:/Users/avina/OneDrive/Desktop/College/tyit.pdf to 30
                exe = ""
                Speak("Enter path and page number into input box.")
                with open("Database\\pdf.txt", "w") as w:
                    w.write('audio')
                with open("Database\\execontrol.txt", "w") as w:
                    w.write("1")
                with open("Database\\execontrol.txt", "r") as r:
                    exe = r.read()
                while exe == "1":
                    with open("Database\\execontrol.txt", "r") as r:
                        exe = r.read()

            elif "convert" in sentence and "handwrit" in sentence and ("pdf" in sentence or "convert" in sentence and "handwrit" in sentence and "file" in sentence):
                # convert pdf in handwritting
                exe = ""
                Speak("Enter path and page number into input box.")
                with open("Database\\pdf.txt", "w") as w:
                    w.write('pdfhand')
                with open("Database\\execontrol.txt", "w") as w:
                    w.write("1")
                with open("Database\\execontrol.txt", "r") as r:
                    exe = r.read()
                while exe == "1":
                    with open("Database\\execontrol.txt", "r") as r:
                        exe = r.read()

            elif "convert" in sentence and "text" in sentence and "handwrit" in sentence or "give" in sentence and "text" in sentence and "handwrit" in sentence or "text" in sentence and "handwrit" in sentence and "in" in sentence:
                # convert give text in handwritting
                exe = ""
                Speak("Enter path and page number into input box.")
                with open("Database\\pdf.txt", "w") as w:
                    w.write('texthand')
                with open("Database\\execontrol.txt", "w") as w:
                    w.write("1")
                with open("Database\\execontrol.txt", "r") as r:
                    exe = r.read()
                while exe == "1":
                    with open("Database\\execontrol.txt", "r") as r:
                        exe = r.read()

            elif "convert" in sentence and "text" in sentence and "handwrit" in sentence and "select" in sentence:
                Seltexttohand()

            elif "read" in sentence and "text" in sentence:
                textreader()
                Speak("reading done")
                sleep(1)

            elif "volume" in sentence and "up" in sentence or "volume" in sentence and "increase" in sentence:
                VolUp()

            elif "volume" in sentence and "down" in sentence or "volume" in sentence and "decrease" in sentence:
                VolDown()

            elif "volume" in sentence and "mute" in sentence:
                VolMute()

            elif "shutdown" in sentence and "pc" in sentence or "laptop" in sentence or "device" in sentence:
                Shutdown()

            elif "restart" in sentence and "pc" in sentence or "laptop" in sentence or "device" in sentence:
                Restart()

            elif "logout" in sentence and "pc" in sentence or "laptop" in sentence or "device" in sentence:
                Logout()

        

            elif "search" in sentence and "youtube" in sentence :
                SearchYou(sentence)

            elif "search" in sentence and "wikipedia" in sentence :
                searchonWIKI(sentence)
                
            elif "search" in sentence and "google" in sentence or "search" in sentence:
                # search avinash on google
                searchongoogle(sentence)

            elif "today" in sentence and "news" in sentence:
                # today news
                readnews()

            elif "net" in sentence and "speed" in sentence:
                Speak("Wait sir, let me check")
                Speak(Speedtesting())
                sleep(2)

            

            # How much power is there in the battery
            elif "power" in sentence and "battery" in sentence or "percent" in sentence or  "battery" in sentence:
                # tell me power of battery
                power()

            
            elif "where" in sentence and "are" in sentence and "we" in sentence or "what" in sentence and "location" in sentence or "where" in sentence and "i" in sentence and "am" in sentence:
                # where we are
                location()
            
            elif "play" in sentence and "music" in sentence or "play" in sentence or "song" in sentence:
                #  play music 
                playmusic()

            elif "play" in sentence and "video" in sentence:
                # play music video
                playvideo()

            elif ("open" in sentence and "app" in sentence) or "start" in sentence and "app" in sentence or ("launch" in sentence and "app" in sentence):
                OpenApp(sentence)

            # open apdroid application y app 
            elif "open" in sentence or "launch" in sentence:
                # open google.com launch
                OpenSite(sentence)

            elif "switch" in sentence and "tab" in sentence or "switch" in sentence and "window" in sentence or "change" in sentence and "tab" in sentence:
                tabswitch()

            

            elif "close" in sentence and "app" in sentence or "close" in sentence and "tab" in sentence:
                # close app
                closeapp()

            elif "close" in sentence and "all" in sentence and "app" in sentence:
                closeall()


            elif "tell" in sentence and "joke" in sentence or "speak" in sentence and "joke" in sentence or "say" in sentence and "joke" in sentence or "tail" in sentence and "joke" in sentence:
                # tell me jokes / speak joke
                if "english" in sentence:
                    E_Jokes()
                else:
                    H_Jokes()

            elif "how to" in sentence:
                # how to drive a car
                howto()

            elif 'empty' in sentence and "recycle" in sentence and "bin" in sentence:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                Speak("Recycle Bin Recycled")

            elif "by" in sentence and name_() in sentence or "by" in sentence and "babu" in sentence or ("exit" in sentence or "close" in sentence and name_() in sentence) or "buy" in sentence and name_() in sentence:
                Speak("Okay Sir bye have a nice day")
                exit(0)

            elif "sleep" in sentence and name_() in sentence:
                li = [i for i in sentence.split(" ")]
                i = 0

                while i < len(li):
                    if (li[i].isnumeric()):
                        Speak(f"I am sleeing for {li[i]}")
                        time.sleep(int(li[i])*60)

            elif "sleep" in sentence and "play" in sentence:
                li = [i for i in sentence.split(" ")]
                i = 0
                while i < len(li):
                    if (li[i].isnumeric()):
                        time.sleep(int(li[i])*60)
                pyautogui.press("space")
                

            elif "set" in sentence and "alarm" in sentence:
                setalarm(sentence)

            elif "what is" in sentence or "what are" in sentence or "what should" in sentence or "what was" in sentence or "when is" in sentence or "when are" in sentence or "when should" in sentence or "when was" in sentence or "where is" in sentence or "where are" in sentence or "where should" in sentence or "where was" in sentence or "who is" in sentence or "who are" in sentence or "who should" in sentence or "which was" in sentence or "which is" in sentence or "which are" in sentence or "which should" in sentence or "who was" in sentence or "why is" in sentence or "why are" in sentence or "why should" in sentence or "why was" in sentence or "question" in sentence or "answer" in sentence or "code" in sentence:
                #  What, when, where, whose, Who, How, Whom, Why व Which.
                if "question" in sentence:
                    sentence = sentence.replace("question", "")
                if "answer" in sentence:
                    sentence = sentence.replace("answer", "")
                question = QuestionsAnswer(sentence)
                Speak(question)
                sleep(2)
            else:
                reply = ReplyBrain(sentence)
                Speak(reply)
                sleep(2)


# MainLoop()
