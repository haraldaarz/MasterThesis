import os
import time
import sys
import argparse

# print current date 
currentDate = time.strftime("%d-%m-%Y-%H:%M:%S")
scanfile = "masscanOUT3.txt"
portsandIP = "portsandIP.txt"
sortedPorts = "sortedPorts.txt"
onlyPorts = "onlyPorts.txt"
uPorts = "uniqPorts.txt"



### Rate ###
# How fast to scan, calculate max speed from network speed & cpu

def cleanBeforeRun():
    # Clean up old files before running

    if os.path.exists('ports'):
        os.system("rm -rf ports")
    if os.path.exists('sortedPorts.txt'):
        os.system("rm sortedPorts.txt")
    if os.path.exists('portsandIP.txt'):
        os.system("rm portsandIP.txt")
    if os.path.exists('uniqPorts.txt'):
        os.system("rm uniqPorts.txt")
    if os.path.exists('paused.txt'):
        os.system("rm paused.conf")
    if os.path.exists('onlyPorts.txt'):
        os.system("rm onlyPorts.txt")
    if os.path.exists('masscanOUT3.txt'):
        os.system("rm masscanOUT3.txt")

    
def cleanAfterRun():
    # Clean up old files after running
    if os.path.exists('sortedPorts.txt'):
        os.system("rm sortedPorts.txt")
    if os.path.exists('portsandIP.txt'):
        os.system("rm portsandIP.txt")
    if os.path.exists('uniqPorts.txt'):
        os.system("rm uniqPorts.txt")
    if os.path.exists('onlyPorts.txt'):
        os.system("rm onlyPorts.txt")
    if os.path.exists('masscanOUT3.txt'):
        os.system("rm masscanOUT3.txt")


def inputIps(ips): # Stores provided IP addresses in a file
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


def masscanExecute2(ports, rate):
    print("Starting masscan")
    os.system('masscan ' + '-iL hosts.txt -p' + ports + ' --rate ' + rate + ' -oL ' + ' masscanOUT3.txt --wait 20')


# Create a file for each open port
def uniquePorts():
    print("Creating files for each port")
    os.system("awk '{ print $3 }' " + scanfile + " | sort -u -n | grep '\S' | awk 'NF' >" + uPorts + "") # TODO : Remove empty lines under uniqPorts.txt
    print("Check 1")

    if not os.path.exists('ports'):
        os.makedirs('ports')
    with open(uPorts, "r+") as f:
       # if f.read(1): # Uncomment for testing 
        for line in f:
            filename = "ports/" + line.strip() + ".txt" # port filename
            if filename == "0.txt":
                print("A file with the name 0.txt is created")
            os.system("touch " + filename) # create a file for each port
            print("Created the file: " + filename)
            # if the file is empty, remove it
            if os.stat(filename).st_size == 0:
                os.remove(filename)
        #else: # Uncomment for testing 
          #  print("Uports file is empty 1") # Uncomment for testing 
         #   sys.exit() # Uncomment for testing 


def parsefile(): # Takes input from masscan -oL file
    print("Parsing ports and IP addresses to corresponding files")
    with open (scanfile , "r+") as f: 
        if f.read(1):
            os.system("awk '{print $3 \" \" $4}' " + scanfile + " | grep '\S' > '" + portsandIP + "'") # Store only the IP and port in a file
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
    print("Done parsing ports and IP addresses to corresponding files")


# Mulig jeg ikke trenger denne funksjonen
def mostUsedPortOrder(): # Start nmap on the most used ports first
    ports = sortedPorts
    os.system("cat " + scanfile + "| awk '{print $3}' | sort | uniq -c | sort -nr | awk '{print $2}' | grep '\S' > " + onlyPorts + "")
    
def nmapExecute():
    # run nmap on each of the port files. Starting with the most used port
    # nmap on the ports with banners found in the masscan output file to separate files for each port
    if not os.path.exists('outputs'):
        os.makedirs('outputs')

    print("Starting Nmap")

    with open (onlyPorts, "r+") as f:
        for line in f:
            print("Ports:", line)

            port = line.strip()
            hosts = "ports/" + port + ".txt"
            outputFile = "outputs/nmapOutput-" + port + ".xml"
                
            os.system("nmap -sV -T4 -Pn -n --open --script=vulners -iL " + hosts + " -p " + port + " -oX " + outputFile) #+ " >/dev/null")  # TODO Mabye dont dev/null
            # Hissing Nmap scan -defeat-rst-ratelimit --host-timeout 23H --max-retries 1 
            # -O --osscan-guess
    print("Done with Nmap")



if __name__ == "__main__":
    
    if len(sys.argv) == 2:
       port = sys.argv[1]
       masscanExecute2(port, "10000")

    if len(sys.argv) == 3:
        port = sys.argv[1]
        ips = sys.argv[2]
        with open("hosts.txt", "w+") as f:
            f.write(ips)
        masscanExecute2(port, "10000")

    if len(sys.argv) == 4:
        port = sys.argv[1]
        ips = sys.argv[2]
        rate = sys.argv[3]
        with open("hosts.txt", "w+") as f:
            f.write(ips)
        masscanExecute2(port, rate)

    #cleanBeforeRun()
    uniquePorts()
    parsefile()
    mostUsedPortOrder()
    nmapExecute()
    #cleanAfterRun()
    moveScanFiles()
    #discoveryScan()
