import sys
from PySide.QtGui import *

from WinGui_PySide import Ui_MainWindow

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)








if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()#MyApp()
    window.show()
    sys.exit(app.exec_())
