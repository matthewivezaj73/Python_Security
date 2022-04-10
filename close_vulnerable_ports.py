#Importing os library.
import os
print(os.system('cmd /k "netstat -ano | findstr :22"'))
#Terminating a port.
os.system('cmd /k "taskkill /pid 12012"')