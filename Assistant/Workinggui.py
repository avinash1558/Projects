import pyautogui as p
from datetime import datetime, time
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from Guinew import Ui_Dialog
import sys
from datetime import datetime
from PDFreader_ import pdfreader
from PDFreader_ import pdfaudio
from Handwriting import texttohand, pdftohand
import threading
from Bravo import MainLoop


def threaduse(text, mod):
    if mod == "read":
        pdfreader(text)
    if mod == "audio":
        pdfaudio(text)
    if mod == "texthand":
        texttohand(text)
    if mod == "pdfhand":
        pdftohand(text)


def runner():
    class MainThread(QThread):

        def __init__(self):
            with open("Database\\run.txt", 'w') as w:
                w.write("")
            mainlo = threading.Thread(target=MainLoop, args=())
            mainlo.start()
            super(MainThread, self).__init__()

    startFunctions = MainThread()

    class Gui_Start(QMainWindow):

        def __init__(self):
            super().__init__()
            self.jarvis_ui = Ui_Dialog()
            self.jarvis_ui.setupUi(self)
            self.startFunc()

        def startFunc(self):
            self.jarvis_ui.movies = QtGui.QMovie("GUI\\earth.gif")
            self.jarvis_ui.label_3.setMovie(self.jarvis_ui.movies)
            self.jarvis_ui.movies.start()

            self.jarvis_ui.movies_2 = QtGui.QMovie("GUI\\jarvis.gif")
            self.jarvis_ui.label_4.setMovie(self.jarvis_ui.movies_2)
            self.jarvis_ui.movies_2.start()

            self.jarvis_ui.movies_3 = QtGui.QMovie("GUI\\voice.gif")
            self.jarvis_ui.label_8.setMovie(self.jarvis_ui.movies_3)
            self.jarvis_ui.movies_3.start()

            self.jarvis_ui.movies_4 = QtGui.QMovie("GUI\\voice2.gif")
            self.jarvis_ui.label_12.setMovie(self.jarvis_ui.movies_4)
            self.jarvis_ui.movies_4.start()

            self.jarvis_ui.movies_5 = QtGui.QMovie("GUI\\initiating.gif")
            self.jarvis_ui.label_9.setMovie(self.jarvis_ui.movies_5)
            self.jarvis_ui.movies_5.start()
            self.jarvis_ui.textBrowser_2.setText(
                str(datetime.now().strftime('%d/%m/%Y')))

            timer = QTimer(self)

            timer.timeout.connect(self.showtime)

            timer.start(1000)
            timer1 = QTimer(self)

            timer1.timeout.connect(self.output)

            timer1.start(1000)

            startFunctions.start()
            self.jarvis_ui.line_edit.returnPressed.connect(self.do_action)

        def showtime(self):
            self.jarvis_ui.textBrowser.setText(
                str(datetime.now().strftime('%H:%M:%S')))

        def output(self):
            with open("Database\\output.txt","r") as r:
                text=r.read()
                li=[i for i in text.split("\n")]
                str1=""
                length=len(li)#40
                # print(int(length))
                if(int(length)>1):
                    if(int(length)<=16):
                        i=0
                        while i<int(length):
                            str1=str1+str(li[i])+"\n"
                            i=i+1
                    else:
                        i=int(length)-16 #24
                        while i<int(length):
                            str1=str1+str(li[i])+"\n"
                            i=i+1
                # print(str1)

            self.jarvis_ui.textBrowser_3.setText(str1)

        def do_action(self):
            text = self.jarvis_ui.line_edit.text()
            self.jarvis_ui.line_edit.setText("")
            with open("Database\\pdf.txt", "r") as r:
                mod = str(r.read())
                if (len(mod) > 3):
                    t1 = threading.Thread(target=threaduse, args=(text, mod,))
                    t1.start()
            with open("Database\\pdf.txt", "w") as w:
                w.write("")

    Gui_App = QApplication(sys.argv)

    Gui_Jarvis = Gui_Start()

    Gui_Jarvis.show()
    if (Gui_App.exec_() == 0):
        with open("Database\\output.txt", 'w') as w:
            w.write("")
        with open("Database\\run.txt", 'w') as w:
            w.write("1")
    exit(Gui_App.exec_())


runner() 
