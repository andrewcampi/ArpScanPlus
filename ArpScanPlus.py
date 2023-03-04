import argparse, subprocess, socket, time 

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-I", "--interface", help="network interface name (e.g. en0)")
parser.add_argument("-o", "--sort", help="sort devices by IP address", action="store_true")
parser.add_argument("-l", "--removedotlan", help="remove .lan from hostnames", action="store_true")
parser.add_argument("-a", "--about", help="display the about menu", action="store_true")
args = parser.parse_args()


if args.about:
    # Display the help menu
    print(" ")
    print("---------------------------------------------------------------------------------------------------")
    print(" █████╗ ██████╗ ██████╗     ███████╗ ██████╗ █████╗ ███╗   ██╗    ██████╗ ██╗     ██╗   ██╗███████╗")
    print("██╔══██╗██╔══██╗██╔══██╗    ██╔════╝██╔════╝██╔══██╗████╗  ██║    ██╔══██╗██║     ██║   ██║██╔════╝")
    print("███████║██████╔╝██████╔╝    ███████╗██║     ███████║██╔██╗ ██║    ██████╔╝██║     ██║   ██║███████╗")
    print("██╔══██║██╔══██╗██╔═══╝     ╚════██║██║     ██╔══██║██║╚██╗██║    ██╔═══╝ ██║     ██║   ██║╚════██║")
    print("██║  ██║██║  ██║██║         ███████║╚██████╗██║  ██║██║ ╚████║    ██║     ███████╗╚██████╔╝███████║")
    print("╚═╝  ╚═╝╚═╝  ╚═╝╚═╝         ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝     ╚══════╝ ╚═════╝ ╚══════╝")
    print("---------------------------------------------------------------------------------------------------")
    print("Arp-Scan+ : ")
    print("    Discover devices on your network.")
    print("Requirements : ")
    print("    - python3")
    print("    - arp-scan")
    print("Additions to Arp-Scan :")
    print("    - Sort devices by IP address.")
    print('    - Display the device hostname (with or without ".lan".')
    print("Usage:")
    print("    To use this tool with the default arguments, simply run (as root):")
    print("    $    python3 ArpScanPlus.py")
    print('    To use a certain NIC (e.g. "en0"):')
    print("    $    python3 ArpScanPlus.py -I en0")
    print("    To display the devices in order:")
    print("    $    python3 ArpScanPlus.py -o")
    print('    To display the hostnames without ".lan":')
    print('    $    python3 ArpScanPlus.py -l')
    print('    You can combine these options (e.g. use NIC "en0" and display devices in order without ".lan"):')
    print("    $    python3 ArpScanPlus.py -I en0 -o -l")
    print("Help Menu:")
    parser.print_help()

else:
    # Build arp-scan command
    command = "arp-scan -l"
    if args.interface:
        command += " -I " + args.interface
    # Run arp-scan command and get output
    output = subprocess.getoutput(command)
    # Parse output and create list of dictionaries
    devices = []
    for line in output.splitlines():
        if line.startswith("Interface:"):
            print(" ")
            print(line)
        if line.startswith("Starting arp-scan"):  # skip over non-device lines
            continue
        fields = line.split("\t")
        if len(fields) != 3:  # skip over malformed lines
            continue
        ip, mac, manufacturer = fields
        devices.append({"ip": ip, "mac_address": mac, "manufacturer": manufacturer})
    # Display the header
    print(" ")
    print("{:<18} {:<25} {:<25} {:<25}".format("IP Address", "Hostname", "Manufacturer", "MAC Address"))
    print("-" * 93)
    # Perform nslookup for each device and add hostname to dictionary
    for device in devices:
        try:
            hostname = socket.gethostbyaddr(device["ip"])[0]
            if args.removedotlan:
                if hostname.endswith(".lan"):
                    hostname = hostname[:-4]
        except socket.herror:
            hostname = "(Unknown)"
        device["hostname"] = hostname
    # Sort devices by IP address if specified
    if args.sort:
        devices = sorted(devices, key=lambda d: [int(octet) for octet in d["ip"].split(".")])
    # print the results
    for device in devices:
        time.sleep(0.01)
        print("{:<18} {:<25} {:<25} {:<25}".format(device["ip"], device["hostname"], device["manufacturer"], device["mac_address"]))
    print(" ")
    print("Detected Devices:", len(devices))
    print(" ")
