#Importing library.
import scapy
import ipaddress

#Creating a list of ports to scan.
ports = [25, 80, 53, 443, 445, 8080, 8443]
#Begin creating a function.
def SynScan(host):
    """
    A function that will carry out a Syn scan.
    """
    ans, unans = sr(
        IP(dst=host)/
        TCP(sport=33333,dport=ports,flags="S")
        ,timeout=2,verbose=0)
    print("Open ports at %s:" % host)
    for (s,r,) in ans:
        if s[TCP].dport == r[TCP].sport and r[TCP].flags=="SA":
            print(s[TCP].dport)