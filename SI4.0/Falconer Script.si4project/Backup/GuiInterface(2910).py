import sys
from PySide.QtGui import *
from falcon_lib import *
from WinGui_PySide import Ui_MainWindow
from PySide import QtCore, QtGui
channelMap={0}
class MainWindow(QMainWindow,Ui_MainWindow):
    
    self.setText1=1
    self.setText2=2
    self.setText3=3
    self.setText4=4
    self.setText5=5
    self.setText6=6
    self.setText7=7
    self.setText8=8
    self.setText9=9
    self.setText10=10
    self.setText11=11
    self.setText12=12
    self.setText13=13
    self.setText14=14
    self.setText15=15
    self.setText16=16
                     
    self.setText17=17
    self.setText18=18
    self.setText19=19
    self.setText20=20
    self.setText21=21
    self.setText22=22
    self.setText23=23
    self.setText24=24
    self.setText25=25
    self.setText26=26
    self.setText27=27
    self.setText28=28
    self.setText29=29
    self.setText30=30
    self.setText31=31
    self.setText32=32
                                    
    self.setText33=33  
    self.setText34=34  
    self.setText35=35  
    self.setText36=36  
    self.setText37=37  
    self.setText38=38  
    self.setText39=39  
    self.setText40=40  
    self.setText41=41  
    self.setText42=42  
    self.setText43=43  
    self.setText44=44  
    self.setText45=45  
    self.setText46=46  
    self.setText47=47  
    self.setText48=48  






    def __init__(self,lib,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.lib=lib
        self.initEventMethods()
        #self.
        #self.channelMap={self.QSFP1_AR1_LS_label,self.QSFP1_AR1_EM_label}
        '''
        self.channelMap[100]={#[15][4]={
         {
         self.QSFP1_AR1_LS_label.setText
        ,self.QSFP1_AR1_EM_label
        ,self.QSFP1_AR1_BR_label
        ,self.QSFP1_AR1_PF_label
        }
        ,{
         self.QSFP1_AR2_LS_label
        ,self.QSFP1_AR2_EM_label
        ,self.QSFP1_AR2_BR_label
        ,self.QSFP1_AR2_PF_label
        }
        ,{
         self.QSFP1_AR3_LS_label
        ,self.QSFP1_AR3_PF_label
        ,self.QSFP1_AR3_EM_label
        ,self.QSFP1_AR3_BR_label
        }
        ,{
         self.QSFP1_AR4_LS_label
        ,self.QSFP1_AR4_PF_label
        ,self.QSFP1_AR4_EM_label
        ,self.QSFP1_AR4_BR_label
        }
        ,{
         self.QSFP2_AR1_LS_label
        ,self.QSFP2_AR1_EM_label
        ,self.QSFP2_AR1_BR_label
        ,self.QSFP2_AR1_PF_label
        }
        ,{
         self.QSFP2_AR2_LS_label
        ,self.QSFP2_AR2_PF_label
        ,self.QSFP2_AR2_EM_label
        ,self.QSFP2_AR2_BR_label
        }
        ,{
         self.QSFP2_AR3_LS_label
        ,self.QSFP2_AR3_PF_label
        ,self.QSFP2_AR3_EM_label
        ,self.QSFP2_AR3_BR_label
        }
        ,{
         self.QSFP2_AR4_LS_label
        ,self.QSFP2_AR4_PF_label
        ,self.QSFP2_AR4_EM_label
        ,self.QSFP2_AR4_BR_label
        }                     
        ,{
         self.SFP1_AR_BR_label
        ,self.SFP1_AR_EM_label
        ,self.SFP1_AR_PF_label
        ,self.SFP1_AR_LS_label
        }
        ,{
         self.SFP2_AR_BR_label
        ,self.SFP2_AR_EM_label
        ,self.SFP2_AR_PF_label
        ,self.SFP2_AR_LS_label
        }
        ,{
         self.SFP3_AR_BR_label
        ,self.SFP3_AR_EM_label
        ,self.SFP3_AR_PF_label
        ,self.SFP3_AR_LS_label
        }
        ,{
         self.SFP4_AR_BR_label
        ,self.SFP4_AR_EM_label
        ,self.SFP4_AR_PF_label
        ,self.SFP4_AR_PF_label#self.SFP4_AR_LS_label
        }
        }
'''

    def initEventMethods(self):
        self.EventMethods = {
           self.setText1:self.QSFP1_AR1_LS_label.setText,
           self.setText2:self.QSFP1_AR1_EM_label.setText,
           self.setText3:self.QSFP1_AR1_BR_label.setText,
           self.setText4:self.QSFP1_AR1_PF_label.setText,
           self.setText5:self.QSFP1_AR2_LS_label.setText,
           self.setText6:self.QSFP1_AR2_EM_label.setText,
           self.setText7:self.QSFP1_AR2_BR_label.setText,
           self.setText8:self.QSFP1_AR2_PF_label.setText,
           self.setText9:self.QSFP1_AR3_LS_label.setText,
           self.setText10:self.QSFP1_AR3_EM_label.setText,
           self.setText11:self.QSFP1_AR3_BR_label.setText,
           self.setText12:self.QSFP1_AR3_PF_label.setText,
           self.setText13:self.QSFP1_AR4_LS_label.setText,
           self.setText14:self.QSFP1_AR4_EM_label.setText,
           self.setText15:self.QSFP1_AR4_BR_label.setText,
           self.setText16:self.QSFP1_AR4_PF_label.setText,
                         
           self.setText17:self.QSFP2_AR1_LS_label.setText,
           self.setText18:self.QSFP2_AR1_EM_label.setText,
           self.setText19:self.QSFP2_AR1_BR_label.setText,
           self.setText20:self.QSFP2_AR1_PF_label.setText,
           self.setText21:self.QSFP2_AR2_LS_label.setText,
           self.setText22:self.QSFP2_AR2_EM_label.setText,
           self.setText23:self.QSFP2_AR2_BR_label.setText,
           self.setText24:self.QSFP2_AR2_PF_label.setText,
           self.setText25:self.QSFP2_AR3_LS_label.setText,
           self.setText26:self.QSFP2_AR3_EM_label.setText,
           self.setText27:self.QSFP2_AR3_BR_label.setText,
           self.setText28:self.QSFP2_AR3_PF_label.setText,
           self.setText29:self.QSFP2_AR4_LS_label.setText,
           self.setText30:self.QSFP2_AR4_EM_label.setText,
           self.setText31:self.QSFP2_AR4_BR_label.setText,
           self.setText32:self.QSFP2_AR4_PF_label.setText,
                         
           self.setText33:self.SFP1_AR_LS_label.setText,
           self.setText34:self.SFP1_AR_EM_label.setText,
           self.setText35:self.SFP1_AR_BR_label.setText,
           self.setText36:self.SFP1_AR_PF_label.setText,
           self.setText37:self.SFP2_AR_LS_label.setText,
           self.setText38:self.SFP2_AR_EM_label.setText,
           self.setText39:self.SFP2_AR_BR_label.setText,
           self.setText40:self.SFP2_AR_PF_label.setText,
           self.setText41:self.SFP3_AR_LS_label.setText,
           self.setText42:self.SFP3_AR_EM_label.setText,
           self.setText43:self.SFP3_AR_BR_label.setText,
           self.setText44:self.SFP3_AR_PF_label.setText,
           self.setText45:self.SFP4_AR_LS_label.setText,
           self.setText46:self.SFP4_AR_EM_label.setText,
           self.setText47:self.SFP4_AR_BR_label.setText,
           self.setText48:self.SFP4_AR_PF_label.setText
        }

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

        for i in range(0,2):
#            for j in range(0,4):
            tmp=self.channelMap[i]
            tmp.setText(QtGui.QApplication.translate("MainWindow", "000000", None, QtGui.QApplication.UnicodeUTF8))
        #[i]
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
