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