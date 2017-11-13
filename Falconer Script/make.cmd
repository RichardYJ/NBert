cl lib.c /c /I"C:/pthreads-w32-2-9-1-release/Pre-built.2/include"
link /def:lib.def /dll lib.obj /LIBPATH:"C:/pthreads-w32-2-9-1-release/Pre-built.2/lib/x86" pthreadVC2.lib
