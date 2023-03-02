import sys
import datetime
import os

time=datetime.datetime.now()

ips = sys.argv[1]
output = "Starting Nmap scan on " + ips

ips = ips.replace(" ", ",")

ports = "--top-ports 1000" # Mulig denne må endres til en verdi, ikke to argumenter
rate = "10000"


print("Starting a default scan towards IP: " + ips)
#os.system("docker run -v /var/run/docker.soc:/var/run/docker.sock -it --name scan -e ADDESSES=ips  ")
os.system("docker run security_lab_robot_scanner " + ips + " " + ports + " " + rate)

print("nmap done")
