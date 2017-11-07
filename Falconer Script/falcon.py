import ctypes as c
import sys
import os
try:
    sys.path.insert(0, os.path.abspath('../../lib/'))
except:
    pass

#from CredoSerdesCommon.CredoUsbDongle import *
from CredoUsbDongle import *

class Falcon_lib(LibBase):
	lib_name_linux = "libfalcon_api.so"
	lib_name_window = "falcon_api.dll"

	macros = ['A0', 'A1', 'A2', 'A3']

	def cr_write_i2c_AC_8(self, regAddr, data, i2cAddr):
		fun = self.usb.lib.cr_write_i2c_AC_8
		return fun(regAddr, data, i2cAddr)

	def cr_read_i2c_AC_8(self, regAddr, i2cAddr):
		fun = self.usb.lib.cr_read_i2c_AC_8
		return fun(regAddr, i2cAddr)

	def TCMRd(self, reg, eip_sel):
		fun = self.usb.lib.tcm_rd
		fun.restype = c.c_uint
		return fun(c.c_uint(reg), c.c_uint(eip_sel))

	def TCMWr(self, reg, data, eip_sel):
		fun = self.usb.lib.tcm_wr
		fun(c.c_uint(reg), c.c_uint(data), c.c_uint(eip_sel))

	def Falcon_DAC_value(self, lane_num):
		fun = self.usb.lib.Falcon_DAC_value
		fun.restype = c.c_double
		return fun(c.c_double(lane_num))

	def Falcon_DAC_value_B(self, lane_num):  #hummingBird
		fun = self.usb.lib.Falcon_DAC_value_B
		fun.restype = c.c_double
		return fun(c.c_double(lane_num))

	def Falcon_InitializeMainDriver_TX(self, cursor, lane_num):
		fun = self.usb.lib.Falcon_InitializeMainDriver_TX
		fun(c.c_double(cursor), c.c_double(lane_num))

	def Falcon_InitializeCurrent(self, current, lane_num):  #HummingBird
		fun = self.usb.lib.Volt_InitializeCurrent
		fun(c.c_double(current), c.c_double(lane_num))

	def Falcon_InitializeFUN_TX(self, lane_num):
		fun = self.usb.lib.Falcon_InitializeFUN_TX
		fun(c.c_double(lane_num))

	def Falcon_InitializeFUN_B_TX(self, lane_num):   #HummingBird
		fun = self.usb.lib.Falcon_InitializeFUN_B_TX
		fun(c.c_double(lane_num))
		
	def Falcon_InitializePRBS(self, prbs_mode, prbs_dis, lane_num):
		fun = self.usb.lib.Falcon_InitializePRBS
		fun(c.c_uint32(prbs_mode), c.c_double(prbs_dis), c.c_double(lane_num))

	def Falcon_InitializePRBS_B(self, prbs_mode, prbs_dis, lane_num):  #HummingBird
		fun = self.usb.lib.Falcon_InitializePRBS_B
		fun(c.c_uint32(prbs_mode), c.c_double(prbs_dis), c.c_double(lane_num))
		
	def Falcon_InitializePRBS_TX(self, prbs_mode, lane_num):
		fun = self.usb.lib.Falcon_InitializePRBS_TX
		fun(c.c_uint32(prbs_mode), c.c_double(lane_num))

	def Falcon_InitializePRBS_B_TX(self, prbs_mode, lane_num): #HummingBird
		fun = self.usb.lib.Falcon_InitializePRBS_B_TX
		fun(c.c_uint32(prbs_mode), c.c_double(lane_num))
		
	def Falcon_InitializePattern_1T(self, lane_num):
		fun = self.usb.lib.Falcon_InitializePattern_1T
		fun(c.c_double(lane_num))
		
	def Falcon_InitializePattern_2T(self, lane_num):
		fun = self.usb.lib.Falcon_InitializePattern_2T
		fun(c.c_double(lane_num))
		
	def Falcon_InitializePattern_4T(self, lane_num):
		fun = self.usb.lib.Falcon_InitializePattern_4T
		fun(c.c_double(lane_num))
		
	def Falcon_InitializePattern_8T(self, lane_num):
		fun = self.usb.lib.Falcon_InitializePattern_8T
		fun(c.c_double(lane_num))

	def Falcon_InitializePattern_16T(self, lane_num):
		fun = self.usb.lib.Falcon_InitializePattern_16T
		fun(c.c_double(lane_num))

	def Falcon_InitializePattern_B_1T(self, lane_num):
		fun = self.usb.lib.Falcon_InitializePattern_B_1T
		fun(c.c_double(lane_num))

	def Falcon_InitializePattern_B_2T(self, lane_num):
		fun = self.usb.lib.Falcon_InitializePattern_B_2T
		fun(c.c_double(lane_num))

	def Falcon_InitializePattern_B_4T(self, lane_num):
		fun = self.usb.lib.Falcon_InitializePattern_B_4T
		fun(c.c_double(lane_num))

	def Falcon_InitializePattern_B_8T(self, lane_num):
		fun = self.usb.lib.Falcon_InitializePattern_B_8T
		fun(c.c_double(lane_num))

	def Falcon_InitializePattern_B_16T(self, lane_num):
		fun = self.usb.lib.Falcon_InitializePattern_B_16T
		fun(c.c_double(lane_num))

	def Falcon_Read_PRBSMode_RX(self, lane_num):
		fun = self.usb.lib.Falcon_Read_PRBSMode_RX
		fun.restype = c.c_double
		res = fun(c.c_double(lane_num))
		if res == 1:
			return 0, 0
		else:
			return 1, res - 2
	#HummingBird
	def Falcon_Read_PRBSMode_B_RX(self, lane_num):
		fun = self.usb.lib.Falcon_Read_PRBS_mode_B
		fun.restype = c.c_double
		addrs = (0, 0x2000, 0x2100, 0x2200, 0x2300, 0x2500, 0x2600, 0x2700, 0x2800,
				0x3000, 0x3100, 0x3200, 0x3300, 0x3500, 0x3600, 0x3700, 0x3800)
		enable_data = self.MdioRd(addrs[lane_num] | 0x0042)
		return ((enable_data & 0x0002) != 0), fun(c.c_double(lane_num))

	def Falcon_Read_PRBSMode_TX(self, lane_num):
		fun = self.usb.lib.Falcon_Read_PRBSMode_TX
		fun.restype = c.c_double
		res = fun(c.c_double(lane_num))
		if res == -1:
			# FIXME: -1 means error
			#return 0
			return 10
		else:
			return res - 1

	def Falcon_Read_PRBSMode_B_TX(self, lane_num):  #HummingBird
		fun = self.usb.lib.Falcon_Read_PRBSMode_B_TX
		fun.restype = c.c_double
		res = fun(c.c_double(lane_num))
		if res == -1:
			# FIXME: -1 means error
			#return 0
			return 10
		else:
			return res - 1

	def Falcon_InitializePostDriver_TX(self, post_cursor, lane_num):
		fun = self.usb.lib.Falcon_InitializePostDriver_TX
		fun(c.c_double(post_cursor), c.c_double(lane_num))

	def Falcon_InitializePostDriver_B_TX(self, post_cursor, lane_num): #HummingBird
		fun = self.usb.lib.Falcon_InitializePostDriver_B_TX
		fun(c.c_double(post_cursor), c.c_double(lane_num))
	
	def Falcon_InitializePostDriver2_TX(self, post_cursor, lane_num):
		fun = self.usb.lib.Falcon_InitializePostDriver2_TX
		fun(c.c_double(post_cursor), c.c_double(lane_num))
	
	def Falcon_InitializePreDriver2_TX(self, post_cursor, lane_num):
		fun = self.usb.lib.Falcon_InitializePreDriver2_TX
		fun(c.c_double(post_cursor), c.c_double(lane_num))
		
	def Falcon_InitializePreDriver_TX(self, pre_cursor, lane_num):
		fun = self.usb.lib.Falcon_InitializePreDriver_TX
		fun(c.c_double(pre_cursor), c.c_double(lane_num))

	def Falcon_InitializePreDriver_B_TX(self, pre_cursor, lane_num):  #HummingBird
		fun = self.usb.lib.Falcon_InitializePreDriver_B_TX
		fun(c.c_double(pre_cursor), c.c_double(lane_num))
		
	def Falcon_Link_Status(self, lane_num):
		fun = self.usb.lib.Falcon_Link_Status
		fun.restype = c.c_double
		return fun(c.c_double(lane_num))

	#Humming Bird
	def Falcon_Link_Status_B(self, lane_num):
		fun = self.usb.lib.Falcon_Link_Status_B
		fun.restype = c.c_double
		return fun(c.c_double(lane_num))
		
	def Falcon_Logic_Reset(self):
		fun = self.usb.lib.Falcon_Logic_Reset
		fun()

	def Falcon_AN_en(self, enable):
		fun = self.usb.lib.Falcon_AN_en
		fun(c.c_double(enable))

	def Falcon_TRA_en(self, enable):
		fun = self.usb.lib.Falcon_TRA_en
		fun(c.c_double(enable))
		
	def Falcon_OW_agc(self, agc_setting, lane_num):
		fun = self.usb.lib.Falcon_OW_agc
		fun(c.c_uint32(agc_setting), c.c_double(lane_num))

	def Falcon_OW_agc_B(self, agc_setting, lane_num):   #HummingBird
		fun = self.usb.lib.Falcon_OW_agc_B
		fun(c.c_uint32(agc_setting), c.c_double(lane_num))
	
	def Falcon_Read_OW_agc(self, lane_num):
		fun = self.usb.lib.Falcon_Read_OW_agc
		fun.restype = c.c_double
		return fun(c.c_double(lane_num))

	def Falcon_Read_OW_agc_B(self, lane_num):   #HummingBird
		fun = self.usb.lib.Falcon_Read_OW_agc_B
		fun.restype = c.c_double
		return fun(c.c_double(lane_num))

	def Falcon_RX_reverse(self, flip, lane_num):
		fun = self.usb.lib.Falcon_RX_reverse
		fun(c.c_double(flip), c.c_double(lane_num))

	def Falcon_RX_reverse_B(self, flip, lane_num):   #HummingBird
		fun = self.usb.lib.Falcon_RX_reverse_B
		fun(c.c_double(flip), c.c_double(lane_num))
		
	def Falcon_Read_RX_reverse(self, lane_num):
		fun = self.usb.lib.Falcon_Read_RX_reverse
		fun.restype = c.c_double
		return fun(c.c_double(lane_num))

	def Falcon_Read_RX_reverse_B(self, lane_num):   #HummingBird
		# TODO: move this routine to MATLAB code
		try:
			fun = self.usb.lib.Falcon_Read_RX_reverse_B
			fun.restype = c.c_double
			return fun(c.c_double(lane_num))
		except AttributeError:
			addrs = (0x2000, 0x2100, 0x2200, 0x2300, 0x2500, 0x2600, 0x2700, 0x2800,
					0x3000, 0x3100, 0x3200, 0x3300, 0x3500, 0x3600, 0x3700, 0x3800)
			addr = addrs[lane_num - 1] + 0x0042
			val = self.MdioRd(addr)
			return (val & 1)

	def Falcon_ReadDriver_post(self, lane_num):
		fun = self.usb.lib.Falcon_ReadDriver_post
		fun.restype = c.c_double
		cursor = int(fun(c.c_double(lane_num)))
		if cursor & 0x80:
			cursor = -(256 - cursor)
		return cursor

	def Falcon_ReadDriver_post_B(self, lane_num): #HummingBird
		fun = self.usb.lib.Falcon_ReadDriver_post_B
		fun.restype = c.c_double
		return fun(c.c_double(lane_num))

	def Falcon_ReadDriver_post2(self, lane_num):
		fun = self.usb.lib.Falcon_ReadDriver_post2
		fun.restype = c.c_double
		cursor = int(fun(c.c_double(lane_num)))
		if cursor & 0x80:
			cursor = -(256 - cursor)
		return cursor

	def Falcon_ReadDriver_pre2(self, lane_num):
		fun = self.usb.lib.Falcon_ReadDriver_pre2
		fun.restype = c.c_double
		cursor = int(fun(c.c_double(lane_num)))
		if cursor & 0x80:
			cursor = -(256 - cursor)
		return cursor

	def Falcon_ReadDriver_pre(self, lane_num):
		fun = self.usb.lib.Falcon_ReadDriver_pre
		fun.restype = c.c_double
		cursor = int(fun(c.c_double(lane_num)))
		if cursor & 0x80:
			cursor = -(256 - cursor)
		return cursor

	def Falcon_ReadDriver_pre_B(self, lane_num):  #HummingBird
		fun = self.usb.lib.Falcon_ReadDriver_pre_B
		fun.restype = c.c_double
		return fun(c.c_double(lane_num))

	def Falcon_ReadDriver_Main(self, lane_num):
		fun = self.usb.lib.Falcon_ReadDriver_Main
		fun.restype = c.c_double
		cursor = int(fun(c.c_double(lane_num)))
		if cursor & 0x80:
			cursor = -(256 - cursor)
		return cursor

	def Falcon_ReadDriver_Main_B(self, lane_num): #HummingBird
		# TODO: move this routine to MATLAB code
		addrs = (0x2000, 0x2100, 0x2200, 0x2300, 0x2500, 0x2600, 0x2700, 0x2800,
				0x3000, 0x3100, 0x3200, 0x3300, 0x3500, 0x3600, 0x3700, 0x3800)
		addr = addrs[lane_num - 1] + 0x00f5
		val = self.MdioRd(addr)

		mtab = {
			4: 20,
			9: 40,
			12: 60, # FIXME which is 60
			14: 60, # FIXME which is 60
			19: 80,
			24: 100
		}
		cur = (val >> 11) & 0x1f
		if cur is mtab.keys():
			cur_val = mtab[cur]
		else:
			cur_val = 60

		return cur_val

	def Falcon_Read_Eyemargin(self, lane_num):
		fun = self.usb.lib.Falcon_Read_Eyemargin
		fun.restype = c.c_double
		return fun(c.c_double(lane_num))

	def Falcon_Read_margin0(self, lane_num):
		fun = self.usb.lib.Falcon_Read_margin0
		fun.restype = c.c_double
		return fun(c.c_double(lane_num))

	def Falcon_Read_margin1(self, lane_num):
		fun = self.usb.lib.Falcon_Read_margin1
		fun.restype = c.c_double
		return fun(c.c_double(lane_num))

	def Falcon_Read_margin2(self, lane_num):
		fun = self.usb.lib.Falcon_Read_margin2
		fun.restype = c.c_double
		return fun(c.c_double(lane_num))


	#25G
	def Falcon_Read_Eyemargin_B(self, lane_num):
		fun = self.usb.lib.Falcon_Read_Eyemargin_B
		fun.restype = c.c_double
		return fun(c.c_double(lane_num))
		
	def Falcon_Read_F1(self, lane_num):  #HummingBird
		fun = self.usb.lib.Falcon_Read_F1
		fun.restype = c.c_double
		return fun(c.c_double(lane_num))

	def Falcon_Read_F2(self, lane_num):  #HummingBird
		fun = self.usb.lib.Falcon_Read_F2
		fun.restype = c.c_double
		return fun(c.c_double(lane_num))
		
	def Falcon_Read_F3(self, lane_num):  #HummingBird
		fun = self.usb.lib.Falcon_Read_F3
		fun.restype = c.c_double
		return fun(c.c_double(lane_num))
		

	def RxReadPRBSCounter(self, lane_num):
		fun = self.usb.lib.Falcon_Read_PRBS_cntr
		fun.restype = c.c_double
		return fun(c.c_double(lane_num))

	#25G
	def RxReadPRBSCounterB(self, lane_num):
		fun = self.usb.lib.Falcon_Read_PRBS_cntr_B
		fun.restype = c.c_double
		return fun(c.c_double(lane_num))

	def Falcon_Reg_default_debug_B(self):
		fun = self.usb.lib.Falcon_Reg_default_debug_B
		fun()
		
	def Falcon_Reset_PRBS_Cntr(self, lane_num):
		fun = self.usb.lib.Falcon_Reset_PRBS_Cntr
		fun(c.c_double(lane_num))

	#HummingBird
	def Falcon_Reset_PRBS_Cntr_B(self, lane_num):
		fun = self.usb.lib.Falcon_Reset_PRBS_Cntr_B
		fun(c.c_double(lane_num))
		
	def Falcon_Reset_SM(self, lane_num):
		fun = self.usb.lib.Falcon_Reset_SM
		fun(c.c_double(lane_num))

	def Falcon_Reset_SM_B(self, lane_num):   #HummingBird
		fun = self.usb.lib.Falcon_Reset_SM_B
		fun(c.c_double(lane_num))
		
	def Falcon_Software_Reset(self):
		fun = self.usb.lib.Falcon_Software_Reset
		fun()
		
	def Falcon_TX_reverse(self, flip, lane_num):
		fun = self.usb.lib.Falcon_TX_reverse
		fun(c.c_double(flip), c.c_double(lane_num))

	def Falcon_TX_reverse_B(self, flip, lane_num):  #HummingBird
		fun = self.usb.lib.Falcon_TX_reverse_B
		fun(c.c_double(flip), c.c_double(lane_num))

	def Falcon_Read_TX_reverse(self, lane_num):
		fun = self.usb.lib.Falcon_Read_TX_reverse
		fun.restype = c.c_double
		return fun(c.c_double(lane_num))

	def Falcon_Read_TX_reverse_B(self, lane_num):
		# TODO: move this routine to MATLAB code
		try:
			fun = self.usb.lib.Falcon_Read_TX_reverse_B
			fun.restype = c.c_double
			return fun(c.c_double(lane_num))
		except AttributeError:
			addrs = (0x2000, 0x2100, 0x2200, 0x2300, 0x2500, 0x2600, 0x2700, 0x2800,
					0x3000, 0x3100, 0x3200, 0x3300, 0x3500, 0x3600, 0x3700, 0x3800)
			addr = addrs[lane_num - 1] + 0x00A0
			val = self.MdioRd(addr)
			return (val & (1 << 7)) != 0     # Tx_data_firmware_flip
		
	def Falcon_ContinueStateMachine_RX(self, lane_num):
		fun = self.usb.lib.Falcon_ContinueStateMachine_RX
		fun(c.c_double(lane_num))

	def Falcon_ContinueStateMachine_B_RX(self, lane_num):  #HummingBird
		fun = self.usb.lib.Falcon_ContinueStateMachine_B_RX
		fun(c.c_double(lane_num))
		
	def Falcon_InitializeAnalog(self):
		fun = self.usb.lib.Falcon_InitializeAnalog
		fun()
		
	def Falcon_InitializePRBS_RX(self, prbs_mode, flip_polarity, lane_num):
		fun = self.usb.lib.Falcon_InitializePRBS_RX
		fun(c.c_uint32(prbs_mode), c.c_double(flip_polarity), c.c_double(lane_num))
		

	def Falcon_OW_agc_B_RX(self, agc_setting, lane_num):
		fun = self.usb.lib.Falcon_OW_agc_B_RX
		fun(c.c_uint32(agc_setting), c.c_double(lane_num))
		
	def Falcon_OW_dac_RX(self, dac_setting, lane_num):
		fun = self.usb.lib.Falcon_OW_dac_RX
		fun(c.c_uint32(dac_setting), c.c_double(lane_num))

	def Falcon_OW_dac_B_RX(self, dac_setting, lane_num): #HummingBird
		fun = self.usb.lib.Falcon_OW_dac_B_RX
		fun(c.c_uint32(dac_setting), c.c_double(lane_num))
		
	def Falcon_PRBS_err_inject_TX(self, lane_num):
		fun = self.usb.lib.Falcon_PRBS_err_inject_TX
		fun(c.c_double(lane_num))

	def Falcon_PRBS_err_inject_B_TX(self, lane_num):
		fun = self.usb.lib.Falcon_PRBS_err_inject_B_TX
		fun(c.c_double(lane_num))
		
	def Falcon_ReadComparatorCal(self, lane_num):
		arr_t = c.c_double * 48
		#arr_t = c.c_double * 88
		t_A = arr_t()
		t_B = arr_t()
		fun = self.usb.lib.Falcon_ReadComparatorCal
		fun(c.c_double(lane_num), t_A, t_B)
		A = map(lambda x: x, t_A)
		B = map(lambda x: x, t_B)
		return {'A':A, 'B':B}

	def Falcon_Read_DTL_RX(self, lane_num):
		class struct_t(c.Structure):
			_fields_ = [
				('phase1_out', c.c_double),
				('phase2_out', c.c_double),
				('phase3_out', c.c_double),
				('phase4_out', c.c_double)
			]
		fun = self.usb.lib.Falcon_Read_DTL_RX
		fun.restype = struct_t
		p = fun(c.c_double(lane_num))
		return {'phase1_out':p.phase1_out, 
		        'phase2_out':p.phase2_out,
		        'phase3_out':p.phase3_out,
		        'phase4_out':p.phase4_out}

	def Falcon_Read_DTL_B_RX(self, lane_num):  #HummingBird
		class struct_t(c.Structure):
			_fields_ = [
				('phase1_out', c.c_double),
				('phase2_out', c.c_double),
				('phase3_out', c.c_double),
				('phase4_out', c.c_double)
			]
		fun = self.usb.lib.Falcon_Read_DTL_B_RX
		fun.restype = struct_t
		p = fun(c.c_double(lane_num))
		return {'phase1_out':p.phase1_out,
		        'phase2_out':p.phase2_out,
		        'phase3_out':p.phase3_out,
		        'phase4_out':p.phase4_out}


	def Falcon_Reg_default_load_RX(self, lane_num):
		fun = self.usb.lib.Falcon_Reg_default_load_RX
		fun(c.c_double(lane_num))

	def Falcon_Reg_default_load_B_RX(self, lane_num):
		fun = self.usb.lib.Falcon_Reg_default_load_B_RX
		fun(c.c_double(lane_num))
		
	def Falcon_Reset_PRBS_Cntr_RX(self, lane_num):
		fun = self.usb.lib.Falcon_Reset_PRBS_Cntr_RX
		fun(c.c_double(lane_num))

	def Falcon_multiple_DTL_read_RX(self, lane_num, test_length):
		dtl_list = []
		for x in range(test_length):
			dtl_list.append(self.Falcon_Read_DTL_RX(lane_num))
		return {'phase1':map(lambda x:x['phase1_out'], dtl_list),
		        'phase2':map(lambda x:x['phase2_out'], dtl_list),
		        'phase3':map(lambda x:x['phase3_out'], dtl_list),
		        'phase4':map(lambda x:x['phase4_out'], dtl_list)}
		
	def MdioRd(self, RegAddr):
		return self.usb.CredoUsbDongleMdioRead(RegAddr)

	def bin2mdio(self, data, RdCheck):
		fun = self.usb.lib.bin2mdio
		c_ubyte_arr = c.c_ubyte * 65536
		ubyte_arr = c_ubyte_arr(*map(ord, data))
		fun(c.cast(ubyte_arr, c.POINTER(c.c_ubyte)), c.c_int(RdCheck))

	def Falcon_EM(self, ber_pop, lane_num):
		fun = self.usb.lib.Falcon_EM

		ber_arr_2d = (c.c_double * 33) * 127

		x = (c.c_double * 34)()
		y = (c.c_double * 128)()
		cm = ((c.c_double * 127) * 33)()
		fun(c.c_double(ber_pop), c.c_double(lane_num), x, y, cm)

		return (x, y, cm)

	#HummingBird
	def Falcon_EM_B(self, ber_pop, lane_num):
		fun = self.usb.lib.Falcon_EM_B

		x = (c.c_double * 34)()
		y = (c.c_double * 100)()
		cm = ((c.c_double * 99) * 33)()
		fun(c.c_double(ber_pop), c.c_double(lane_num), x, y, cm)

		return (x, y, cm)

	def Falcon_EM_read_progress(self):
		fun = self.usb.lib.Falcon_EM_read_progress
		fun.restype = c.c_double
		return int(fun())

	def Falcon_EM_read_progress_B(self):
		try:
			fun = self.usb.lib.Falcon_EM_read_progress_B
			fun.restype = c.c_double
			return int(fun())
		except AttributeError:
			fun = self.usb.lib.Falcon_EM_read_progress
			fun.restype = c.c_double
			return int(fun())

	def Falcon_EM_abort(self):
		fun = self.usb.lib.Falcon_EM_abort
		fun()

	def Falcon_EM_abort_B(self):
		try:
			fun = self.usb.lib.Falcon_EM_abort_B
			fun()
		except AttributeError:
			fun = self.usb.lib.Falcon_EM_abort
			fun()

	def LoadFirmware_read_progress(self):
		fun = self.usb.lib.LoadFirmware_read_progress
		fun.restype = c.c_double
		return int(fun())

	def Falcon_EM_Vert(self, ber_pop, lane_num):
		fun = self.usb.lib.Falcon_EM_Vert

		dmap = ((c.c_double * 127) * 3)()
		fun(c.c_double(ber_pop), c.c_double(lane_num), dmap)

		return dmap

	#25G
	def Falcon_EM_Vert_B(self, ber_pop, lane_num):
		fun = self.usb.lib.Falcon_EM_Vert_B

		dmap = ((c.c_double * 62) * 3)()
		fun(c.c_double(ber_pop), c.c_double(lane_num), dmap)

		return dmap

	def Falcon_EM_Vert_read_progress(self):
		fun = self.usb.lib.Falcon_EM_Vert_read_progress
		fun.restype = c.c_double
		return int(fun())

	def Falcon_EM_Vert_read_progress_B(self):
		try:
			#print "em_vert_read_progress_B"
			fun = self.usb.lib.Falcon_EM_Vert_read_progress_B
			fun.restype = c.c_double
			return int(fun())
		except AttributeError:
			print "em_vert_read_progress"
			fun = self.usb.lib.Falcon_EM_Vert_read_progress
			fun.restype = c.c_double
			return int(fun())

	def Falcon_EM_Vert_abort(self):
		fun = self.usb.lib.Falcon_EM_Vert_abort
		fun()

	def Falcon_EM_Vert_abort_B(self):
		try:
			fun = self.usb.lib.Falcon_EM_Vert_abort_B
			fun()
		except AttributeError:
			fun = self.usb.lib.Falcon_EM_Vert_abort
			fun()

	def Bitset(self, addr, value, lbit, width):
		fun = self.usb.lib.Falcon_Bitset
		fun(c.c_ushort(addr), c.c_ushort(value), c.c_int(lbit), c.c_int(width))

	def get_lanes(self, macro, lane_num):
		lanes = []
		if macro != 0xf and lane_num != 0xf:
			lanes.append(macro*4 + lane_num)
		elif macro == 0xf and lane_num != 0xf:
			lanes = [i+lane_num for i in range(16) if i%4 == 0]
		elif macro != 0xf and lane_num == 0xf:
			lanes = [macro*4 + i for i in range(16) if i<4]
		else:
			lanes = [i for i in range(16)]
		return lanes

	def M_Falcon_DAC_value_B(self, macro, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_DAC_value_B
		lanes = []
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_int(macro), c.c_int(lane_num), value_list)
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_InitializeFUN_TX_B(self, macro, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_InitializeFUN_TX_B
		lanes = None
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_int(macro), c.c_int(lane_num))
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_InitializePRBS_B(self, macro, prbs_mode, prbs_dis, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_InitializePRBS_B
		lanes = None
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_uint32(prbs_mode), c.c_double(prbs_dis), c.c_int(lane_num))
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_InitializePRBS_TX_B(self, macro, prbs_mode, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_InitializePRBS_TX_B
		lanes = None
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_uint32(prbs_mode), c.c_int(lane_num))
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_InitializePattern_1T_B(self, macro, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_InitializePattern_1T_B
		lanes = None
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_int(macro), c.c_int(lane_num))
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_InitializePattern_2T_B(self, macro, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_InitializePattern_2T_B
		lanes = None
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_int(macro), c.c_int(lane_num))
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_InitializePattern_4T_B(self, macro, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_InitializePattern_4T_B
		lanes = None
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_int(macro), c.c_int(lane_num))
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_InitializePattern_8T_B(self, macro, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_InitializePattern_8T_B
		lanes = None
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_int(macro), c.c_int(lane_num))
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_InitializePattern_16T_B(self, macro, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_InitializePattern_16T_B
		lanes = None
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_int(macro), c.c_int(lane_num))
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_InitializePreDriver_TX_B(self, macro, pre_cursor, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_InitializePreDriver_TX_B
		lanes = None
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_double(pre_cursor), c.c_int(lane_num))
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_InitializePostDriver_TX_B(self, macro, post_cursor, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_InitializePostDriver_TX_B
		lanes = None
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_double(post_cursor), c.c_int(lane_num))
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_Link_Status_B(self, macro, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_Link_Status_B
		lanes = []
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_int(macro), c.c_int(lane_num), value_list)
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_OW_agc_B(self, macro, agc_setting, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_OW_agc_B
		lanes = None
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_uint32(agc_setting), c.c_int(lane_num))
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_PRBS_err_inject_TX_B(self, macro, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_PRBS_err_inject_TX_B
		lanes = None
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_int(macro), c.c_int(lane_num))
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_RX_reverse_B(self, macro, flip, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_RX_reverse_B
		lanes = None
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_double(flip), c.c_int(lane_num))
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_ReadDriver_pre_B(self, macro, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_ReadDriver_pre_B
		lanes = []
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_int(macro), c.c_int(lane_num), value_list)
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_ReadDriver_post_B(self, macro, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_ReadDriver_post_B
		lanes = []
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_int(macro), c.c_int(lane_num), value_list)
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_Read_Eyemargin_B(self, macro, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_Read_Eyemargin_B
		lanes = []
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_int(macro), c.c_int(lane_num), value_list)
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_Read_F1_B(self, macro, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_Read_F1_B
		lanes = []
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_int(macro), c.c_int(lane_num), value_list)
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_Read_F2_B(self, macro, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_Read_F2_B
		lanes = []
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_int(macro), c.c_int(lane_num), value_list)
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_Read_F3_B(self, macro, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_Read_F3_B
		lanes = []
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_int(macro), c.c_int(lane_num), value_list)
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_Read_OW_agc_B(self, macro, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_Read_OW_agc_B
		lanes = []
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_int(macro), c.c_int(lane_num), value_list)
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_Read_PRBS_cntr_B(self, macro, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_Read_PRBS_cntr_B
		lanes = []
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_int(macro), c.c_int(lane_num), value_list)
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_Read_PRBSMode_B(self, macro, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_Read_PRBSMode_B
		lanes = []
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_int(macro), c.c_int(lane_num), value_list)
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_Read_RX_reverse_B(self, macro, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_Read_RX_reverse_B
		lanes = []
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_int(macro), c.c_int(lane_num), value_list)
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_Read_TX_reverse_B(self, macro, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_Read_TX_reverse_B
		lanes = []
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_int(macro), c.c_int(lane_num), value_list)
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_Reset_PRBS_Cntr_B(self, macro, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_Reset_PRBS_Cntr_B
		lanes = None
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_int(macro), c.c_int(lane_num))
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_Reset_SM_B(self, macro, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_Reset_SM_B
		lanes = None
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_int(macro), c.c_int(lane_num))
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_TX_reverse_B(self, macro, flip, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_TX_reverse_B
		lanes = None
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_double(flip), c.c_int(lane_num))
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_Read_PRBSMode_TX_B(self, macro, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_Read_PRBSMode_TX_B
		lanes = []
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_int(macro), c.c_int(lane_num), value_list)
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def M_Falcon_Read_PRBSMode_TX_NRZ_B(self, macro, lane_num):  #hummingBird
		fun = self.usb.lib.M_Falcon_Read_PRBSMode_TX_NRZ_B
		lanes = []
		if lanes is not None:
			lanes = self.get_lanes(macro, lane_num)
			value_list = (c.c_double*len(lanes))()
		fun(c.c_int(macro), c.c_int(lane_num), value_list)
		if lanes is not None:
			for index, lane in enumerate(lanes):
				print '%sL%d: %lf' % (self.macros[(lane / 4)], lane % 4, value_list[index])

	def print_format(self, value_list, name_list, macro):
		LANE_COUNT = 4
		MACRO_COUNT = 4
		if macro != 0xf:
			length = LANE_COUNT
		else:
			length = MACRO_COUNT * LANE_COUNT
		sys.stdout.write('                            ')
		for i in range(length):
			sys.stdout.write('%sL%d   ' % (self.macros[i / 4], i % 4))
		sys.stdout.write('\n')
		for index, name in enumerate(name_list):
			if name is None:
				break
			sys.stdout.write('%25s   ' % name)
			for i in range(length):
				sys.stdout.write('%4X   ' % (value_list[index*length+i]))
			sys.stdout.write('\n')
		sys.stdout.write('\n')
		sys.stdout.flush()

	def DumpStateMachine(self, macro):
		value_list = (c.c_uint16*500)()
		name_list = (c.c_char_p*100)()
		self.usb.lib.DumpStateMachine(c.c_int(macro), value_list, name_list)
		print ("===========================State machine=============================")
		self.print_format(value_list, name_list, macro)

	def DumpRX(self, macro):
		value_list = (c.c_uint16*500)()
		name_list = (c.c_char_p*100)()
		self.usb.lib.DumpRX(c.c_int(macro), value_list, name_list)
		print ("=================================RX==================================")
		self.print_format(value_list, name_list, macro)

	def DumpTX(self, macro):
		value_list = (c.c_uint16*500)()
		name_list = (c.c_char_p*100)()
		self.usb.lib.DumpTX(c.c_int(macro), value_list, name_list)
		print ("=================================TX==================================")
		self.print_format(value_list, name_list, macro)

	def DumpAnalog(self, macro):
		value_list = (c.c_uint16*500)()
		name_list = (c.c_char_p*100)()
		self.usb.lib.DumpAnalog(c.c_int(macro), value_list, name_list)
		print ("==============================Analog=================================")
		self.print_format(value_list, name_list, macro)

	def DumpPLL(self, macro):
		value_list = (c.c_uint16*500)()
		name_list = (c.c_char_p*100)()
		self.usb.lib.DumpPLL(c.c_int(macro), value_list, name_list)
		print ("================================PLL==================================")
		self.print_format(value_list, name_list, macro)

	def DumpAll(self, macro):
		self.DumpCPU()
		self.DumpStateMachine(macro)
		self.DumpRX(macro)
		self.DumpTX(macro)
		self.DumpAnalog(macro)
		self.DumpPLL(macro)

	def DumpCPU(self):
		print ("================================CPU==================================")
		name = 'Firmware status'
		rtv = self.usb.lib.ReadFirmwareStatus()
		if rtv == 0:
			value = 'Successful'
		elif rtv == -1:
			value = 'Mdio error'
		else:
			value = 'Failed'
		print '%25s   %s' % (name, value)
		name = 'CPU status'
		rtv = self.usb.lib.ReadCPUStatus()
		if rtv == 1:
			value = 'Running'
		else:
			value = 'Stop'
		print '%25s   %s' % (name, value)


	def DumpFullRegAll(self, macro, lane_num):
		HB_base = [
			0x2000, 0x2100, 0x2200, 0x2300,
			0x2500, 0x2600, 0x2700, 0x2800,
			0x3000, 0x3100, 0x3200, 0x3300,
			0x3500, 0x3600, 0x3700, 0x3800
		]
		lanes = self.get_lanes(macro, lane_num)
		length = 0x100*len(lanes)
		value_list = (c.c_uint16*length)()
		self.usb.lib.DumpFullRegAll(macro, lane_num, value_list)
		for i in range(length):
			lane = i / 0x100
			offset = i % 0x100
			if offset == 0:
				sys.stdout.write('\n')
				sys.stdout.write('        ')
				for j in range(0x10):
					sys.stdout.write('%6x '% j)
			if offset % 0x10 == 0:
				sys.stdout.write('\n')
				sys.stdout.write('0x%04X: ' % (HB_base[lanes[lane]]+offset))
			sys.stdout.write('0x%04X ' % value_list[i])
		sys.stdout.flush()

	def LoadScript(self, path):
		self.usb.lib.LoadScript(c.c_char_p(path))

	def LoadFirmware(self, path):
		return self.usb.lib.LoadFirmware(c.c_char_p(path))

	def ReadFirmwareStatus(self):
		return self.usb.lib.ReadFirmwareStatus()

	def ReadCPUStatus(self):
		return self.usb.lib.ReadCPUStatus()

if __name__ == "__main__":
	falcon = Falcon_lib()
	
	try:
		print "%x"%falcon.Falcon_Read_PRBS_cntr(1)
		print "%x"%falcon.Falcon_Read_F1(1)
		print "%x"%falcon.Falcon_Read_F2(1)
		print "%x"%falcon.Falcon_Read_F3(1)
		for i in range(1):
			print falcon.Falcon_Read_DTL_RX(1)
		a = falcon.Falcon_multiple_DTL_read_RX(1,7)
		print a
		falcon.MdioWr(0x9814, 0x1234)
		#falcon.Falcon_SetStateBreakPoints_RX(0, 0, 1)
		print '%x'%falcon.MdioRd(0x800b)

		ret = falcon.Falcon_EM(10 ** 8, 3)

		import numpy as np
		import numpy.ctypeslib as clib
		x = clib.as_array(ret[0])
		y = clib.as_array(ret[1])
		cm = clib.as_array(ret[2])
		cm = np.transpose(cm)
		print cm.shape
		import matplotlib.pyplot as plt
		plt.pcolor(x, y, cm, cmap = 'jet')
		plt.show()

	finally:

		del falcon

