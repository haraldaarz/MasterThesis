import os
import time
import subprocess
import sys

# Program to scan computers from a list. Ran by Docker containers which are spawned by the main.py


### User agent
# Leave user agent tag
# --http-user-agent uio-lab-masscan-scanner
# https://www.mn.uio.no/ifi/english/research/networks/securitylab/
# https://www.mn.uio.no/ifi/english/research/groups/sec/


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



def discoveryScan():

    # Discovery Scan
    # masscan all ports on all hosts
    # Output number of open ports and IP addresses to a file
    # Run a screen instance

    date = time.strftime("%d-%m-%Y-%H:%M:%S") 
    os.system('masscan -iL hosts.txt -p1-65535 --max-rate 100000 -oX discoveryScan' + date + ' --wait 1')

    pass

    

def masscanExecute():
    ports = "-p1-444"
    rate = "10000"
    print("Starting scan")
    os.system('masscan ' + '-iL hosts.txt ' + ports + ' --max-rate ' + rate + ' -oL ' + ' masscanOUTXX --wait 1')
    # --source-ip 192.168.1.200. To make banners more persistent




def nmapExecute(port):
    # nmap on the ports with banners found in the masscan output file to separate files for each port
    target_file = 'nmap_targets.txt'
    date = 0
    output_file = port + 'nmap.xml'
    print("Starting Nmap")
    os.system('nmap -sV -p' + port + ' -T4 -Pn --script=vulners -iL ' + target_file + ' -oL ' +  output_file)
    # Hissing Nmap scan -defeat-rst-ratelimit --host-timeout 23H --max-retries 1 
    # -O --osscan-guess



scanfile = "scan.txt"
portsandIP = "portsandIP.txt"
sortedPorts = "sortedPorts.txt"
outtt = "outtt.txt"
uPorts = "uniqPorts.txt"


# Create a file for each open port
def uniquePorts(scanfile, uPorts):
    os.system("awk '{ print $3 }' " + scanfile + " | sort -u -n > " + uPorts + "")
    if not os.path.exists('ports'):
        os.makedirs('ports')

    with open(uPorts, "r+") as f:
        if f.read(1):
            for line in f:
                filename = "ports/" + line.strip() + ".txt" # port filename
                os.system("touch " + filename) # create a file for each port
        else:
            print("File is empty")
            sys.exit()


def parsefile(scanfile, portsandIP, sortedPorts):
    with open (scanfile , "r+") as f: 
        if f.read(1):
            os.system("awk '{print $3 \" \" $4}' " + scanfile + "> '" + portsandIP + "'") 
        else:
            print("File is empty")
            sys.exit()
    with open(portsandIP, "r+") as f:
        if f.read(1):
            os.system("sort -k1 -n -t ' ' " + portsandIP + " | awk 'NF' > '" + sortedPorts + "'") # Sort on the first column, and remove empty lines

        else:
            print("File is empty")
            sys.exit()

    with open(sortedPorts, "r+") as f:
        if f.read(1):
            for line in f:
                port = line.split()[0]
                ip = line.split()[1]
                # store the port and ip in a file named after the port
                filename = "ports/" + port + ".txt"
                with open(filename, "a+") as f:
                    f.write(ip + "\n")


        else:
            print("File is empty")
            sys.exit()





def mostUsedPortOrder():
    pass




uniquePorts(scanfile, uPorts)
parsefile(scanfile, portsandIP, sortedPorts)

if __name__ == "__main__":
    
    cleanBeforeRun()
    masscanExecute()
    masscanParse()
    nmapExecute()
# Clean up files

