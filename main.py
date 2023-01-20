import subprocess
import os
import sys
import requests
import csv
#import docker
#pip3 install docker-compose
# from the file scan import *


# Main program to controll Docker containers, and logging

#### Consts


def installDependencies():
    os.system('apt install python3-pip')
    # if os.system('masscan --regres) returns [hint]: you must install libpcap or WinPcap
        # then os.system('apt install libpcap-dev -y)
    pass


def prepearInterface():
    os.system('iptables -A INPUT -i eth0 -p tcp --dport 44444 -j DROP')



def getIPs():
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



def startContainer()
    os.system("sudo docker run -v $(pwd)/results:/outputs security_lab_robot_scanner") # & 80 213.187.160.0/22  



def moveScanResults()
    os.system("mv /results/* /elk_nmap/import/")


def startIngestorContainer()
    os.system("docker-compose run ingestor")


def main():
    getIPs()
    


# Before running the scan, create or delete all of the files in the folder "results"
# after scanning, ingest all the files from the folder "results" into the elastic database



# main
if __name__ == "__main__":
    main()
