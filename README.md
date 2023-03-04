# Arp-Scan+  
    Discover devices on your network.
    
# Requirements  
    python3
    arp-scan
    
# Additions to Arp-Scan 
    Sort devices by IP address.
    Display the device hostname (with or without ".lan".
    
# Usage
    To use this tool with the default arguments, simply run (as root):
    -    python3 ArpScanPlus.py
    To use a certain NIC (e.g. "en0"):
    -    python3 ArpScanPlus.py -I en0
    To display the devices in order:
    -    python3 ArpScanPlus.py -o
    To display the hostnames without ".lan":
    -    python3 ArpScanPlus.py -l
    You can combine these options (e.g. use NIC "en0" and display devices in order without ".lan"):
    -    python3 ArpScanPlus.py -I en0 -o -l
    
# Help Menu
usage: ArpScanPlus.py [-h] [-I INTERFACE] [-o] [-l] [-a]

options:
  - h, --help            show this help message and exit
  - I INTERFACE, --interface INTERFACE
                        network interface name (e.g. en0)
  - o, --sort            sort devices by IP address
  - l, --removedotlan    remove .lan from hostnames
  - a, --about           display the about menu
