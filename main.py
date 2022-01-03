import subprocess
import os
import sys

def checkForUpdate():
    pass
    # git pull
    

def masscan():
    pass
# Masscan supports json output
# take results from masscan, and do nmap on the ports



### Check Docker container
def dockerController():
    
    if containerNr < 2:
        print(containerNr)
        os.system('cd Docker && docker-compose up -d')


#docker ps -a | wc -l

def main():
    print("hey there")
    containerNr = int(os.system('docker ps | wc -l'))
    print(containerNr)
    print("There are", containerNr, "running")
    val = input("Start docker? y/n ")
    if val == "y":
        dockerController()
    else:
        print("Not starting.")


# main
if __name__ == "__main__":
    main()
