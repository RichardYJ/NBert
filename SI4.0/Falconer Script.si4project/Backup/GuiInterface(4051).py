import sys
from PySide.QtGui import *
from falcon_lib import *
from WinGui_PySide import Ui_MainWindow
from PySide import QtCore, QtGui
import threading

class MainWindow(QMainWindow,Ui_MainWindow):
    
    def __init__(self,lib,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.lib=lib
        self.initEventMethods()
        ######yj test
        self.testGPIO()
        self.refresh_GUI()
        self.timer = QtCore.QBasicTimer()
        self.func()
        # master=Tk()
#        timer = threading.Timer(1, self.func)
#        timer.start()
        ######  

    def initEventMethods(self):
        self.channelMapList=(
         (
         self.QSFP1_AR1_LS_label
        ,self.QSFP1_AR1_EM_label
        ,self.QSFP1_AR1_BR_label
        ,self.QSFP1_AR1_PF_label
        )
        ,(
         self.QSFP1_AR2_LS_label
        ,self.QSFP1_AR2_EM_label
        ,self.QSFP1_AR2_BR_label
        ,self.QSFP1_AR2_PF_label
        )
        ,(
         self.QSFP1_AR3_LS_label
        ,self.QSFP1_AR3_EM_label
        ,self.QSFP1_AR3_BR_label
        ,self.QSFP1_AR3_PF_label
        )
        ,(
         self.QSFP1_AR4_LS_label
        ,self.QSFP1_AR4_EM_label
        ,self.QSFP1_AR4_BR_label
        ,self.QSFP1_AR4_PF_label
        )
        ,(
         self.QSFP2_AR1_LS_label
        ,self.QSFP2_AR1_EM_label
        ,self.QSFP2_AR1_BR_label
        ,self.QSFP2_AR1_PF_label
        )
        ,(
         self.QSFP2_AR2_LS_label
        ,self.QSFP2_AR2_EM_label
        ,self.QSFP2_AR2_BR_label
        ,self.QSFP2_AR2_PF_label
        )                 
        ,(                
         self.QSFP2_AR3_LS_label
        ,self.QSFP2_AR3_EM_label
        ,self.QSFP2_AR3_BR_label
        ,self.QSFP2_AR3_PF_label
        )                 
        ,(                
         self.QSFP2_AR4_LS_label
        ,self.QSFP2_AR4_EM_label
        ,self.QSFP2_AR4_BR_label
        ,self.QSFP2_AR4_PF_label
        )                     
        ,(
         self.SFP1_AR_LS_label
        ,self.SFP1_AR_EM_label
        ,self.SFP1_AR_BR_label
        ,self.SFP1_AR_PF_label
        )               
        ,(              
         self.SFP2_AR_LS_label
        ,self.SFP2_AR_EM_label
        ,self.SFP2_AR_BR_label
        ,self.SFP2_AR_PF_label
        )               
        ,(              
         self.SFP3_AR_LS_label
        ,self.SFP3_AR_EM_label
        ,self.SFP3_AR_BR_label
        ,self.SFP3_AR_PF_label
        )               
        ,(              
         self.SFP4_AR_LS_label
        ,self.SFP4_AR_EM_label
        ,self.SFP4_AR_BR_label
        ,self.SFP4_AR_PF_label
        )
        )
        
        self.EventMethods = {
           "1":self.QSFP1_AR1_LS_label.setText,
           "72":self.SFP4_AR_PF_label.setStyleSheet,                	
        }
#        t = str((i-1)*4+1)
#        self.EventMethods[t](QtGui.QApplication.translate("MainWindow", "ON", None, QtGui.QApplication.UnicodeUTF8))
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL("clicked()"),self.prbs_reset)


    def timerEvent(self, e):
        if self.stop == 1:
            self.timer.stop()
            return
        self.refresh_GUI2()

    '''
    def paintEvent(self,e):
        print 'refresh'
        self.refresh_GUI2()
    '''

    def refresh_GUI(self):
        #for j in range(1,4):
        for i in range(1,13):
            j=i-1
            if self.link_stat(i) == 1:
                #link[i - 1].config(text='ON', bg='green')
                self.channelMapList[j][0].setText(QtGui.QApplication.translate("MainWindow", "ON", None, QtGui.QApplication.UnicodeUTF8))
                self.channelMapList[j][0].setStyleSheet("background-color: rgb(0, 255, 0);")
                if self.ber(i) <= 1e-13:
                    #fail[i - 1].config(text='PASS', bg='green')
                    self.channelMapList[j][3].setText(QtGui.QApplication.translate("MainWindow", "PASS", None, QtGui.QApplication.UnicodeUTF8))
                    self.channelMapList[j][3].setStyleSheet("background-color: rgb(0, 255, 0);")
                else:
                    #fail[i - 1].config(text='FAIL', bg='red')
                    self.channelMapList[j][3].setText(QtGui.QApplication.translate("MainWindow", "FAIL", None, QtGui.QApplication.UnicodeUTF8))
                    self.channelMapList[j][3].setStyleSheet("background-color: rgb(255, 0, 0);")
            else:
#                link[i - 1].config(text='OFF', bg='red')
#                fail[i - 1].config(text='FAIL', bg='red')
                self.channelMapList[j][0].setText(QtGui.QApplication.translate("MainWindow", "OFF", None, QtGui.QApplication.UnicodeUTF8))
                self.channelMapList[j][0].setStyleSheet("background-color: rgb(255, 0, 0);")
                self.channelMapList[j][3].setText(QtGui.QApplication.translate("MainWindow", "FAIL", None, QtGui.QApplication.UnicodeUTF8))
                self.channelMapList[j][3].setStyleSheet("background-color: rgb(255, 0, 0);")
            self.channelMapList[j][1].setText(QtGui.QApplication.translate("MainWindow", '%.3f' % self.eye_marg(i), None, QtGui.QApplication.UnicodeUTF8))
            self.channelMapList[j][2].setText(QtGui.QApplication.translate("MainWindow", '%.2E' % self.ber(i), None, QtGui.QApplication.UnicodeUTF8))


    def func(self):
        self.refresh_GUI2()
        print 'hello timer!'
        timer = threading.Timer(1, self.func)
        timer.start()

    def refresh_GUI2(self):
        self.channelMapList[0][0].setText(QtGui.QApplication.translate("MainWindow", "xxxxxxxxxxxxxxxxx", None, QtGui.QApplication.UnicodeUTF8))
#        self.refresh_GUI()
#        timer = threading.Timer(20, self.refresh_GUI2())
#        timer.start()


    def testGPIO(self):
        adr=0
        a=self.lib.MdioRd(0)
        print "addr %x's value0x%x" %(adr,a)

    def prbs_reset(self):
        for i in range(16):
            self.lib.Falcon_Reset_PRBS_Cntr_B(i + 1)
        self.count = 0

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

'''
def func():
    print 'hello timer!'
    timer = threading.Timer(1, func)
    timer.start()
'''
