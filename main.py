import subprocess
import os
#os.system('nmap 127.0.0.1')
# os.system('masscan -banners')


def checkForUpdate()
    pass
    # git pull


def masscan():
    pass
# Masscan supports json output
# take results from masscan, and do nmap on the ports



### Check Docker container
def dockerController():
    containerNr = os.system('docker ps | wc -l')
    
    print(containerNr)
dockerController()

#docker ps -a | wc -l

# main