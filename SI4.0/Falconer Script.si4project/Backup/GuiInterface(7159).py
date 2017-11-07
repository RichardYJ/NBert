import sys
from PySide.QtGui import *
from falcon_lib import *
from WinGui_PySide import Ui_MainWindow
from PySide import QtCore, QtGui
channelMap={0}
class MainWindow(QMainWindow,Ui_MainWindow):
    
    setText1=1
    setText2=2
    setText3=3
    setText4=4
    setText5=5
    setText6=6
    setText7=7
    setText8=8
    setText9=9
    setText10=10
    setText11=11
    setText12=12
    setText13=13
    setText14=14
    setText15=15
    setText16=16
                
    setText17=17
    setText18=18
    setText19=19
    setText20=20
    setText21=21
    setText22=22
    setText23=23
    setText24=24
    setText25=25
    setText26=26
    setText27=27
    setText28=28
    setText29=29
    setText30=30
    setText31=31
    setText32=32
                               
    setText33=33  
    setText34=34  
    setText35=35  
    setText36=36  
    setText37=37  
    setText38=38  
    setText39=39  
    setText40=40  
    setText41=41  
    setText42=42  
    setText43=43  
    setText44=44  
    setText45=45  
    setText46=46  
    setText47=47  
    setText48=48  






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
           "1":self.QSFP1_AR1_LS_label.setText,
           "2":self.QSFP1_AR1_EM_label.setText,
           "3":self.QSFP1_AR1_BR_label.setText,
           "4":self.QSFP1_AR1_PF_label.setText,
           "5":self.QSFP1_AR2_LS_label.setText,
           "6":self.QSFP1_AR2_EM_label.setText,
           "7":self.QSFP1_AR2_BR_label.setText,
           "8":self.QSFP1_AR2_PF_label.setText,
           "9":self.QSFP1_AR3_LS_label.setText,
           "10":self.QSFP1_AR3_EM_label.setText,
           "11":self.QSFP1_AR3_BR_label.setText,
           "12":self.QSFP1_AR3_PF_label.setText,
           "13":self.QSFP1_AR4_LS_label.setText,
           "14":self.QSFP1_AR4_EM_label.setText,
           "15":self.QSFP1_AR4_BR_label.setText,
           "16":self.QSFP1_AR4_PF_label.setText,
              
           "17":self.QSFP2_AR1_LS_label.setText,
           "18":self.QSFP2_AR1_EM_label.setText,
           "19":self.QSFP2_AR1_BR_label.setText,
           "20":self.QSFP2_AR1_PF_label.setText,
           "21":self.QSFP2_AR2_LS_label.setText,
           "22":self.QSFP2_AR2_EM_label.setText,
           "23":self.QSFP2_AR2_BR_label.setText,
           "24":self.QSFP2_AR2_PF_label.setText,
           "25":self.QSFP2_AR3_LS_label.setText,
           "26":self.QSFP2_AR3_EM_label.setText,
           "27":self.QSFP2_AR3_BR_label.setText,
           "28":self.QSFP2_AR3_PF_label.setText,
           "29":self.QSFP2_AR4_LS_label.setText,
           "30":self.QSFP2_AR4_EM_label.setText,
           "31":self.QSFP2_AR4_BR_label.setText,
           "32":self.QSFP2_AR4_PF_label.setText,
             
           "33":self.SFP1_AR_LS_label.setText,
           "34":self.SFP1_AR_EM_label.setText,
           "35":self.SFP1_AR_BR_label.setText,
           "36":self.SFP1_AR_PF_label.setText,
           "37":self.SFP2_AR_LS_label.setText,
           "38":self.SFP2_AR_EM_label.setText,
           "39":self.SFP2_AR_BR_label.setText,
           "40":self.SFP2_AR_PF_label.setText,
           "41":self.SFP3_AR_LS_label.setText,
           "42":self.SFP3_AR_EM_label.setText,
           "43":self.SFP3_AR_BR_label.setText,
           "44":self.SFP3_AR_PF_label.setText,
           "45":self.SFP4_AR_LS_label.setText,
           "46":self.SFP4_AR_EM_label.setText,
           "47":self.SFP4_AR_BR_label.setText,
           "48":self.SFP4_AR_PF_label.setText
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

        for i in range(1,49):
            t = str(1)
            self.EventMethods[t](QtGui.QApplication.translate("MainWindow", "000000", None, QtGui.QApplication.UnicodeUTF8))

            #            for j in range(0,4):
            #t = "1"
            # str(1)

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
