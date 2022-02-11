import subprocess
import os

# Program to scan computers from a list. Ran by Docker containers which are spawned by the main.py

# Check if a scan is currently running
# docker ps


### WORKING COMMANDS ####
# sudo masscan 137.74.187.0/24 -p 80 
# masscan --banners # For å få med versjoner 
# til fil: -oL
# --rate 100000000
##   Til testing: 10000 
# port: -p1-65535
# masscan 192.168.0.0/24 --top-ports --banners --rate 10000 -oX scan3.xml

### User agent
# Leave user agent tag
# --http-user-agent uio-lab-masscan


### IPs ###
# Get IPs from file, and parse it in as an argument


### Ports ###
# Use most common ports
## https://nullsec.us/top-1-000-tcp-and-udp-ports-nmap-default/
# Mode to check all ports
#    Mabye do some comparisons

### Rate ###
# How fast to scan


### Output ###
# output to file
# -oX scan.xml
# -oG grepable
# -oJ Json



### Exclude ###
# Excluded IP ranges


# Clean old files




print("Starting Masscan")
# os.system('masscan%s-p%s --rate %i -oG %s %s %s >/dev/null 2>&1' % (host, ports_to_scan, args.rate, savefile, hostfile, exclude))
os.system('masscan 161.35.17.0/24 -p1-1000 --rate 10000 -oX scan.xml')

print("Masscan done")

print("Starting Nmap")
# Nmap banner grabber
# nmap 161.35.17.24 -sV -p80 --script=banner


print("Scan finished")
# Clean up files