from Speak import Speak
import os
import time
from gtts import gTTS
import random
import PyPDF2


def pathcheck(value=""):
    if ('\\' in value):
        value = value.replace("\\", "\\\\")
        return value

    if ("/" in value):
        value = value.replace("/", "\\\\")
        return value
    else:
        return value


def audiofile(str, file):
    """
    its take string and speak that string
    """
    try:
        gtt = gTTS(text=str)
        li = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        file = random.choice(li)+file
        gtt.save(file)
        time.sleep(0.2)
    except:
        Speak("sorry i am not able to create audio file")


def pdfreader(value=""):
    if len(value) >= 3:
        try:
            if " " in value:
                path = value.split(" to ")[0]
                path = pathcheck(path)
                pdfFileObj = open(path, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                Speak(
                    f"Total number of pages in this pdf is {pdfReader.numPages}.")
                pageno = value.split(" to ")[1]
                Speak(f"I am reading from page number {pageno}.")
                pageObj = pdfReader.getPage(int(pageno))
                Speak(pageObj.extractText())
                Speak("PDF reding is done")
            else:
                path = value
                path = pathcheck(path)
                pdfFileObj = open(path, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                Speak(
                    f"Total number of pages in this pdf is {pdfReader.numPages}")

                Speak("I am reading from 1 ")
                pageObj = pdfReader.getPage(1)
                Speak(pageObj.extractText())
                Speak("I am reading from 2 ")

                pageObj = pdfReader.getPage(2)
                print(pageObj.extractText())
                print(type(pageObj.extractText()))
                Speak(pageObj.extractText())
                Speak("PDF reding is done")
            with open("Database\\execontrol.txt", "w") as w:
                w.write("2")
            pdfFileObj.close()
        except:
            Speak("You are not entering data in valid format please, try again")
            with open("Database\\execontrol.txt", "w") as w:
                w.write("2")

# pdfreader("C:/Users/avina/OneDrive/Desktop/College/tyit.pdf to 30")


def pdfaudio(value=""):
    if len(value) >= 3:
        try:
            if " " in value:
                path = value.split(" to ")[0]
                path = pathcheck(path)
                pdfFileObj = open(path, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                Speak(
                    f"Total number of pages in this pdf is {pdfReader.numPages}")
                pageno = value.split("to ")[1]
                Speak(f"I am creating audio file from page number {pageno}")
                Speak("Wait For Few Seconds")
                pageObj = pdfReader.getPage(int(pageno))
                data = pageObj.extractText()
                file = path.split("\\")[-1]
                filename = file.split(".")[0]+".mp3"
                audiofile(data, filename)
                Speak("audio creation is done")

            else:
                path = value
                path = pathcheck(path)
                pdfFileObj = open(path, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                Speak(
                    f"Total number of pages in this pdf is {pdfReader.numPages}")
                Speak("i am reading from 1 ")

                pageObj = pdfReader.getPage(1)
                data = pageObj.extractText()
                file = path.split("\\\\")[-1]
                filename = file.split(".")[0]+"mp3"
                audiofile(data, filename)
                Speak("audio creation is done")
            with open("Database\\execontrol.txt", "w") as w:
                w.write("2")
            pdfFileObj.close()
        except:
            Speak("You are not entering data in valid format please, try again")
            with open("Database\\execontrol.txt", "w") as w:
                w.write("2")

