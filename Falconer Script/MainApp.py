# -*- coding: utf-8 -*-
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
#############################################################    LIB  content
    iled = 0
    lib.cr_write_i2c_AC_8(0x1, 0x00, 0x20)
    lib.cr_write_i2c_AC_8(0x13, iled, 0x20)
    for i in range(0,0x6):
        j=0x01<<i
        ioDir=lib.cr_read_i2c_AC_8(j,0x70)           #config I2C channel
        lib.cr_write_i2c_AC_8(0x4A, 0x00, 0x50)
        lib.cr_write_i2c_AC_8(0x4B, 0x00, 0x50)
        lib.cr_write_i2c_AC_8(0x4E, 0x01, 0x50)
        ioDataH=lib.cr_read_i2c_AC_8(0x4C,0x50)
        ioDataL=lib.cr_read_i2c_AC_8(0x4D,0x50)
        ioData = ioDataH<<8|ioDataL
        if 0x204C==ioData:
            iled |= j
            lib.cr_write_i2c_AC_8(0x13,iled, 0x20)
##################################################################


    '''
    lib.cr_write_i2c_AC_8(0x4A,0x00, 0x50)
    lib.cr_write_i2c_AC_8(0x4B,0x00, 0x50)
    lib.cr_write_i2c_AC_8(0x4E,0x01, 0x50)
    '''
#    ioDataH=lib.cr_read_i2c_AC_8(0x4C,0x50)
#    ioDataL=lib.cr_read_i2c_AC_8(0x4D,0x50)
#    for i in range(0,0x1b):
    '''
    while 1:
        ioDataH = lib.cr_read_i2c_AC_8(0,0x50)
        print '0x%x'%ioDataH
    '''


    ioData=lib.cr_read_i2c_AC_8(0x13,0x20)
    window = MainWindow(lib)
    window.show()
    sys.exit(app.exec_())
