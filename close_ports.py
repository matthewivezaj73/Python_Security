#Importing subprocess and sys libs.
import subprocess
import sys
import os
#Assigning a variable the output of netstat -ano.
os.system('netstat -ano')
#Reading index 0 and inserting a newline char plus a carraige return.
