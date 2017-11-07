import visa
import time

class E3646a():
    def __init__(self):
        self.rm = visa.ResourceManager()
        self.power = None
        self.target = None
        self.port = None

    def __del__(self):
        if self.power != None:
            self.power.close()
            self.power = None
        if self.rm != None:
            self.rm.close()
            self.rm = None

    def opensource(self, port = 0, target = 7):
        self.target = target
        self.port = port
        self.power = self.rm.open_resource('GPIB'+str(port)+'::' +str(target)+'::INSTR')
        self.power.read_termination = '\n'
        self.power.write_termination = '\n'
        
    def write(self, data = ''):
        self.power.write(data)

    def query(self, data = ''):
        self.power.query(data)

    def sel_src(self, src):
        self.power.write('INST:NSEL '+str(src))

    def setting(self, volt, curr):
        self.power.write('APPL ' +str(volt)+',' +str(curr))

    def output(self, en = ''):
        self.power.write('OUTP ' +str(en))

if __name__ == '__main__':
    Power = E3646a()
    Power.opensource(0, 5)
    Power.sel_src(1)
    Power.setting(4,2)
    Power.sel_src(2)
    Power.setting(7,2)
    Power.output(1)
    time.sleep(10)
    Power.output(0)

    #instr.opensource(0, 5)
    #instr.sel_src(1)
    #instr.setting(6)

    #instr.sel_src(2)
    #instr.setting(3)
    #instr.output(1)

    #rm = visa.ResourceManager()
    #p = rm.open_resource('GPIB0::7::INSTR')
    #p.write('INST:NSEL 1')
    #p.write('APPL 4, 3')
    #p.write('INST:NSEL 2')
    #p.write('APPL 8, 3')
    #p.write('OUTP 1')
