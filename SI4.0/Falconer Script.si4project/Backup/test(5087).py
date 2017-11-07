from Tkinter import *
import threading
import time

def func():
    print 'hello timer!'
    timer = threading.Timer(1, func)
    timer.start()

#master=Tk()
timer = threading.Timer(1, func)
timer.start()
#while True:
#    time.sleep(0.5)
#    print 'main running'
#group=LabelFrame(master,text="Group",padx=5,pady=5)
#group.pack(padx=10,pady=10)
#w=Label(group, text='BER')
#w=Entry(group)
#w.pack()

#mainloop()


