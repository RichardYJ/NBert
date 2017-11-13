from Tkinter import *
import threading
import time
from CredoUsbDongle import *
import sys
from PySide.QtGui import *
from falcon_lib import *
from WinGui_PySide import Ui_MainWindow
from GuiInterface import *
import time
from falcon import *
from ctypes import *

def func():
    print 'hello timer!'
    timer = threading.Timer(1, func)
    timer.start()
    

#master=Tk()
#timer = threading.Timer(1, func)
#timer.start()
#while True:
#    time.sleep(0.5)
#    print 'main running'
#group=LabelFrame(master,text="Group",padx=5,pady=5)
#group.pack(padx=10,pady=10)
#w=Label(group, text='BER')
#w=Entry(group)
#w.pack()

'''
lib = Falcon_lib()
script = 'Falcon_CHRIS2.txt'
try:
    lib.connect()
except BaseException:
    print 'ErrorExit(app)'
else:
    adr=0
    a=lib.MdioRd(0)
    print "addr %x's value0x%x" %(adr,a)
'''
dll = cdll.LoadLibrary('lib.dll')
lib = Falcon_lib()
script = 'Falcon_CHRIS2.txt'
try:
    lib.connect()
except BaseException:
    print 'ErrorExit(app)'
'''
else:
    adr=0
    a=lib.MdioRd(0)
    print "addr %x's value0x%x" %(adr,a)

#    for i in range(0,0x1b):
lib.cr_write_i2c_AC_8(0x1,0x00, 0x20)
lib.cr_write_i2c_AC_8(0x13,0xff, 0x20)

lib.cr_write_i2c_AC_8(0x01,0x01, 0x70)
#    ioDir=lib.cr_read_i2c_AC_8(0xff,0x70)

lib.cr_write_i2c_AC_8(0x4A,0x00, 0x50)
lib.cr_write_i2c_AC_8(0x4B,0x00, 0x50)
lib.cr_write_i2c_AC_8(0x4E,0x01, 0x50)
'''


dll.test()
ioDataH=lib.cr_read_i2c_AC_8(0x0,0x50)
ioDataL=lib.cr_read_i2c_AC_8(0x0,0x50)
print '0x%x'%ioDataH
print '0x%x\n'%ioDataL
#while(1):
#    t=0

#mainloop()


