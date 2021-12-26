import os #Linux commands
import sys #Arguments
#import docker

print("Hello world")

print("The first argument is '%s'."%(sys.argv[1]))


os.system('docker ps -a')
# Start docker container


if sys.platform == 'linux':
    print("The host is a Linux machine")


content = "Hello"

with open("data/data.txt", "w") as file: # Overwrite the file
#with open("data/data.txt", "a") as file: # Append to excisting file
    file.write(content)