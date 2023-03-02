import subprocess
import os
import sys
import requests
import csv
#import docker
#pip3 install docker-compose
# from the file scan import *


# Main program to controll Docker containers, and logging


def installDependencies():
    os.system('apt update -y && sudo apt upgrade -y')
    os.system('apt install docker.io docker-compose git -y')
    os.system('sudo usermod -aG docker ${USER}')
    os.system('git clone https://github.com/bennettwarner/elk_nmap')
    os.system('git clone https://github.com/haraldaarz/MasterThesis')
    # Web interface
    # git clone or cd and docker-compose up -d



def prepearInterface():
    os.system('iptables -A INPUT -i eth0 -p tcp --dport 44444 -j DROP')


def getIPs(): # Gets all of the IP adresses in Norway to a list
    response = requests.get("https://www.nirsoft.net/countryip/no.csv")
    reader = csv.reader(response.text.splitlines())
    ip_data = {}
    for row in reader:
        try:
            # Extract the IP range and amount from the row
            ip_range = row[0] + "-" + row[1]
            amount = row[2]

            # Add the IP range and amount to the dictionary
            ip_data[ip_range] = amount
        except IndexError:
            # Handle the error here
            pass

    # Write the IP ranges to the hosts.txt file
    with open("allhosts.txt", "w") as f:
        for ip_range, amount in ip_data.items():
            f.write(ip_range + "\n")

    # Calculate the total number of IPs
    total_ips = sum(int(amount) for amount in ip_data.values())
    print("Total IPs:", total_ips)


def buildContainer():
    print("Building the scanner container""")
    os.system("docker build . -t security_lab_robot_scanner --no-cache")
    
def startWebServer():
    # Start the django web server
    os.system("python3 manage.py runserver")


def elastic():
    os.system("cd elk_nmap")
    os.system("docker-compose up -d")
    # run a scan, and then run the ingestor
    # after ingesting, visit IP:5601, 
    # add index pattern, *nmap*
    # copy dashboard template
    pass

def main():
    getIPs()


if __name__ == "__main__":
    main()
