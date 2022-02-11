import os
import time
import subprocess


def masscanExecute():
    ports = "-p1-444"
    rate = "10000"
    print("Starting scan")
    os.system('masscan ' + '-iL hosts.txt ' + ports + ' --max-rate ' + rate + ' -oX ' + ' masscanOUTXX --wait 1')

def masscanParse():

    # Store Ports to list
    #open_ports = os.system('cat masscanOUTXX | grep portid | cut -d "\"" -f 10 | sort -n | uniq | paste -sd,')
    # Store IPs to file
    os.system('cat masscanOUTXX | grep portid | cut -d "\"" -f 4 | sort -V | uniq > nmap_targets.tmp')
    print("Done parsing")

#def nmap(open_ports):
    target_file = 'nmap_targets.tmp'
    output_file = 'nmap.xml'
    open_ports = '22,80,53,443'
    print("Starting Nmap")
    os.system('nmap -sV -p' + open_ports + ' -T4 -iL ' + target_file + ' -oX ' +  output_file)    


if __name__ == "__main__":
    
    masscanExecute()
    masscanParse()

   #parseMasscanReport()



