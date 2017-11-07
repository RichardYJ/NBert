import sys
from PySide.QtGui import *
from falcon_lib import *
from WinGui_PySide import Ui_MainWindow
from PySide import QtCore, QtGui

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.lib=Falcon_lib()

    def refresh_GUI(self):
        self.QSFP1_AR1_LS_label.setText(QtGui.QApplication.translate("MainWindow", "111111", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP1_AR1_EM_label.setText(QtGui.QApplication.translate("MainWindow", "222222", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP1_AR1_BR_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP1_AR1_PF_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP1_AR2_LS_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP1_AR2_PF_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP1_AR2_EM_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP1_AR2_BR_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP1_AR3_LS_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP1_AR3_PF_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP1_AR3_EM_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP1_AR3_BR_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP1_AR4_LS_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP1_AR4_PF_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP1_AR4_EM_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP1_AR4_BR_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
    
        self.QSFP2_AR1_LS_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP2_AR1_EM_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP2_AR1_BR_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP2_AR1_PF_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP2_AR2_LS_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP2_AR2_PF_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP2_AR2_EM_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP2_AR2_BR_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP2_AR3_LS_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP2_AR3_PF_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP2_AR3_EM_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP2_AR3_BR_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP2_AR4_LS_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP2_AR4_PF_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP2_AR4_EM_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.QSFP2_AR4_BR_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

        self.SFP1_AR1_BR_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP1_AR1_EM_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP1_AR1_PF_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP1_AR1_LS_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP1_AR2_BR_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP1_AR2_EM_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP1_AR2_PF_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP1_AR2_LS_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP1_AR3_BR_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP1_AR3_EM_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP1_AR3_PF_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP1_AR3_LS_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP1_AR4_BR_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP1_AR4_EM_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP1_AR4_PF_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP1_AR4_LS_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

        if self.link_stat(i) == 1:
            link[i - 1].config(text='ON', bg='green')
            if self.ber(i) <= 1e-13:
                fail[i - 1].config(text='PASS', bg='green')
            else:
                fail[i - 1].config(text='FAIL', bg='red')
        else:
            link[i - 1].config(text='OFF', bg='red')
            fail[i - 1].config(text='FAIL', bg='red')

        if self.link_stat(1) == 1:
            self.QSFP1_AR1_LS_label.setStyleSheet("background-color: rgb(255, 255, 0);")