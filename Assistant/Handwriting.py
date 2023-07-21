from Speak import Speak
from Listening import Listening
import pywhatkit
import random
import PyPDF2
import pyperclip
import pyautogui as p


def Seltexttohand(text):
    Speak("Sir i am converting selected text")
    p.keyDown("ctrl")
    p.press("c")
    p.keyUp("ctrl")
    text = pyperclip. paste()
    if len(text) > 3:

        Speak("Which color you want")
        Speak("Red")  # 255, 0, 0
        Speak("Black")  # 0, 0, 0
        Speak("Blue")  # 0,0, 255
        i = 1
        try:
            while (i <= 2):
                i = i+1
                li = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
                file = random.choice(li)+random.choice(li)
                sentence = Listening()
                spk = file
                if ("red" in sentence or "first" in sentence or "1" in sentence):
                    pywhatkit.text_to_handwriting(
                        text, f"{file}.png", [255, 0, 0])
                elif ("Black" in sentence or "second" in sentence or "2" in sentence):
                    pywhatkit.text_to_handwriting(
                        text, f"{file}.png", [0, 0, 0])
                elif ("Blue" in sentence or "third" in sentence or "3" in sentence):
                    pywhatkit.text_to_handwriting(
                        text, f"{file}.png", [0, 0, 255])
                elif (i == 2):
                    pywhatkit.text_to_handwriting(
                        text, f"{file}.png", [0, 0, 255])
            Speak(f"handwriting file is create with name of {spk}")
        except:
            # Speak("You are not enter valid data")
            Speak("Now this feature is not available")
    else:
        Speak("nothing is selected")

def texttohand(text):
    Speak("Which color you want")
    Speak("Red")  # 255, 0, 0
    Speak("Black")  # 0, 0, 0
    Speak("Blue")  # 0,0, 255
    i = 1
    try:
        while (i <= 2):
            i = i+1
            li = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
            file = random.choice(li)+random.choice(li)
            sentence = Listening()
            spk = file
            if ("red" in sentence or "first" in sentence or "1" in sentence):
                pywhatkit.text_to_handwriting(text, f"{file}.png", [255, 0, 0])
            elif ("Black" in sentence or "second" in sentence or "2" in sentence):
                pywhatkit.text_to_handwriting(text, f"{file}.png", [0, 0, 0])
            elif ("Blue" in sentence or "third" in sentence or "3" in sentence):
                pywhatkit.text_to_handwriting(text, f"{file}.png", [0, 0, 255])
            elif (i == 2):
                pywhatkit.text_to_handwriting(text, f"{file}.png", [0, 0, 255])
        Speak(f"handwriting file is create with name of {spk}.png")
        with open("Database\\execontrol.txt", "w") as w:
            w.write("2")
    except:
        # Speak("You are not enter valid data")
        Speak("Now this feature is not available")
        with open("Database\\execontrol.txt", "w") as w:
            w.write("2")

def pathcheck(value=""):
    if ('\\' in value):
        value = value.replace("\\", "\\\\")
        return value

    if ("/" in value):
        value = value.replace("/", "\\\\")
        return value
    else:
        return value

def pdftohand(value=""):

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
                Speak(f"I am converting page number {pageno}.")
                pages = int(pdfReader.numPages)
                pageObj = pdfReader.getPage(int(pageno))
                text = pageObj.extractText()
                li = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
                file = path.split("\\")[-1]
                filename = file.split(".")[0]+".png"
                file = random.choice(li)+filename
                pywhatkit.text_to_handwriting(text, file, [0, 0, 255])
                Speak("Conversion done")
            else:
                path = value
                path = pathcheck(path)
                pdfFileObj = open(path, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                Speak(
                    f"Total number of pages in this pdf is {pdfReader.numPages}")
                pages = pdfReader.numPages
                if pages <= 20 and pages >= 5:
                    Speak("wait a few second")
                if pages >= 21:
                    Speak("it is taking more time wait sir")
                for i in range(pages):
                    li = ['q', 'w', 'e', 'r', 't',
                          'y', 'u', "h", 'i', 'o', 'p']
                    file = path.split("\\")[-1]
                    filename = file.split(".")[0]+".png"
                    file = random.choice(li)+random.choice(li)+filename
                    pageObj = pdfReader.getPage(i)
                    text = pageObj.extractText()
                    Speak(f"I am converting page number {i}.")
                    pywhatkit.text_to_handwriting(
                        text, f"{file}.png", [0, 0, 255])
                Speak("your work is done")
            with open("Database\\execontrol.txt", "w") as w:
                w.write("2")
                pdfFileObj.close()
        except:
            # Speak("You are not entering data in valid format please, try again")
            Speak("Now this feature is not available")
            with open("Database\\execontrol.txt", "w") as w:
                w.write("2")