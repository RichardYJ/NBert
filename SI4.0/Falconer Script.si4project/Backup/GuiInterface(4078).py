import sys
from PySide.QtGui import *
from falcon_lib import *
from WinGui_PySide import Ui_MainWindow

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)


    def refresh_GUI(self):
    


