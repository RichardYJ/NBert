import sys
from PySide.QtGui import *
from falcon_lib import *
from WinGui_PySide import Ui_MainWindow
from GuiInterface import *
import time


class ErrorExit():
    def __init__(self, app):
        dialog = DialogError()
        dialog.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    lib = Falcon_lib()
    script = 'Falcon_CHRIS2.txt'
    app = QApplication(sys.argv)
    try:
        lib.connect()
    except BaseException:
        ErrorExit(app)
    else:
        lib.Falcon_Software_Reset()
        time.sleep(0.5)
        lib.LoadScript(script)
        time.sleep(0.5)
        lib.Falcon_Logic_Reset()
    window = MainWindow(lib)
    window.show()
    sys.exit(app.exec_())