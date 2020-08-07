# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Swimming Macro")
        MainWindow.resize(932, 1232)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #제목라인
        self.Title = QtWidgets.QTextBrowser(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(130, 70, 671, 121))
        self.Title.setObjectName("Title")


        #ID 입력
        self.input_id = QtWidgets.QLineEdit(self.centralwidget)
        self.input_id.setGeometry(QtCore.QRect(320, 260, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.input_id.setFont(font)
        self.input_id.setText("")
        self.input_id.setObjectName("input_id")
        self.label_ID = QtWidgets.QLabel(self.centralwidget)
        self.label_ID.setGeometry(QtCore.QRect(140, 210, 171, 141))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)

        #ID 라벨
        self.label_ID.setFont(font)
        self.label_ID.setObjectName("label_ID")
        self.label_pw = QtWidgets.QLabel(self.centralwidget)
        self.label_pw.setGeometry(QtCore.QRect(140, 350, 171, 141))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.label_pw.setFont(font)
        self.label_pw.setObjectName("label_pw")
        self.input_pw = QtWidgets.QLineEdit(self.centralwidget)
        self.input_pw.setGeometry(QtCore.QRect(320, 390, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.input_pw.setFont(font)
        self.input_pw.setText("")
        self.input_pw.setObjectName("input_pw")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(320, 510, 271, 131))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(36)
        self.btn_login.setFont(font)
        self.btn_login.setObjectName("btn_login")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 740, 961, 16))
        self.line.setLineWidth(9)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(130, 780, 171, 141))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label_time.setFont(font)
        self.label_time.setObjectName("label_time")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(330, 830, 441, 51))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.btn_apply = QtWidgets.QPushButton(self.centralwidget)
        self.btn_apply.setGeometry(QtCore.QRect(320, 930, 311, 101))
        font = QtGui.QFont()
        font.setFamily("Haettenschweiler")
        font.setPointSize(36)
        self.btn_apply.setFont(font)
        self.btn_apply.setObjectName("btn_apply")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 932, 38))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600;\">수영장 매크로</span></p></body></html>"))
        self.label_ID.setText(_translate("MainWindow", "I D"))
        self.label_pw.setText(_translate("MainWindow", "PW"))
        self.btn_login.setText(_translate("MainWindow", "Log In"))
        self.label_time.setText(_translate("MainWindow", "Time"))
        self.comboBox.setItemText(0, _translate("MainWindow", "06:00-07:30"))
        self.comboBox.setItemText(1, _translate("MainWindow", "08:00-09:30"))
        self.comboBox.setItemText(2, _translate("MainWindow", "10:00-11:30"))
        self.comboBox.setItemText(3, _translate("MainWindow", "12:00-13:30"))
        self.comboBox.setItemText(4, _translate("MainWindow", "14:00-15:30"))
        self.comboBox.setItemText(5, _translate("MainWindow", "16:00-17:30"))
        self.comboBox.setItemText(6, _translate("MainWindow", "18:00-19:30"))
        self.btn_apply.setText(_translate("MainWindow", "Run"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

