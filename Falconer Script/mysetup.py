from cx_Freeze import setup, Executable

build_exe_options = {'include_files': ['falcon_api.dll', 'falcon_lib.py', 'Falcon_CHRIS2.txt'],
                     'include_msvcr': True,
                     'excludes': ['curses', 'distutils', 'email', 'importlib', 'logging', 'multiprocessing',
                                  'numpy', 'pkg_resources', 'pydoc_data', 'setuptools', 'unittest', 'xml']}

base = 'Win32GUI'

setup(name=u"Falconer",
      version="0.1",
      description=u"Credo QSFP-SFP Tester",
      options={'build_exe': build_exe_options},
      author=u"Marc Xu",
      executables=[Executable('Falcon_GUI.py', base=base, targetName='Credo_Falconer.exe')])
