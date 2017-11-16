# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogError.ui'
#
# Created: Mon Nov 13 18:00:31 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DialogError(object):
    def setupUi(self, DialogError):
        DialogError.setObjectName("DialogError")
        DialogError.resize(423, 129)
        self.buttonBox = QtGui.QDialogButtonBox(DialogError)
        self.buttonBox.setGeometry(QtCore.QRect(170, 90, 71, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtGui.QLabel(DialogError)
        self.label.setGeometry(QtCore.QRect(60, 40, 341, 31))
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")

        self.retranslateUi(DialogError)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DialogError.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DialogError.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogError)

    def retranslateUi(self, DialogError):
        DialogError.setWindowTitle(QtGui.QApplication.translate("DialogError", "ERROR", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogError", "Connection Failed! Please Check Dongle Connection ", None, QtGui.QApplication.UnicodeUTF8))

