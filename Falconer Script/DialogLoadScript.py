# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogLoadScript.ui'
#
# Created: Mon Nov 13 18:00:33 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DialogLoadScript(object):
    def setupUi(self, DialogLoadScript):
        DialogLoadScript.setObjectName("DialogLoadScript")
        DialogLoadScript.resize(386, 150)
        self.label = QtGui.QLabel(DialogLoadScript)
        self.label.setGeometry(QtCore.QRect(40, 20, 121, 16))
        self.label.setObjectName("label")
        self.pushButton = QtGui.QPushButton(DialogLoadScript)
        self.pushButton.setGeometry(QtCore.QRect(230, 50, 131, 31))
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtGui.QLabel(DialogLoadScript)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 151, 31))
        self.label_2.setStyleSheet("background-color: rgb(165, 165, 165);")
        self.label_2.setObjectName("label_2")
        self.pushButton_OK = QtGui.QPushButton(DialogLoadScript)
        self.pushButton_OK.setGeometry(QtCore.QRect(260, 100, 75, 23))
        self.pushButton_OK.setObjectName("pushButton_OK")

        self.retranslateUi(DialogLoadScript)
        QtCore.QMetaObject.connectSlotsByName(DialogLoadScript)

    def retranslateUi(self, DialogLoadScript):
        DialogLoadScript.setWindowTitle(QtGui.QApplication.translate("DialogLoadScript", "Load Alternate Script", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogLoadScript", "Current Script:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("DialogLoadScript", "Load Another Script", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogLoadScript", "aaaaaa", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_OK.setText(QtGui.QApplication.translate("DialogLoadScript", "OK", None, QtGui.QApplication.UnicodeUTF8))

