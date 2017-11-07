#######By Marc Xu
import Tkinter as tk
from Tkinter import *
import time, sys
from tkFileDialog import askopenfilename
from falcon_lib import Falcon_lib


class FalconGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Credo QSFP-SFP Tester")
        self.api = Falcon_lib()

        self.mainFrm = Frame(self.master)
        self.mainFrm.grid(row=0,column=0)
        self.monitor_1 = Label(self.mainFrm, text='RX Monitor 1')
        self.monitor_1.bind("<Button-3>", self.print_click)
        self.monitor_1.pack(ipady=5)
        self.subFrm1 = LabelFrame(self.mainFrm, text="sub1", padx=5, pady=5)
        self.subFrm1.pack(fill='both', padx=10)

        self.link_status = Label(self.subFrm1, text='Link Status')
        self.link_status.grid(row=1, sticky='W', padx=10)
        self.eye = Label(self.subFrm1, text='Eye Margin')
        self.eye.grid(row=3, sticky='W', padx=10)
        self.BER = Label(self.subFrm1, text='BER')
        self.BER.grid(row=4, sticky='W', padx=10)
        self.passfail = Label(self.subFrm1, text='Pass/Fail')
        self.passfail.grid(row=5, sticky='W', padx=10)

#        group = LabelFrame(master, text="Group", padx=5, pady=5)
#        group.grid(row=2, column=0)
#        group.pack(padx=10, pady=10)


        self.monitor_2 = Label(self.mainFrm, text='RX Monitor 2')
        self.monitor_2.pack(pady=10)
        self.subFrm2 = LabelFrame(self.mainFrm, text="sub2", padx=5, pady=5)
        self.subFrm2.pack(fill='both', padx=10)#grid(row=0,column=1)

        self.link_status = Label(self.subFrm2, text='Link Status')
        self.link_status.grid(row=1, sticky='W', padx=10)
        self.eye = Label(self.subFrm2, text='Eye Margin')
        self.eye.grid(row=3, sticky='W', padx=10)
        self.BER = Label(self.subFrm2, text='BER')
        self.BER.grid(row=4, sticky='W', padx=10)
        self.passfail = Label(self.subFrm2, text='Pass/Fail')
        self.passfail.grid(row=5, sticky='W', padx=10)
        self.count = 0


        self.all_button = Button(self.mainFrm, text='Reset All',
                                 command=self.prbs_reset)
        self.all_button.pack(pady=10)

        self.all_button1 = Button(self.mainFrm, text='Reset All  1',
                                 command=self.testGPIO)
        self.all_button1.pack(pady=11)

        self.main_menu = Menu(self.master)
        self.master.config(menu=self.main_menu)
        self.option_menu = Menu(self.main_menu, tearoff=0)
        self.option_menu.add_command(label='Load Alternate Script',
                                     command=self.load_window)
        self.option_menu.add_separator()
        self.option_menu.add_command(label='Exit', command=the_end)
        self.main_menu.add_cascade(label='Options', menu=self.option_menu)

        self.table()
        self.display()

    def print_click(self):
        print 'You right clicked!'

    def prbs_reset(self):
        for i in range(16):
            self.api.Falcon_Reset_PRBS_Cntr_B(i + 1)
        self.count = 0

    def table(self):
        eye = []
        ber = []
        ar = []
        br = []

        for i in range(1, 9):
            eye.append('eye_%d' % i)
            ber.append('ber_%d' % i)
            ar.append('AR%d' % i)

            ar[i - 1] = Label(self.subFrm1, text='AR%d' % i, bg='grey')
            eye[i - 1] = Label(self.subFrm1, bg='white')
            ber[i - 1] = Label(self.subFrm1, bg='white')

            ar[i - 1].grid(row=0, column=i, sticky='S', ipadx=41, pady=1)
            eye[i - 1].grid(row=3, column=i, ipadx=52, ipady=5)
            ber[i - 1].grid(row=4, column=i, ipadx=52, ipady=5)

        for i in range(1, 9):
            v = i + 8
            eye.append('eye_%d' % i)
            ber.append('ber_%d' % i)
            br.append('BR%d' % i)

            br[i - 1] = Label(self.subFrm2, text='BR%d' % i, bg='grey')
            eye[v - 1] = Label(self.subFrm2, bg='white')
            ber[v - 1] = Label(self.subFrm2, bg='white')

            br[i - 1].grid(row=0, column=i, ipadx=41, pady=1)
            eye[v - 1].grid(row=3, column=i, ipadx=52, ipady=5)
            ber[v - 1].grid(row=4, column=i, ipadx=52, ipady=5)

    def data(self):

        link = []
        eye = []
        ber = []
        fail = []

        self.count += 1
        timer = Label(self.master, text='Test Time: %d' % self.count)
        timer.grid(row=1, pady=10, ipadx=7)

        for i in range(1, 9):
            link.append('link_%d' % i)
            eye.append('eye_%d' % i)
            ber.append('ber_%d' % i)
            fail.append('fail_%d' % i)

            link[i - 1] = Label(self.subFrm2, width=3, height=1)
            fail[i - 1] = Label(self.subFrm2, width=3, height=1, relief='solid', bd=1)
            
            if self.link_stat(i) == 1:
                link[i - 1].config(text='ON', bg='green')
                if self.ber(i) <= 1e-13:
                    fail[i - 1].config(text='PASS', bg='green')
                else:
                    fail[i - 1].config(text='FAIL', bg='red')
            else:
                link[i - 1].config(text='OFF', bg='red')
                fail[i - 1].config(text='FAIL', bg='red')
            eye[i - 1] = Label(self.subFrm2, text='%.3f' % self.eye_marg(i),
                               bg='white', width=3, height=1)
            ber[i - 1] = Label(self.subFrm2, text='%.2E' % self.ber(i),
                               bg='white', width=3, height=1)
                               
            if (i<5):
                link[i - 1].grid(row=1, column=i+4, ipadx=41, ipady=5)
                eye[i - 1].grid(row=3, column=i+4, ipadx=14)
                ber[i - 1].grid(row=4, column=i+4, ipadx=14)
                fail[i - 1].grid(row=5, column=i+4, ipadx=40, ipady=5)
            else:
                link[i - 1].grid(row=1, column=i-4, ipadx=41, ipady=5)
                eye[i - 1].grid(row=3, column=i-4, ipadx=14)
                ber[i - 1].grid(row=4, column=i-4, ipadx=14)
                fail[i - 1].grid(row=5, column=i-4, ipadx=40, ipady=5)

            
        for i in range(1, 9):
            v = i + 8
            link.append('link_%d' % i)
            eye.append('eye_%d' % i)
            ber.append('ber_%d' % i)
            fail.append('fail_%d' % i)

            link[v - 1] = Label(self.subFrm1, width=3, height=1)
            fail[v - 1] = Label(self.subFrm1, width=3, height=1, relief='solid', bd=1)
            if self.link_stat(v) == 1:
                link[v - 1].config(text='ON', bg='green')
                if self.ber(v) <= 1e-13:
                    fail[v - 1].config(text='PASS', bg='green')
                else:
                    fail[v - 1].config(text='FAIL', bg='red')
            else:
                link[v - 1].config(text='OFF', bg='red')
                fail[v - 1].config(text='FAIL', bg='red')
            eye[v - 1] = Label(self.subFrm1, text='%.3f' % self.eye_marg(v),
                               bg='white', width=3, height=1)
            ber[v - 1] = Label(self.subFrm1, text='%.2E' % self.ber(v),
                               bg='white', width=3, height=1)
          
            if (i<5):
                link[v - 1].grid(row=1, column=i+4, ipadx=41, ipady=5)
                eye[v - 1].grid(row=3, column=i+4, ipadx=14)
                ber[v - 1].grid(row=4, column=i+4, ipadx=14)
                fail[v - 1].grid(row=5, column=i+4, ipadx=40, ipady=5)
            else:
                link[v - 1].grid(row=1, column=i-4, ipadx=41, ipady=5)
                eye[v - 1].grid(row=3, column=i-4, ipadx=14)
                ber[v - 1].grid(row=4, column=i-4, ipadx=14)
                fail[v - 1].grid(row=5, column=i-4, ipadx=40, ipady=5)
            '''
            link[v - 1].grid(row=1, column=i, ipadx=41, ipady=5)
            eye[v - 1].grid(row=3, column=i, ipadx=14)
            ber[v - 1].grid(row=4, column=i, ipadx=14)
            fail[v - 1].grid(row=5, column=i, ipadx=40, ipady=5)
            '''
    def display(self):
        self.data()
        self.master.after(1000, self.display)

    def testGPIO(self):
        adr=0
        a=self.api.MdioRd(0)
        print "addr %x's value0x%x" %(adr,a)

    def connect(self):
        self.api.connect()

    def link_stat(self, m):
        return int(self.api.Falcon_Link_Status_B(m))

    def eye_marg(self, m):
        eye = float(self.api.Falcon_Read_Eyemargin_B(m))
        return eye

    def ber(self, m):
        return self.api.RxReadPRBSCounterB(m) / float((40 * 50 * 10 ** 9))

    def load_window(self):
        new = Toplevel(self.master)
        what = Fetch(new)


class Error:
    def __init__(self, master):
        self.master = master
        self.master.title('ERROR')

        self.frame = Frame(master)
        self.frame.pack(ipadx=40, ipady=10)
        self.exit_button = Button(self.frame, text='Exit', command=the_end)
        self.exit_button.pack(side='bottom', ipadx=10, pady=10)
        self.message = Label(self.frame, text='Connection Failed ' +
                                              'Please Check Dongle Connection.')
        self.message.pack(side='bottom')


class Fetch:
    def __init__(self, master):
        self.master = master
        self.master.title('Load Alternate Script')

        self.frame = Frame(self.master)
        self.frame.pack(ipady=10, ipadx=10)
        self.label = Label(self.frame, text='Current Script:')
        self.label.grid(row=0, sticky='W', pady=10, padx=20)
        self.new_script = Label(self.frame, text=script, bg='white', relief='sunken', bd=3)
        self.new_script.grid(row=1, padx=20, ipadx=5, ipady=2)
        self.change_button = Button(self.frame, text='Load Script',
                                    command=self.load_script)
        self.change_button.grid(row=1, column=1, padx=10)

    def load_script(self):
        filename = askopenfilename()
        words = filename.split("/")
        if filename != '':
            self.new_script.config(text=words.pop(-1))
            test.LoadScript(filename)


def the_end():
    root.quit()
    root.destroy()

    sys.exit()


if __name__ == "__main__":
    global script
    root = tk.Tk()
    test = Falcon_lib()
    script = 'Falcon_CHRIS2.txt'

    try:
        test.connect()
    except BaseException:
        Error(root)
    else:
        test.Falcon_Software_Reset()
        time.sleep(0.5)
        test.LoadScript(script)
        time.sleep(0.5)
        test.Falcon_Logic_Reset()
        FalconGUI(root)

    root.protocol("WM_DELETE_WINDOW", the_end)
    root.mainloop()
