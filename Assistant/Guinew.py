from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Assistant")
        Dialog.resize(1650, 900)
        Dialog.setAutoFillBackground(False)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1650, 900))
        self.label.setStyleSheet("background:rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(1110, 120, 461, 251))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("GUI\\earth.gif"))
        self.label_3.setObjectName("label_3")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1650, 900))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("GUI\\backframe.gif"))
        self.label_2.setObjectName("label_2")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(1280, 460, 181, 161))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("GUI\\jarvis.gif"))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(1120, 400, 511, 411))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("GUI\\laptop.png"))
        self.label_5.setObjectName("label_5")

        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(120, 700, 231, 91))
        self.textBrowser.setStyleSheet(
            "background:rgb(0, 0, 0);color:red;font-size:40px;padding: 18px;border-radius:50px")
        self.textBrowser.setObjectName("textBrowser")

        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(380, 700, 231, 91))
        self.textBrowser_2.setStyleSheet(
            "background:rgb(0, 0, 0);color:red;font-size:37px;padding: 15px;")
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(100, 90, 511, 421))
        self.label_10.setStyleSheet("background:transferent;")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("GUI\\input1.png"))
        self.label_10.setObjectName("label_10")

        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(150, 130, 451, 361))
        self.textBrowser_3.setStyleSheet(
            "background:rgb(0, 0, 0);color:green;font-size:15px;padding: 15px;border:none;border-radius:50px")

        self.textBrowser_3.setObjectName("textBrowser_3")

        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(320, 670, 381, 261))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("GUI\\frame.png"))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(60, 680, 451, 241))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("GUI\\frame.png"))
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(730, 260, 411, 381))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("GUI\\voice.gif"))
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(740, 80, 411, 151))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("GUI\\initiating.gif"))
        self.label_9.setObjectName("label_9")

        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(100, 560, 521, 111))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("GUI\\input2.png"))
        self.label_11.setObjectName("label_11")

        self.line_edit = QtWidgets.QLineEdit(Dialog)
        self.line_edit.setGeometry(QtCore.QRect(140, 580, 470, 75))
        self.line_edit.setStyleSheet(
            "background:rgb(0, 0, 0);color:red;font-size:23px;padding: 15px;border:none")
        self.line_edit.setObjectName("line_edit")

        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(680, 630, 511, 151))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("GUI\\voice2.gif"))
        self.label_12.setObjectName("label_12")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(520, 420, 40, 40))
        self.pushButton.setText("➕")
        self.pushButton.setStyleSheet("font-size:30px;background:none;color:rgb(255,255,255);border-radius:50px;")
#   (150, 130, 451, 361
        # adding signal and slot 
        self.pushButton.clicked.connect(self.changelabeltext)




        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

    def changelabeltext(self):
  
        # changing the text of label after button get clicked
        # self.label.setText("You clicked PushButton")  
        os.startfile("C:\\Users\\avina\\OneDrive\\Desktop\\Assistant\\Database\\output.txt")
          
  
        # Hiding pushbutton from the main window
        # after button get clicked. 
        # self.pushButton.hide()   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
