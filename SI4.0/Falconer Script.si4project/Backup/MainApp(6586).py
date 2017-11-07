import sys
from PySide.QtGui import *
from falcon_lib import *
from WinGui_PySide import Ui_MainWindow
from GuiInterface import *
import time
from falcon import *

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

    lib.cr_write_i2c_AC_8(0x19,0xff, 0x20)
    ioDir=lib.cr_read_i2c_AC_8(0x10,0x20)    
    ioData=lib.cr_read_i2c_AC_8(0x19,0x20)
    window = MainWindow(lib)
    window.show()
    sys.exit(app.exec_())