#Importing subprocess and sys libs.
import subprocess
import sys
#Assigning a variable the output of netstat -ano.
output = subprocess.Popen(['netstat', '-ano'], stdout=subprocess.PIPE).communicate()
#Reading index 0 and inserting a newline char plus a carraige return.
