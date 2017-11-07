import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"
    options = {
        'build_exe': {
            'build_exe': 'Credo Falconer',
            'includes': [],
            'excludes': ['PyQt4', 'curses', 'distutils', 'email', 'importlib', 'logging', 'xml',
                         'multiprocessing', 'numpy', 'pkg_resources', 'pydoc_data', 'setuptools', 'unittest'],
            'include_msvcr': True,
            'include_files': ['falcon_api.dll'],
        },
        'install_exe': {
            'install_dir': ['Credo Falconer'],
            'build_dir': ['Falconer GUI'],
            'force': True
        }

    }
else:
    options = {
        'build_exe': {
            'include_files': [('eagle_api.so', 'eagle_api.so', 'Falcon_CHRIS2.txt')],
        },
        'install_exe': {'install_dir': 'Credo Falconer',
                        'build_dir': 'Falconer GUI',
                        'force': True
                        }
    }

setup(
    name=[u"Credo_Falconer"],
    version="0.1",
    description=u"Credo QSFP-SFP Tester",
    executables=[Executable(
        'Falcon_GUI.py',
        base=base,
        targetName="Credo_Falconer.exe"
    )],
    options=options
)
