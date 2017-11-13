rd /s /q build
rd /s /q dist
del *.exe
;pyinstaller -D -w -p C:\Python27\Lib; MainApp.py
;pyinstaller -F -w -p C:\Python27\Lib; MainApp.py
pyinstaller -D --console -p C:\Python27\Lib; MainApp.py
pyinstaller -F --console -p C:\Python27\Lib; MainApp.py -i credo.ico
timeout /t 1 /nobreak
copy dist\MainApp.exe .\MainApp.exe
rd /s /q build
rd /s /q dist
