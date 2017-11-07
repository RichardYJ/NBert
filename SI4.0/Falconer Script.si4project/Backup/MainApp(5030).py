import sys
from PySide.QtGui import *

from WinGui_PySide import Ui_MainWindow
from GuiInterface import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()#MyApp()
    window.refresh_GUI()
    window.show()
    sys.exit(app.exec_())
