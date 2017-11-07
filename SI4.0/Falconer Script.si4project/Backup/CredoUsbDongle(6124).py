import platform
import os
import ctypes as c

class CredoUsbDongle:
    maxDeviceCount = 4

    def __init__(self, lib_name_linux, lib_name_window, phy_addr=0, dev_addr=1, shared_lib_path=""):
        self.cr_phy_addr = phy_addr
        self.cr_dev_addr = dev_addr

        if platform.system() == 'Linux':
            shared_lib_name = lib_name_linux
        elif platform.system() == 'Windows':
            shared_lib_name = lib_name_window
        else:
            print 'Your platform is unsupported!'
            exit(-1)

        shared_lib_path = os.path.abspath(shared_lib_path)
        self.lib_path_name = os.path.join(shared_lib_path, shared_lib_name)

        self.lib = c.CDLL(self.lib_path_name)

    def CredoUsbDongleOpen(self, usb_sel, phy_addr = None, dev_addr = None, mdio = 0):
        if phy_addr is None:
            phy_addr = self.cr_phy_addr
        if dev_addr is None:
            dev_addr = self.cr_dev_addr
        for i in range(5):
            ret = self.lib.cr_mdio_init(c.c_ubyte(phy_addr), c.c_ubyte(dev_addr), c.c_int(usb_sel), c.c_int(mdio))
            if ret != 0:
                self.lib.cr_mdio_close()
            else:
                port_index = usb_sel
                return port_index
            self.lib.cr_wait(10)
        raise IOError("MDIO Open Error!")

    def CredoUsbDogleOpenFirstValid(self, phy_addr = None, dev_addr = None, mdio = 0):
        if phy_addr is None:
            phy_addr = self.cr_phy_addr
        if dev_addr is None:
            dev_addr = self.cr_dev_addr

        deviceCounts = self.lib.cr_mdio_get_device_number()
        if deviceCounts > self.maxDeviceCount:
            deviceCounts = self.maxDeviceCount

        for i in range (3):
            for j in range(deviceCounts):
                ret = self.lib.cr_mdio_init(c.c_ubyte(phy_addr), c.c_ubyte(dev_addr), c.c_int(j), c.c_int(mdio))
                if ret == 0:
                    port_index = j
                    return port_index
            self.lib.cr_wait(10)
        raise IOError("MDIO Open Error!")

    def CredoUsbDongleGetDeviceNumber(self):
        deviceCounts = self.lib.cr_mdio_get_device_number()
        if deviceCounts > self.maxDeviceCount:
            deviceCounts = self.maxDeviceCount
        return deviceCounts


    # def CredoUsbDongleOpen(self, usb_sel, phy_addr = None, dev_addr = None):
    #     if phy_addr is None:
    #         phy_addr = self.cr_phy_addr
    #     if dev_addr is None:
    #         dev_addr = self.cr_dev_addr
    #     for i in range(5):
    #         ret = self.lib.cr_mdio_init(c.c_ubyte(phy_addr), c.c_ubyte(dev_addr), c.c_int(usb_sel))
    #         if ret != 0:
    #             self.lib.cr_mdio_close()
    #             ret = self.lib.cr_mdio_init(c.c_ubyte(phy_addr), c.c_ubyte(dev_addr), c.c_int(1))
    #             if ret != 0:
    #                 self.lib.cr_mdio_close()
    #             else:
    #                 port_index = 1
    #                 return port_index
    #         else:
    #             port_index = 0
    #             return port_index
    #         self.lib.cr_wait(10)
    #     raise IOError("MDIO Open Error!")

    # def listDeviceWithLocationId(self):
    #     locId = c.c_long * 16
    #     locId_result = locId()
    #     self.lib.cr_mdio_listDevice(locId_result)
    #     A = map(lambda x: x, locId_result)
    #     print A
    #     return A

    def isUsbDongleValid(self):
        nValid = self.lib.isDeviceHadleValid()
        if nValid == 1:
            return True
        return False

    def CredoUsbDongleMdioRead(self, reg):
        data = self.lib.cr_mdio_read(c.c_ushort(reg))
        return data  # FIXME: may have issue

    def CredoUsbDongleMdioWrite(self, reg, data):
        ret = self.lib.cr_mdio_write(c.c_ushort(reg), c.c_ushort(data))
        if ret != 0:
            raise IOError("MDIO Write Error!")

    def CredoUsbDongleClose(self):
        ret = self.lib.cr_mdio_close()
        if ret != 0:
            raise IOError("MDIO Close Error!")

class CredoNdUsbDongle:
    def __init__(self, lib_name_linux, lib_name_window, phy_addr=0, dev_addr=1, shared_lib_path=""):
        self.cr_phy_addr = phy_addr
        self.cr_dev_addr = dev_addr

        if platform.system() == 'Linux':
            shared_lib_name = lib_name_linux
        elif platform.system() == 'Windows':
            shared_lib_name = lib_name_window
        else:
            print 'Your platform is unsupported!'
            exit(-1)

        shared_lib_path = os.path.abspath(shared_lib_path)

        self.lib = c.CDLL(os.path.join(shared_lib_path, shared_lib_name))

    def CredoNdUsbDongleOpen(self):
        ret = self.lib.CredoNdUsbDongleOpen(c.c_ubyte(self.cr_phy_addr), c.c_ubyte(self.cr_dev_addr))
        if ret != 0:
            raise Exception("Open Failed")  # XXX

    def CredoNdUsbDongleMdioRead(self, reg):
        data = self.lib.CredoNdUsbDongleMdioRead(c.c_ushort(reg))
        return data  # FIXME: may have issue

    def CredoNdUsbDongleMdioWrite(self, reg, data):
        ret = self.lib.CredoNdUsbDongleMdioWrite(c.c_ushort(reg), c.c_ushort(data))
        if ret != 0:
            raise Exception("Write Failed")  # XXX

    def CredoNdUsbDongleClose(self):
        self.lib.CredoNdUsbDongleClose()

class LibBase:
    lib_name_linux = ""
    lib_name_window = ""

    def __init__(self, shared_lib_path=""):
        # TODO: support 2 usb dongle
        if platform.system() == 'Linux' and len(self.lib_name_linux) <= 0:
            raise Exception("Need correct lib path")
        elif platform.system() == 'Windows' and len(self.lib_name_window) <= 0:
            raise Exception("Need correct lib path")
        self.usb = CredoUsbDongle(self.lib_name_linux, self.lib_name_window,
                shared_lib_path=shared_lib_path)

        # Firmware communicate default registers
        self.reg_cmd = 0x9815
        self.reg_cmd_detail = 0x9816
        self.reg_reg_value = 0x9812

    def getLibPathName(self):
        return self.usb.lib_path_name

    def isDebug(self):
        result = self.usb.lib.isDebug()
        if result == 1:
            return True
        else:
            return False

    # def listDeviceWithLocationId(self):
    #     return self.usb.listDeviceWithLocationId()

    def connectFirstValid(self):
        self.connected = False
        port_index = self.usb.CredoUsbDogleOpenFirstValid()
        self.connected = True
        return port_index

    def connect(self, phy_addr = None, dev_addr = None, usb_sel = 0, mdio = True, I2C = 1):
        self.connected = False
        if mdio:
            port_index = self.usb.CredoUsbDongleOpen(usb_sel, phy_addr, dev_addr, 0)
        else:
            port_index = self.usb.CredoUsbDongleOpen(usb_sel, phy_addr, dev_addr, I2C)
        self.connected = True
        return port_index

    def disconnect(self):
        self.connected = False
        self.usb.CredoUsbDongleClose()

    def isConnected(self):
        return self.connected

    def getDeviceNumber(self):
        return self.usb.CredoUsbDongleGetDeviceNumber()

    # def getComPort(self):
    #     return self.usb.CredoUsbDongleGetComPort()

    def isDeviceValid(self):
        return self.usb.isUsbDongleValid()

    def MdioRd(self, reg):
        # return self.usb.CredoNdUsbDongleMdioRead(reg)
        return self.usb.CredoUsbDongleMdioRead(reg)

    def MdioWr(self, reg, val):
        # return self.usb.CredoNdUsbDongleMdioWrite(reg, val)
        return self.usb.CredoUsbDongleMdioWrite(reg, val)

    def setClkDivMdio(self, clkDivMdio):
        self.usb.lib.setClkDivMdio(c.c_int64(clkDivMdio))

    # Firmware communicate functions
    def fw_reg_setup(self, reg_cmd, reg_cmd_detail, reg_reg_value):
        self.reg_cmd = reg_cmd
        self.reg_cmd_detail = reg_cmd_detail
        self.reg_reg_value = reg_reg_value

    def fw_reg_rd(self, addr):
        self.MdioWr(self.reg_cmd_detail, addr)
        response = self._fw_cmd(0xe010)
        if response<0:
            raise IOError("Firmware register read timeout! Is firmware loaded?")
        if response!=0x0e00:
            raise RuntimeError("Firmware register read error, code=%04x" % response)
        return self.MdioRd(self.reg_reg_value)

    def fw_reg_wr(self, addr, value):
        self.MdioWr(self.reg_reg_value, value)
        self.MdioWr(self.reg_cmd_detail, addr)
        response = self._fw_cmd(0xe020)
        if response<0:
            raise IOError("Firmware register write timeout! Is firmware loaded?")
        if response!=0x0e00:
            raise RuntimeError("Firmware register write error, code=%04x" % response)

    def fw_reg_rd_all(self):
        addr = 0
        result = []
        while True:
            try:
                result.append(self.fw_reg_rd(addr))
                addr += 1
            except RuntimeError:
                break
        return result

    def _fw_cmd(self, cmd):
        self.MdioWr(self.reg_cmd, cmd)
        count=0
        response = self.MdioRd(self.reg_cmd)
        while (response>>12)!=0 and count<1000:
            count+=1
            response = self.MdioRd(self.reg_cmd)
        if count>=1000:
            return -1
        return response

    def cr_write_i2c_AC_8(self, regAddr, data, i2cAddr):
        fun = self.usb.lib.cr_write_i2c_AC_8
        return fun(regAddr, data, i2cAddr)

    def cr_read_i2c_AC_8(self, regAddr, i2cAddr):
        fun = self.usb.lib.cr_read_i2c_AC_8
        return fun(regAddr, i2cAddr)