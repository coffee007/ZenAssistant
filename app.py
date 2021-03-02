from PyQt5 import QtCore, QtGui, QtWidgets
from chatbot import chatbot

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(766, 531)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.introlabel = QtWidgets.QLabel(self.centralwidget)
        self.introlabel.setGeometry(QtCore.QRect(110, 10, 571, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.introlabel.setFont(font)
        self.introlabel.setStyleSheet("color: black;\n"
                                      "text-align: center;")
        self.introlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.introlabel.setWordWrap(False)
        self.introlabel.setObjectName("introlabel")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(340, 130, 101, 31))
        self.submit.setObjectName("submit")
        self.submit.clicked.connect(self.onsend)
        self.textinput = QtWidgets.QLineEdit(self.centralwidget)
        self.textinput.setGeometry(QtCore.QRect(260, 70, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.textinput.setFont(font)
        self.textinput.setObjectName("textinput")
        self.chatrec = QtWidgets.QTextEdit(self.centralwidget)
        self.chatrec.setGeometry(QtCore.QRect(170, 180, 461, 361))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.chatrec.setFont(font)
        self.chatrec.setObjectName("chatrec")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 766, 21))
        self.menubar.setAutoFillBackground(True)
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EVA"))
        self.introlabel.setText(_translate("MainWindow", "Hello, I\'m EVA, your virtual assistant!"))
        self.submit.setWhatsThis(_translate("MainWindow", "Send your message to EVA"))
        self.submit.setText(_translate("MainWindow", "Send!"))
        self.textinput.setWhatsThis(_translate("MainWindow", "Enter your message here"))
        self.menubar.setWhatsThis(_translate("MainWindow", "A virtual assistant"))

    def onsend(self):
        self.chatrec.append("You: {}".format(self.textinput.text()))
        self.chatrec.append('EVA: {}'.format(str(chatbot(self.textinput.text()))))
        self.textinput.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())