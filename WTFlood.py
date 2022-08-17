#!/usr/bin/env python3
import sys
try:
	from scapy.all import *
except ImportError as Error:
	print("Failed to import library - {}".format(Error))
	print("Please check if needed libararies are installed, or run the installer once more.")
	sys.exit(1)

__version__ = "V0.1.0.0A"

if __name__ "__main__":
	print("Test")
