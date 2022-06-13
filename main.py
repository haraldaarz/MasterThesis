import subprocess
import os
import sys
import docker
#pip3 install docker-compose


# Main program to controll Docker containers, and logging

#### Consts


def installDependencies():
    os.system('apt install python3-pip')
    # if os.system('masscan --regres) returns [hint]: you must install libpcap or WinPcap
        # then os.system('apt install libpcap-dev -y)
    pass

def checkForGitUpdate():
    if os.path.exists("MasterThesis"):
        print("Folder exists")
        os.system('cd MasterThesis && git pull')
    else:
        print("Folder does not exist")
        os.system('git clone xxx') # Clone repo
    

def prepearInterface():
    os.system('iptables -A INPUT -i eth0 -p tcp --dport 44444 -j DROP')




def getIPs():
    os.system('curl -s https://www.nirsoft.net/countryip/no.csv > scanme.csv') # Get IPs from nirsoft
    with open ("scanme.csv", "r+") as f:
        for line in f:
            ip1 = (line.split(',')[0])
            ip2 = (line.split(',')[1])
            amount = (line.split(',')[2])
            ipRange = ip1 + "-" + ip2
            print(ipRange)
            with open("hosts.txt", "a") as f:
                f.write(ipRange + "\n")
        print("Total IPs:", amount)

def masscan():
    # Start the masscan container
    pass








def main():
    getIPs()
    


# main
if __name__ == "__main__":
    main()
