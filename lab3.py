#importing libraries.
import os
#Executing dir command.
os.system('dir')
#Asking for user input.
enter_username = input("Please enter your username: ")
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