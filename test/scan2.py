# Take in 2 arguments, a IP address and a port range
# Scan the IP address for open ports in the given range
# Print the open ports
# Usage: ./scan.py

import sys
import subprocess
import shlex

# Check for correct number of arguments


# Get the IP address and port range
ip = sys.argv[1]
port_range = sys.argv[2]

# Split the port range into a list
ports = port_range.split("-")


# run the nmap command. Take in the IP address and port range

def run_nmap(ip, port_range):
    nmap_command = "nmap -p {} {}".format(port_range, ip)
    args = shlex.split(nmap_command)
    return subprocess.check_output(args).decode("utf-8")

# run the nmap command and store the output
nmap_output = run_nmap(ip, port_range)


# print the open ports
def print_open_ports(nmap_output):
    print("Open ports:")
    for line in nmap_output.splitlines():
        if "open" in line:
            print(line)

print_open_ports(nmap_output)

