from features import Assistant
from feature_files.natural_language import talk
import json
import inspect
from feature_files.speak_and_get_audio import speak
from PyQt5 import QtGui
from PyQt5.QtCore import QThread
import speech_recognition as sr
from PyQt5 import QtCore

TEXT = ''

try:
    with open("feature_files/data/userdata.json", "r+") as d:
        data = dict(json.load(d))
        d.close()
    write = open("feature_files/data/userdata.json", "w")


    if data.get("signedin") == 0:
        username = input("Enter your name: ")
        data["signedin"] = 1

    if data.get("botname") == "":
        name = input("Enter bot's name: ")
        data['botname'] = name
    else:
        name = data.get("botname")

    json.dump(data, write)

    write.close()

    print("The data you enter here is stored on your device and not sent anywhere else.")
    print()

    bot = Assistant(name)
except:
    bot = Assistant("Zen")

import PyQt5.uic
from PyQt5.QtWidgets import *
import sys


class MainBackgroundThread(QThread):
    def __init__(self, text):
        QThread.__init__(self)
        self.text = text
    def run(self):
        speak(self.text)


class VoiceWorker(QtCore.QObject):
    textChanged = QtCore.pyqtSignal(str)

    @QtCore.pyqtSlot()
    def task(self):
        r = sr.Recognizer()
        m = sr.Microphone()
        while True:
            print("Say somethig!")
            with m as source:
                audio = r.listen(source)
                print("Got it! Now to recognize it...")
                try:
                    global TEXT
                    value = r.recognize_google(audio)
                    TEXT = value
                    print("You said: {}".format(value))
                except sr.UnknownValueError:
                    print("Oops")


class UiMainWindow(QMainWindow):
    def __init__(self):
        super(UiMainWindow, self).__init__()
        PyQt5.uic.loadUi('UI/main.ui', self)
        self.submit.clicked.connect(self.onsend)
        # self.voiceinput.clicked.connect(worker.task)
        self.parameter_entered = False
        self.parameter = None
        self.current_function = None


    def onsend(self):
        text = self.textinput.toPlainText().lower()
        if self.parameter_entered:
            self.parameter = str(text)
        if not self.parameter is None and not self.current_function is None:
            res = self.current_function(self.parameter, reqs_confirm=False)
            self.chatrec.setText("{}\n{}".format(self.chatrec.toPlainText(), res))
            QtGui.QGuiApplication.processEvents()
            self.worker = MainBackgroundThread(res)
            self.worker.start()
            self.parameter_entered = False
            self.current_function = None
            self.parameter = None
            return
        x = self.return_response(text)
        if isinstance(x, dict):
            res = x.get("error")
            self.chatrec.setText("{}\n{}".format(self.chatrec.toPlainText(), res))
            self.parameter_entered = True
            QtGui.QGuiApplication.processEvents()
            self.worker = MainBackgroundThread(res)
            self.worker.start()
            return
        self.chatrec.append(x)
        QtGui.QGuiApplication.processEvents()
        self.worker = MainBackgroundThread(x)
        self.worker.start()
        self.textinput.setText("")

    def return_response(self, text=''):
        x = talk(text)
        if x[1] == "function":
            a = inspect.getmembers(Assistant)
            y = getattr(bot, x[0])
            result = y()
            if isinstance(result, dict):
                if self.parameter_entered:
                    return y(self.parameter, reqs_confirm=False)
                else:
                    self.current_function = y
                    return result
            else:
                return result
        else:
            return x[0]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = UiMainWindow()
    widget.show()
    sys.exit(app.exec_())


