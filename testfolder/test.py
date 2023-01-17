###### THIS FILE IS NOT THE FINAL VERSION ###### 
# IT HAS SOME REALLY SIMILAR CODE TO scan.py, HOWEVER THAT FILE IS MORE RECENT.

import os
import sys

# Files
scanfile = "scan.txt"
portsandIP = "portsandIP.txt"
sortedPorts = "sortedPorts.txt"
onlyPorts = "onlyPorts.txt"
uPorts = "uniqPorts.txt"
time = os.system("date +%s")

def startCleanUp():
    os.system("rm -r ports")
    os.system("rm -r outputs")

def uniquePorts(scanfile, uPorts): # Create a file for each open port
    os.system("awk '{ print $3 }' " + scanfile + " | sort -u -n > " + uPorts + "")
    if not os.path.exists('ports'):
        os.makedirs('ports')
    with open(uPorts, "r+") as f:
        for line in f:
            filename = "ports/" + line.strip() + ".txt" # port filename
            os.system("touch " + filename) # create a file for each port

def parsefile(scanfile, portsandIP, sortedPorts): # Takes input from masscan -oL file, and save the IPs to correct port file
    with open (scanfile , "r+") as f: 
        os.system("awk '{print $3 \" \" $4}' " + scanfile + "> '" + portsandIP + "'") # Store only the IP and port in a file
    with open(portsandIP, "r+") as f:
        os.system("sort -k1 -n -t ' ' " + portsandIP + " | awk 'NF' > '" + sortedPorts + "'") # Sort on the first column, and remove empty lines
    with open(sortedPorts, "r+") as f:
        if f.read(1):
            for line in f:
                port = line.split()[0] # Get the port number
                ip = line.split()[1] # Get the IP
                filename = "ports/" + port + ".txt" 
                with open(filename, "a+") as f:
                    f.write(ip + "\n") # Write the IP to the correct port file
        else:
            print("Portfile does not exist")
            sys.exit()


def mostUsedPortOrder(): # Start nmap on the most used ports first
    ports = sortedPorts
    os.system("cat " + scanfile + " | sed '/^$/d' | awk '{print $3}' | sort | uniq -c | sort -nr | awk '{print $2}' > " + onlyPorts + "") # Sort on most used port.
    

def countPorts(): # Count the amount of ports that are open from the ports files
    totalPorts = os.system("cat ports/* | wc -l")
    return totalPorts


def nmapExecute():
    if not os.path.exists('outputs'):
        os.makedirs('outputs')  # Create a folder for the output files
    with open (onlyPorts, "r+") as f:
        if f.read(1):
            for line in f:
                port = line.strip()
                hosts = "ports/" + port + ".txt"
                outputFile = "outputs/nmapOutput-" + port + ".xml"
                os.system("sudo nmap --open -Pn  -sV -O --open --osscan-limit -T4 -script=banner -iL " + hosts + " -p " + port + " -oX " + outputFile + "")


def endCleanUp():
    os.system("sleep 1")
    os.system("rm " + portsandIP)
    os.system("rm " + sortedPorts)
    os.system("rm " + onlyPorts)
    os.system("rm " + uPorts)
    # if a output file does not contain any host information, delete the file




startCleanUp()
uniquePorts(scanfile, uPorts)
parsefile(scanfile, portsandIP, sortedPorts)

mostUsedPortOrder()

nmapExecute()

#endCleanUp()

time2 = os.system("date +%s")
timeElapsed = time2 - time
print("Time elapsed: " + str(timeElapsed))

# nmap -n -sP -T5 --min-parallelism 100 --max-parallelism 256 -iL ips_list.txt | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" > live_hosts.txt
