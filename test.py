from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
import speech_recognition as sr
import sys

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
                    value = r.recognize_google(audio)
                    self.textChanged.emit(value)
                    print("You said: {}".format(value))
                except sr.UnknownValueError:
                    print("Oops")

def Gui():
    app = QtWidgets.QApplication(sys.argv)

    worker = VoiceWorker()
    thread = QtCore.QThread()
    thread.start()
    worker.moveToThread(thread)

    window = QtWidgets.QWidget()
    window.setGeometry(200, 200, 350, 400)
    window.setWindowTitle("Assistant")

    title_label = QtWidgets.QLabel(window)
    title_label.setText("Assistant")
    title_label.move(135,10)
    title_label.setFont(QtGui.QFont("SansSerif", 15))

    programs_says = QtWidgets.QLabel(window)
    programs_says.setText("Programs Says")
    programs_says.move(240,100)

    you_says = QtWidgets.QLabel(window)
    you_says.move(25,100)


    you_text = QtWidgets.QLabel(window)
    worker.textChanged.connect(you_text.setText)
    you_text.move(25,150)


    start_button = QtWidgets.QPushButton("Start")
    close_button = QtWidgets.QPushButton("Close")


    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addWidget(start_button)
    v_box.addWidget(close_button)
    window.setLayout(v_box)

    start_button.clicked.connect(worker.task)
    close_button.clicked.connect(QCoreApplication.instance().quit)
    window.show()
    sys.exit(app.exec())


Gui()