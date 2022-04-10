#Importing subprocess and sys libs.
import subprocess
import sys
#Assigning a variable the output of netstat -ano.
output = subprocess.Popen(['netstat', '-ano'], stdout=subprocess.PIPE).communicate()

newlines = str(output[0]).split('\r\n')  
for line in newlines:
    if line.find("Foreign") != -1:
        print(line)
    if line.find("ESTABLISHED") != -1:
        print(line)