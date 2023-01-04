https://img.shields.io/github/languages/code-size/WTechnologyDevelopers/WTFlood
## Introduction
WTFlood is a network tool designed to testing networks against MAC-Flooding Attack / CEM Overflow Attack. The tool sends a constant
stream of random network data from random IP Addresses, and with random MAC Addresses to force the target switch to fill it's 
MAC Address Table to the memory limit, to force the switch to send all the network traffic over all it's interfaces.

WTFlood uses a burst of a select numbers of network packets to fill the CEM buffer on the switch, the number of packets generated
between each burst will determine the time between each burst.

### Disclaimer
WTechnology as a company and it's developers are not responsible for any misuse of the "WTFlood" network tool. The "WTFlood" network tool
is designed for the purpose of testing your **OWN** network!

## Installation
The installation process should be fairly simple, just download the package from the WTechnology GitHub, unzip it, and run the
**install.sh** install script.

### wget installation
if you have wget package installed on your system, then use this installation method:
```bash
$ wget https://github.com/WTechnologyDevelopers/WTFlood/archive/refs/heads/master.zip
$ unzip master.zip
$ cd WTFlood-master/
$ sudo bash install.sh
```

### curl installation
if you have curl package installed on your system, then use this installation method:
```bash
$ curl https://github.com/WTechnologyDevelopers/WTFlood/archive/refs/heads/master.zip
$ unzip master.zip
$ cd WTFlood-master/
$ sudo bash install.sh
```

## Usage Example
**WTFlood with automatic selected interface.**
WTFlood usage without any arguments, WTFlood picks a active interface to use.
```bash
WTFlood
```

**WTFlood with selected interface.**
WTFlood usage with both selected interface, and in verbose logging mode.
```bash
WTFlood -i wlo1 -v
```

**WTFlood Help.**
WTFlood usage with the "help" argument, this show the different arguments to input to the tool.
```bash
WTFlood -h
```
