import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Ybhat\AppData\Local\Programs\Python\Python312\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Ybhat\AppData\Local\Programs\Python\Python312\tcl\tk8.6"

executables = [cx_Freeze.Executable("FAAS.py", base=base, icon="desktop.ico")]


cx_Freeze.setup(
    name = "Face Authentication-Based Attendace System",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["desktop.ico",'tcl86t.dll','tk86t.dll', 'college_images','photos','database','Attendance_Report']}},
    version = "1.0",
    description = "Face Authentication-Based Attendace System | Developed by Yogesh Bhattarai",
    executables = executables
    )