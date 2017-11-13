//#pragma comment (dll, "falcon_api.dll")

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

//typedef int FUNADDR;
typedef int(*FUNADDR)();
//typedef int (*FUNADDR2)();


int test()
{
	HINSTANCE dllDemo=NULL;
	FUNADDR read8i2c;
	FUNADDR write8i2c;
  int i,j,iled = 0;
  short ioDir,ioDataH,ioDataL,ioData;
	dllDemo = LoadLibrary("falcon_api.dll");
#if 1
	printf("test lib ============= start\n");
#endif

	if(dllDemo)
	{
		read8i2c = (FUNADDR)GetProcAddress(dllDemo,"cr_read_i2c_AC_8");
		write8i2c = (FUNADDR)GetProcAddress(dllDemo,"cr_write_i2c_AC_8");
	}
	

  write8i2c(0x1, 0x00, 0x20);
  write8i2c(0x13, iled, 0x20);
#if 1
  for(i=0;i<0x6;i++)
  {
      j=0x01<<i;
      ioDir=read8i2c(j,0x70);           //#config I2C channel
      write8i2c(0x4A, 0x00, 0x50);
      write8i2c(0x4B, 0x00, 0x50);
      write8i2c(0x4E, 0x01, 0x50);
      ioDataH=read8i2c(0x4C,0x50);
      ioDataL=read8i2c(0x4D,0x50);
      ioData = ioDataH<<8|ioDataL;
      if(0x204C==ioData)
      {
      	  iled |= j;
          write8i2c(0x13,iled, 0x20);
      }
  }
#endif


	printf("test lib ============= end\n");

	return FreeLibrary(dllDemo);
}