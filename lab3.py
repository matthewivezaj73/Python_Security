#importing libraries.
import os
import subprocess, sys
#Asking for user input.
enter_username = input("Please enter your username: ")
#Formatting a string to change into the desktop.
my_path = f"C:/Users/{enter_username}/Destop"
#Executing dir command.
os.system('dir')

#Executing dir command.
os.system('dir')
#Asking for the path.
path = input("Please enter your path: ")
#Executing cd to desktop command.
os.chdir(path)
#Executing dir command.
os.system('dir')
#Executing systeminfo command.
os.system('systeminfo >sysinfo.txt')
#Executing dir command.
os.system('dir')
#Executing hostname command.
os.system('hostname')
#Executing tasklist command.
os.system('tasklist.exe > tasklist.txt')
#Executing tasklistSVC command.
os.system('tasklist.exe /SVC > tasklistSVC.txt')
#Executing Query user command.
os.system('query user')
#Running a powershell script from the desktop.
output_script = subprocess.Popen(["powershell.exe", "C:\\Users\\Monty\\Desktop\\powershell_script.ps1"], stdout=sys.stdout)
output_script.communicate()
#Error, will need to import subprocess to use Powershell...



#Executing GetEventLog –list .
# os.system('GetEventLog –list')