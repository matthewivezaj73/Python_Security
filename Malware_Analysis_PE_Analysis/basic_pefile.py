#Import libraries
import pefile
pe = pefile.PE("/home/monty/Desktop/malware_data_science_entrypoints_redacted/malware_data_science/ch2/ircbot.exe")
#Parsing the executable.
for section in pe.sections:
    malicious_output = section.Name,hex(section.VirtualAddress), hex(section.Misc_VirtualSize), section.SizeOfRawData
    print(malicious_output)