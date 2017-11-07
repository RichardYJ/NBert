import time, re, xlwt, os
#from power import E3646a
#from falcon_lib import Falcon_lib
from xlrd import open_workbook
from xlutils.copy import copy

class falcon_powercycletest:
    def __init__(self):
        self.api = Falcon_lib()
        #self.power = E3646a()
       
       
        self.borders = xlwt.Borders()
        self.borders.left = 1
        self.borders.right = 1
        self.borders.top = 1
        self.borders.bottom = 1
        self.alignment = xlwt.Alignment()
        self.alignment.horz = xlwt.Alignment.HORZ_CENTER
        self.alignment.vert = xlwt.Alignment.VERT_CENTER

        self.pattern = xlwt.Pattern()
        self.pattern.pattern = xlwt.Pattern.SOLID_PATTERN 
        self.pattern.pattern_fore_colour = 22
        self.style = xlwt.XFStyle()
        self.style.alignment = self.alignment
        self.style.borders = self.borders
        self.style.pattern = self.pattern

        self.pattern = xlwt.Pattern()
        self.pattern.pattern = xlwt.Pattern.SOLID_PATTERN 
        self.pattern.pattern_fore_colour = 2
        self.style_red = xlwt.XFStyle()
        self.style_red.alignment = self.alignment
        self.style_red.borders = self.borders
        self.style_red.pattern = self.pattern

        self.pattern = xlwt.Pattern()
        self.pattern.pattern = xlwt.Pattern.SOLID_PATTERN 
        self.pattern.pattern_fore_colour = 3
        self.style_green = xlwt.XFStyle()
        self.style_green.alignment = self.alignment
        self.style_green.borders = self.borders
        self.style_green.pattern = self.pattern
        

    def excelinit(self, filename = 'test'):
        self.excelo = xlwt.Workbook(encoding='ascii')
        self.sheet1o = self.excelo.add_sheet('Data',cell_overwrite_ok=True)
    
        for col in range(22):
            self.sheet1o.col(col).width = 256*9

        self.sheet1o.write_merge(0, 0, 1, 16, 'NRZ',self.style)
        self.sheet1o.write_merge(0, 0, 17, 24, 'Pam4',self.style)
       
        nrz_lane = ['A0R0','A0R1','A0R2','A0R3','A1R0','A1R1','A1R2','A1R3',
                    'A2R0','A2R1','A2R2','A2R3','A3R0','A3R1','A3R2','A3R3']
        pam4_lane = ['B0R0','B0R1','B1R0','B1R1','B2R0','B2R1','B3R0','B3R1']

        for i in range(16):
            self.sheet1o.write(1,i+1,nrz_lane[i],self.style)
        for i in range(8):
            self.sheet1o.write(1,i+17,pam4_lane[i],self.style)
        self.excelo.save('%s.xls'%filename)
        
    def writedata(self,rows,data = [],filename = 'test'):
        for i in data:
            print i
        link_status = data[0]
        prbs = data[1]
        eyemargin = data[2]
        tap_F1 = data[3]
        tap_F2 = data[4]
        tap_F3 = data[5]
        BER = data[6]
        print BER
        self.excel_org = open_workbook('%s.xls'%filename,formatting_info=True)
        self.excel = copy(self.excel_org)
        self.sheet1 = self.excel.get_sheet(0)
        test_time = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
       
        self.sheet1.write(rows+1,0,'%s'%(test_time),self.style)
        self.sheet1.write(rows+2,0,'link_s',self.style)
        self.sheet1.write(rows+3,0,'Prbs',self.style)
        self.sheet1.write(rows+4,0,'eyemargin',self.style)
        self.sheet1.write(rows+5,0,'tap_F1',self.style)
        self.sheet1.write(rows+6,0,'tap_F2',self.style)
        self.sheet1.write(rows+7,0,'tap_F3',self.style)
        self.sheet1.write(rows+8,0,'BER',self.style)
        

        for i in range(24):
            if link_status[i] == 1:
                 self.sheet1.write(rows+2,i+1,link_status[i],self.style_green)
                 self.sheet1.write(rows+3,i+1,prbs[i],self.style_green)
                 self.sheet1.write(rows+4,i+1,eyemargin[i],self.style_green)
                 self.sheet1.write(rows+5,i+1,tap_F1[i],self.style_green)
                 self.sheet1.write(rows+6,i+1,tap_F2[i],self.style_green)
                 self.sheet1.write(rows+7,i+1,tap_F3[i],self.style_green)
                 self.sheet1.write(rows+8,i+1,BER[i],self.style_green)
                 
            else:
                 self.sheet1.write(rows+2,i+1,link_status[i],self.style_red)
                 self.sheet1.write(rows+3,i+1,prbs[i],self.style_red)
                 self.sheet1.write(rows+4,i+1,eyemargin[i],self.style_red)
                 self.sheet1.write(rows+5,i+1,tap_F1[i],self.style_red)
                 self.sheet1.write(rows+6,i+1,tap_F2[i],self.style_red)
                 self.sheet1.write(rows+7,i+1,tap_F3[i],self.style_red)
                 self.sheet1.write(rows+8,i+1,BER[i],self.style_red)
        

        self.excel.save('%s.xls'%filename)


    def rdbybit(self, addr = 0x84ff, bit = [12,8]):
        value_all = self.api.MdioRd(addr)
        ref = 0
        for i in range(bit[0]-bit[-1]+1):
            ref = ref + pow(2,i)
        value = (value_all >> bit[-1]) & ref
        return value

    def Pam4_BER(self):
        base_pam4 = [0x1000,0x1100,0x1400,0x1500,0x1800,0x1900,0x1c00,0x1d00]
        Msb = []
        Lsb = []
        Msb_1 = 0
        Lsb_1 = 0
        Pam4_BER = []
        for base in range(len(base_pam4)):
            for i in range(0,24):
                if(i%2)==0:
                    Msb.append(self.rdbybit((base_pam4[base]+(0x52+i)),[15,0]))
                else:
                    Lsb.append(self.rdbybit((base_pam4[base]+(0x52+i)),[15,0]))
            for a in range(len(Msb)):
                Msb_1 = Msb_1 + Msb[a]
            for b in range(len(Lsb)):
                Lsb_1 = Lsb_1 + Lsb[b]
            BER = Msb_1*pow(2,16)+ Lsb_1
            print BER
            BER = float(BER)/(51*10^9)
            Pam4_BER.append(BER)
        return Pam4_BER
        
       
    def Nrz_BER(self):
        base_nrz = [0x2000,0x2100,0x2200,0x2300,0x2500,0x2600,0x2700,0x2800,
                     0x3000,0x3100,0x3200,0x3300,0x3500,0x3600,0x3700,0x3800]
        nrz_BER = []
        for b in range(len(base_nrz)):
            Msb = self.rdbybit((base_nrz[b]+ 0x4C),[15,0])
            Lsb = self.rdbybit((base_nrz[b]+ 0x4D),[15,0])
            BER = Msb*pow(2,16)+ Lsb
            print BER
            BER = float(BER)/(25*10^9)
            nrz_BER.append(BER)
        return nrz_BER
            
        
        
    def rows(self,filename = 'test'):
        self.excel_d = open_workbook('%s.xls'%filename)
        self.sheet = self.excel_d.sheets()[0]
        row_list = []
        rows_num = self.sheet.nrows
        return rows_num
    
    def setpower(self, site = 1, volt = 5, current = 2):
        self.power.sel_src(site)
        self.power.setting(volt,current)
        self.power.output(1)

    def chipstatus(self):
        link_status = []
        prbs = []
        eyemargin = []
        tap_F1 = []
        tap_F2 = []
        tap_F3 = []
        BER = []
        #Nrz_BER = self.Nrz_BER()
        #print Nrz_BER
        #Pam4_BER = self.Pam4_BER()
        #print Pam4_BER
        #BER = Nrz_BER.extend( Pam4_BER)       
        
        
        for i in range(16):
            link_status.append(int(self.api.Falcon_Link_Status_B(i+1)))
            prbs.append(int(self.api.RxReadPRBSCounterB(i+1)))
            eyemargin.append(int(self.api.Falcon_Read_Eyemargin_B(i+1)))
            tap_F1.append(self.api.Falcon_Read_F1(i+1))
            tap_F2.append(self.api.Falcon_Read_F2(i+1))
            tap_F3.append(self.api.Falcon_Read_F3(i+1))
            BER.append(self.api.RxReadPRBSCounterB(i+1)/(40*25*10**9))
        for i in range(8):
            link_status.append(int(self.api.Falcon_Link_Status(i+1)))
            prbs.append(int(self.api.RxReadPRBSCounter(i+1)))
            eyemargin.append(int(self.api.Falcon_Read_Eyemargin(i+1)))
            tap_F1.append(int(self.api.Falcon_Read_margin0(i+1)))
            tap_F2.append(int(self.api.Falcon_Read_margin1(i+1)))
            tap_F3.append(int(self.api.Falcon_Read_margin2(i+1)))
            BER.append(self.api.RxReadPRBSCounter(i+1)/(40*50*10**9))
       
        
        #print link_s
        #print prbs_s
        #print eyemargin_s
        #print [link_status,prbs,eyemargin,tap_F1,tap_F2, tap_F3]
        return [link_status,prbs,eyemargin,tap_F1,tap_F2, tap_F3, BER]
    
    def testonce(self,filename = 'test',script = '123',time = 1):       
        print 'init...'
        #self.power.output(0) #############################################POWER
        time.sleep(3)
        #self.setpower(1,5,3) #############################################POWER
        time.sleep(1)
        try:
            self.api.connect()
        except BaseException:
            print 'MDIO disconnect!!'
            data = []
        else:
            #print 'init chip...'
            self.api.Falcon_Software_Reset()
            time.sleep(0.5)
            self.api.LoadScript(script)
            time.sleep(0.5)
            self.api.Falcon_Logic_Reset()  
            time.sleep(0.5)
            tmp = self.api.MdioRd(0x0000)
            if tmp != 0x204c:
                data = []
            else:
                time.sleep(1)

                for i in range(16):
                    self.api.Falcon_Reset_PRBS_Cntr_B(i+1)
                for i in range(8):
                    self.api.Falcon_Reset_PRBS_Cntr(i+1)

                time.sleep(40)

                data = self.chipstatus()
            time.sleep(0.5)
            self.api.disconnect()
        return data

    def autotest(self,filename = 'test',script = 'xx.txt',times = 5):
        if os.path.exists(r'E:\Falcon\Falcon SLT\Falcon GUI\Falcon_PowerCycleTest_V1.0\test.xls')== False:
            self.excelinit(filename)
        #self.power.opensource(0,7) ########################################################POWER
        print 'Start test %d times...'%times
        
        for i in range(times):
            rows = self.rows(filename)
            data = self.testonce(filename,script,time)
            if data == []:
                print 'Test (%d/%d) Error~!!!\n'%(i+1,times)
            else:
                prbs = data[1]
                x = 0
                for j in range(16):
                    if prbs[0] != 0 :
                        x = x+1                    
                if (0 in data[0]) and (x==0):
                    self.writedata(rows,data,filename)
                    print 'Chip Test (%d/%d) Failed...\n'%(i+1,times)
                else:
                    self.writedata(rows,data,filename)
                    print 'Chip Test (%d/%d) Pass~!\n'%(i+1,times)
        print '\n Test Done~!'


if __name__ == "__main__":
    test = falcon_powercycletest()
    filename = 'test'
    script = 'Falcon_CHRIS2.txt'
    times = 1
    test.autotest(filename,script,times)
    
