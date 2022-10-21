import os
import time
import subprocess
import sys
import argparse

# print current date 
currentDate = time.strftime("%d-%m-%Y-%H:%M:%S")
scanfile = "masscanOUT3"
portsandIP = "portsandIP.txt"
sortedPorts = "sortedPorts.txt"
onlyPorts = "onlyPorts.txt"
uPorts = "uniqPorts.txt"



### Rate ###
# How fast to scan, calculate max speed from network speed & cpu

def cleanBeforeRun():
    # Clean up old files before running
    # delete all files in the ports folder
    os.system("rm -rf ports")
    os.system("rm sortedPorts.txt")
    os.system("rm portsandIP.txt")
    os.system("rm uniqPorts.txt")
    os.system("rm paused.conf")
    pass


def nmapTest(ip, port):

    
    if len(sys.argv) == 2:
        os.system("nmap -sV -T4 " + ip)

    elif len(sys.argv) == 3:
        os.system("nmap -sV -T4 " + ip + " " + "-p " + port)

    
    os.system("nmap -sV -T4 " + ip + port)


def inputIps(ips): # take in from sysargs
    os.system("rm hosts2.txt")
    ## take in a input of different number strings which are ip addresses, and store them in a file
    with open ("hosts2.txt", "a+") as file:
        for ip in ips:
            file.write(ip + "\n")
        else :
            print("No IP addresses entered")

        
def discoveryScan():

    # Discovery Scan
    # masscan all ports on all hosts
    # Output number of open ports and IP addresses to a file
    # Run a screen instance
    date = time.strftime("%d-%m-%Y-%H:%M:%S") 
    os.system('masscan -iL hosts.txt -p1-65535 --max-rate 100000 -oX discoveryScan' + date + ' --wait 20')
    os.system('cp hosts.txt ' + "discoveryScan_" + date)


def masscanExecute():
    ports = "-p1-444"
    rate = "1000"
    print("Starting scan")
    os.system('masscan ' + '-iL hosts.txt ' + ports + ' --rate ' + rate + ' -oL ' + ' masscanOUT3 --wait 10')
   # os.system('cp masscanOUTXX2' + scanfile)
    # --source-ip 192.168.1.200. To make banners more persistent




# Create a file for each open port
def uniquePorts():
    print("Creating files for each port")
    os.system("awk '{ print $3 }' " + scanfile + " | sort -u -n > " + uPorts + "")
    if not os.path.exists('ports'):
        os.makedirs('ports')

    with open(uPorts, "r+") as f:
        if f.read(1):
            for line in f:
                filename = "ports/" + line.strip() + ".txt" # port filename
                os.system("touch " + filename) # create a file for each port
        else:
            print("Uports file is empty 1")
            sys.exit()


def parsefile(): # Takes input from masscan -oL file
    print("Parsing ports and IP addresses to corresponding files")
    with open (scanfile , "r+") as f: 
        if f.read(1):
            os.system("awk '{print $3 \" \" $4}' " + scanfile + "> '" + portsandIP + "'") # Store only the IP and port in a file
        else:
            print("File is empty 2")
            sys.exit()
    with open(portsandIP, "r+") as f:
        if f.read(1):
            os.system("sort -k1 -n -t ' ' " + portsandIP + " | awk 'NF' > '" + sortedPorts + "'") # Sort on the first column, and remove empty lines
        else:
            print("File is empty 3")
            sys.exit()


    with open(sortedPorts, "r+") as f:
        for line in f:

            port = line.split()[0] # Get the port
            ip = line.split()[1] # Get the IP

            #store the port and ip in a file named after the port
            filename = "ports/" + port + ".txt" 
            with open(filename, "a+") as f:
                f.write(ip + "\n")
        #else:
       #    print("File is empty 4")
        #    sys.exit()



def mostUsedPortOrder(): # Start nmap on the most used ports first
    ports = sortedPorts
    os.system("cat " + scanfile + "| awk '{print $3}' | sort | uniq -c | sort -nr | awk '{print $2}' > " + onlyPorts + "")
    



def nmapExecute(port):
    # run nmap on each of the port files. Starting with the most used port
    # nmap on the ports with banners found in the masscan output file to separate files for each port
    if not os.path.exists('outputs'):
        os.makedirs('nmap')

    with open (onlyPorts, "r+") as f:
        if f.read(1):
            for line in f:
                port = line.strip()
                hosts = "ports/" + port + ".txt"
                outputFile = "outputs/nmapOutput-" + port + ".xml"
                    
                os.system("nmap -sV -iL " + hosts + " -p " + port + " -oX " + outputFile)


    target_file = 'nmap_targets.txt'
    date = 0
    output_file = port + 'nmap.xml'
    print("Starting Nmap")
    os.system('nmap -sV -p' + port + ' -T4 -Pn --script=vulners -iL ' + target_file + ' -oL ' +  output_file)
    # Hissing Nmap scan -defeat-rst-ratelimit --host-timeout 23H --max-retries 1 
    # -O --osscan-guess





if __name__ == "__main__":
    
    ip = sys.argv[1]
    port = sys.argv[2]


    #cleanBeforeRun()

    # if there is 1 argument, run discovery scan
    if len(sys.argv) == 2:
        nmapTest(ip)

    elif len(sys.argv) == 3:
        nmapTest(ip, port)
    
    #discoveryScan()
    #masscanExecute()
    #nmapExecute()
    #uniquePorts()
    #parsefile()

 #   mostUsedPortOrder()

# Clean up files

