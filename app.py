import PyQt5.uic
from PyQt5.QtWidgets import *
from chatbot import chatbot
import sys
from main import speak, get_audio
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore

print("hello world forked")

class UiMainWindow(QMainWindow):
    def __init__(self):
        super(UiMainWindow, self).__init__()
        PyQt5.uic.loadUi('mainui.ui', self)
        self.talked = False
        self.submit.clicked.connect(self.onsend)
        self.voiceinput.clicked.connect(self.onvoice)
        self.btn_toggle.clicked.connect(self.toggleclick)
        self.sidemenu = False

    def talk(self, text):
        if text == "" and self.talked:
            self.chatrec.append('EVA: {}'.format(str("Sorry, I didn't get that. Please try again.")))
            self.chatrec.repaint()
            speak("Sorry, I didn't get that. Please try again.")
            self.talked = False
            return
        elif text == "" and not self.talked:
            return
        self.chatrec.append("You: {}".format(text))
        output = str(chatbot(text))
        self.chatrec.append('EVA: {}'.format(output))
        self.textinput.setText("")
        self.chatrec.repaint()
        speak(output)

    def onsend(self):
        self.talk(self.textinput.text())

    def onvoice(self):
        userinput = get_audio()
        self.talked = True
        self.talk(userinput)

    def toggleclick(self):
        if self.sidemenu:
            self.toggleMenu(False)
        else:
            self.toggleMenu(True)

    def toggleMenu(self, enable):
        if enable:
            self.sidemenu = True
            self.side_frame.setFixedWidth(250)
        else:
            self.sidemenu = False
            self.side_frame.setFixedWidth(70)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = UiMainWindow()
    widget.show()
    sys.exit(app.exec_())
