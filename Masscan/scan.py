import os
import time
import subprocess
import sys

# Program to scan computers from a list. Ran by Docker containers which are spawned by the main.py


### User agent
# Leave user agent tag
# --http-user-agent uio-lab-masscan


### IPs ###
# Get IPs from file, and parse it in as an argument
# hosts.txt

### Ports ###
# Use most common ports
## https://nullsec.us/top-1-000-tcp-and-udp-ports-nmap-default/
# Mode to check all ports
#    Mabye do some comparisons

### Rate ###
# How fast to scan
# Calculate max speed from network speed & cpu


### Exclude ###
# Excluded IP ranges


def cleanBeforeRun():
    if os.path.exists("nmap.xml"):
        os.remove("nmap.xml")

    if os.path.exists("nmap_targets.txt"):
        os.remove("nmap_targets.txt")

    if os.path.exists("masscan"):
        os.remove("nmap_targets.txt")


def masscanExecute():
    ports = "-p1-444"
    rate = "10000"
    print("Starting scan")
    os.system('masscan ' + '-iL hosts.txt ' + ports + ' --max-rate ' + rate + ' -oX ' + ' masscanOUTXX --wait 1')

def masscanParse():

    # If file is not empty

    with open ("masscanOUTXX" , "r+") as f:
        if f.read(1):
            print("File is not empty")

            with open("masscanOUTXX") as origin, \
                open('nmap_targets.txt', mode='w') as out_file:

                for line in origin:
                    if "portid" in line:
                        # Prints out only the IP address from the masscan list
                        out_file.write(line.split('"')[3]+"\n")
            print("Done parsing")

        else:
            print("Masscan output file is empty")
            sys.exit()


def nmapExecute():
    target_file = 'nmap_targets.txt'
    output_file = 'nmap.xml'
    open_ports = ' 1-400'
    print("Starting Nmap")
    os.system('nmap -sV -p' + open_ports + ' -T4 -Pn --script=vulners -iL ' + target_file + ' -oX ' +  output_file)
    # Hissing Nmap scan -defeat-rst-ratelimit --host-timeout 23H --max-retries 1 
    # -O --osscan-guess


def generateHtml():
    os.system('xsltproc -o scanme.html nmap-bootstrap.xsl nmap.xml')

if __name__ == "__main__":
    
    cleanBeforeRun()
    masscanExecute()
    masscanParse()
    nmapExecute()
# Clean up files