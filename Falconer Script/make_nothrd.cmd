cl lib_nothrd.c /c /I"C:/pthreads-w32-2-9-1-release/Pre-built.2/include"
link /def:lib_nothrd.def /dll lib_nothrd.obj /LIBPATH:"C:/pthreads-w32-2-9-1-release/Pre-built.2/lib/x86" pthreadVC2.lib
