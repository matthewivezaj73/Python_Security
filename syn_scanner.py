#Importing library.
from scapy import *
import ipaddress

#Creating a list of ports to scan.
ports = [25, 80, 53, 443, 445, 8080, 8443]