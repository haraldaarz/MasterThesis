import subprocess
import os
import sys
import docker

# Main program to controll Docker containers, and logging

#### Consts
client = docker.from_env()


def installDependencies():
    os.system('apt install python3-pip')
    pass

def checkForGitUpdate():
    pass
    # git pull
    

def masscan():
    pass
# Masscan supports json output
# take results from masscan, and do nmap on the ports

def startTestDocker():
    #client.containers.run('ubuntu', 'echo hello world')
    client.containers.list()

### Check Docker container
def dockerController():
    #print(containerNr)
    os.system('cd Docker && docker-compose up -d --remove-orphans')


def main():

    print("Containers running:")
    containerNr = int(os.system('docker ps | wc -l'))
    print(containerNr)
    print("There are", containerNr, "running")
    val1 = input("Start docker? y/n ")
    if val1 == "y":
        dockerController()
    else:
        print("Not starting.")
    if val1 == "n":
        val2 = input("Start Test container? y/n")
        if val2 == "y":
            startTestDocker()


# main
if __name__ == "__main__":
    main()
