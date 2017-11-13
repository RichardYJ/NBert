import sys
from PySide.QtGui import *
from falcon_lib import *
from WinGui_PySide import Ui_MainWindow
from DialogError import Ui_DialogError
from DialogLoadScript import Ui_DialogLoadScript
from PySide import QtCore, QtGui
from tkFileDialog import askopenfilename
from ctypes import *

class MainWindow(QMainWindow,Ui_MainWindow):
    
    def __init__(self,lib,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.lib=lib
        self.dll = cdll.LoadLibrary('lib_nothrd.dll')    #####################################
        self.count = 0
        self.stop = 0
        self.rst = 0
        self.initEventMethods()
#        self.testGPIO()     ######yj test
        self.refresh_GUI()
        self.timer = QtCore.QBasicTimer()
        self.timer.start(1000,self)
        QtCore.QObject.connect(self.actionLoad, QtCore.SIGNAL("triggered()"), self.load_window)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), self.the_end)


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
#        t = str((i-1)*4+1)     #do not delete
#        self.EventMethods[t](QtGui.QApplication.translate("MainWindow", "ON", None, QtGui.QApplication.UnicodeUTF8))       #do not delete
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL("clicked()"),self.prbs_reset)



    def timerEvent(self, e):
        if self.stop == 1:
            self.timer.stop()
            return
        self.dll.test()        #####################################
        self.rst += 1
#        if self.rst>=5:
        self.refresh_GUI()
        self.rst = 0
#        print 'timer'


    def refresh_GUI(self):
        self.count += 1
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", 'Test Time: %d' % self.count, None, QtGui.QApplication.UnicodeUTF8))
        for k in range(1,13):
            j=k-1
            i=self.calc(k,13)+4
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

    def calc(self,i,j):
        return j-i


    def refresh_GUI2(self):
        self.channelMapList[0][0].setText(QtGui.QApplication.translate("MainWindow", "xxxxxxxxxxxxxxxxx", None, QtGui.QApplication.UnicodeUTF8))



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
        self.dialog = DialogLoadScript(self.lib)
        self.dialog.show()
#        sys.exit(app.exec_())
        print 'Load'

    def the_end(self):
        QtCore.QCoreApplication.instance().quit()


class DialogError(QDialog, Ui_DialogError):
    def __init__(self, parent=None):
        super(DialogError, self).__init__(parent)
        self.setupUi(self)

class DialogLoadScript(QDialog, Ui_DialogLoadScript):
    def __init__(self, lib,parent=None):
        super(DialogLoadScript, self).__init__(parent)
        self.lib=lib
        self.setupUi(self)
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL("clicked()"),self.load_script)
        self.label_2.setText(QtGui.QApplication.translate("DialogLoadScript", "Falcon_CHRIS2.txt", None,
                                                      QtGui.QApplication.UnicodeUTF8))


    def load_script(self):
        filename = QFileDialog.getOpenFileName(self,"Open File")
        words = filename[0].split("/")
        if filename != '':
            self.label_2.setText(QtGui.QApplication.translate("DialogLoadScript",unicode.encode(words[-1]) , None, QtGui.QApplication.UnicodeUTF8))#(text=words.pop(-1))  words[0]
            self.lib.LoadScript(filename[0])
