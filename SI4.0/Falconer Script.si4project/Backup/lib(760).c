//#pragma comment (dll, "falcon_api.dll")

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <pthread.h>
//typedef int FUNADDR;
typedef int(*FUNADDR)();
//typedef int (*FUNADDR2)();
#define USE_VSTHREAD 1
#if USE_VSTHREAD
DWORD WINAPI test1(LPVOID lpParameter)

{
	printf("test1\n");
	return 0;
}

DWORD WINAPI test2(LPVOID lpParameter)

{
	printf("test2\n");
	return 0;
}

#else
void test1(void)
{
	printf("test1\n");
	return ;
}

void test2(void)
{
	printf("test2\n");
	return ;
}
#endif

int test()
{
	HINSTANCE dllDemo=NULL;
	FUNADDR read8i2c;
	FUNADDR write8i2c;
  	int i,j,ret,iled = 0;
  	short ioDir,ioDataH,ioDataL,ioData;
#if USE_VSTHREAD
	HANDLE handle1,handle2;
#else
	pthread_t id_1,id_2;
#endif

	printf("test lib ============= start\n");
#if USE_VSTHREAD	
	handle1=CreateThread(NULL,0,test1,NULL,0,NULL);
	handle2=CreateThread(NULL,0,test2,NULL,0,NULL);

	if(!handle1||!handle2)
		printf("CreateThread Error!");
	CloseHandle(handle1);
	CloseHandle(handle2);
#else
	ret=pthread_create(&id_1,0,(void *)test1,0);
	ret=pthread_create(&id_2,0,(void *)test2,0);
#endif
	
	dllDemo = LoadLibrary("falcon_api.dll");


	if(dllDemo)
	{
		read8i2c = (FUNADDR)GetProcAddress(dllDemo,"cr_read_i2c_AC_8");
		write8i2c = (FUNADDR)GetProcAddress(dllDemo,"cr_write_i2c_AC_8");
	}
	

	write8i2c(0x1, 0x00, 0x20);
//  write8i2c(0x13, iled, 0x20);
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
	  }
	}
	write8i2c(0x13,iled, 0x20);

	printf("test lib ============= end\n");

	FreeLibrary(dllDemo);

#if USE_VSTHREAD

#else
	pthread_exit(0);
#endif

	return 0;
}
