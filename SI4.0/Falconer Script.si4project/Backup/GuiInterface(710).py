import sys
from PySide.QtGui import *
from falcon_lib import *
from WinGui_PySide import Ui_MainWindow
from PySide import QtCore, QtGui

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,lib,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.lib=lib
        self.channelMap[][4]={{self.QSFP1_AR1_LS_label,self.QSFP1_AR1_EM_label,self.QSFP1_AR1_BR_label,self.QSFP1_AR1_PF_label}
        ,{self.QSFP1_AR1_EM_lab
self.QSFP1_AR1_BR_lab
self.QSFP1_AR1_PF_lab
self.QSFP1_AR2_LS_lab
self.QSFP1_AR2_PF_lab
self.QSFP1_AR2_EM_lab
self.QSFP1_AR2_BR_lab
self.QSFP1_AR3_LS_lab
self.QSFP1_AR3_PF_lab
self.QSFP1_AR3_EM_lab
self.QSFP1_AR3_BR_lab
self.QSFP1_AR4_LS_lab
self.QSFP1_AR4_PF_lab
self.QSFP1_AR4_EM_lab
self.QSFP1_AR4_BR_lab
                     
self.QSFP2_AR1_LS_lab
self.QSFP2_AR1_EM_lab
self.QSFP2_AR1_BR_lab
self.QSFP2_AR1_PF_lab
self.QSFP2_AR2_LS_lab
self.QSFP2_AR2_PF_lab
self.QSFP2_AR2_EM_lab
self.QSFP2_AR2_BR_lab
self.QSFP2_AR3_LS_lab
self.QSFP2_AR3_PF_lab
self.QSFP2_AR3_EM_lab
self.QSFP2_AR3_BR_lab
self.QSFP2_AR4_LS_lab
self.QSFP2_AR4_PF_lab
self.QSFP2_AR4_EM_lab
self.QSFP2_AR4_BR_lab
                     
self.SFP1_AR_BR_label
self.SFP1_AR_EM_label
self.SFP1_AR_PF_label
self.SFP1_AR_LS_label
self.SFP2_AR_BR_label
self.SFP2_AR_EM_label
self.SFP2_AR_PF_label
self.SFP2_AR_LS_label
self.SFP3_AR_BR_label
self.SFP3_AR_EM_label
self.SFP3_AR_PF_label
self.SFP3_AR_LS_label
self.SFP4_AR_BR_label
self.SFP4_AR_EM_label
self.SFP4_AR_PF_label
self.SFP4_AR_LS_label
}




                         }

    def refresh_GUI(self):
        self.array.setText(QtGui.QApplication.translate("MainWindow", "111111", None, QtGui.QApplication.UnicodeUTF8))
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

        self.SFP1_AR_BR_label.setText(QtGui.QApplication.translate("MainWindow", "666666", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP1_AR_EM_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP1_AR_PF_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP1_AR_LS_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP2_AR_BR_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP2_AR_EM_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP2_AR_PF_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP2_AR_LS_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP3_AR_BR_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP3_AR_EM_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP3_AR_PF_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP3_AR_LS_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP4_AR_BR_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP4_AR_EM_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP4_AR_PF_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.SFP4_AR_LS_label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        '''
        for i in range(1,17):
            if self.link_stat(i) == 1:
                link[i - 1].config(text='ON', bg='green')
                if self.ber(i) <= 1e-13:
                    fail[i - 1].config(text='PASS', bg='green')
                else:
                    fail[i - 1].config(text='FAIL', bg='red')
            else:
                link[i - 1].config(text='OFF', bg='red')
                fail[i - 1].config(text='FAIL', bg='red')

            text='%.3f' % self.eye_marg(i)
            text='%.2E' % self.ber(i)
            
            if self.link_stat(1) == 1:
                self.QSFP1_AR1_LS_label.setStyleSheet("background-color: rgb(255, 255, 0);")
        '''
    def testGPIO(self):
        adr=0
        a=self.lib.MdioRd(0)
        print "addr %x's value0x%x" %(adr,a)

    def connect(self):
        self.lib.connect()

    def link_stat(self, m):
        return int(self.lib.Falcon_Link_Status_B(m))

    def eye_marg(self, m):
        eye = float(self.lib.Falcon_Read_Eyemargin_B(m))
        return eye

    def ber(self, m):
        return self.lib.RxReadPRBSCounterB(m) / float((40 * 50 * 10 ** 9))

    def load_window(self):
        new = Toplevel(self.master)
        what = Fetch(new)