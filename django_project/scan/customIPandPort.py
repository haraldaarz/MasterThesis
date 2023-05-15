# Scanning file for custom port scan
import sys
import os

ip = sys.argv[1]
port = sys.argv[2]
rate = sys.argv[3]
ip = ip.replace(" ", ",")

print("Starting scan towards IP: " + ip + ", Port: " + port + " at rate: " + rate + " requests per second")

os.system("docker run security_lab_robot_scanner " + ip + " " + port + " " + rate)

portRange = ""

# if the port has a - in it
if "-" in port:
    portRange = port

if "," in port:
    portRange = port.replace(",", "%20or%20port%20")

if not "0/" in ip:
    ipRange = ip

ipRange = ip

mainURL = "http://192.168.1.85:5601/app/discover#/?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(columns:!(),filters:!(),index:ab7a45f0-2d0f-11ed-a4f1-8f3a048603fe,interval:auto,query:(language:kuery,query:'ip%20:%20" 
ending = ")'),sort:!())"
midDivider = "%20and%20(port%20"
customUrl = mainURL + ipRange + midDivider + portRange + ending


print("Database results from the specified scan: ")
print(customUrl)
