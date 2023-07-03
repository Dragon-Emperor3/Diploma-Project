import sys
from cx_Freeze import setup,Executable

build_exe_options={"packages":["os"],"excludes":["Tkinter"]}

base=None
if sys.platform=="win32":
    base="Win32GUI"

setup(name="Face-Detect",
      version="1.0.0",
      author='6_boys_group',
      description="My Gui Application",
      options={"build_exe":build_exe_options},
      executables=[Executable('GUI.py',base=base,shortcutName="Face-Detect",shortcutDir="DesktopFolder")])
#,icon=r"C:\Users\sunny\Desktop\Project_Attendance\pictures\guifoo.ico"