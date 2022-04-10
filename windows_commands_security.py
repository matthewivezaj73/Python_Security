#Importing subprocess and sys libs.
import subprocess
import sys
#Assigning a variable the output of netstat -ano.
output = subprocess.Popen(['netstat', '-ano'], stdout=subprocess.PIPE).communicate()
#Reading index 0 and inserting a newline char plus a carraige return.
newlines = str(output[0]).split('\r\n')  
#Running through each line in the newlines variable and printing based off of certain criteria.
for line in newlines:
    if line.find("Foreign") != -1:
        print(line)
    if line.find("ESTABLISHED") != -1:
        print(line)