import argparse
import sys
import os


def runScan(port, ip, rate):

    os.system("sudo docker run -v $(pwd)/results:/outputs security_lab_robot_scanner "+ port + " " + ip + " " +  rate  ) # & 8

def moveToIngestor():
    os.system("mv results/* ../elk_nmap/import/")
    print("Moved files to ingestor")

def ingestor():
    print("Starting ingestor")
    os.system("docker-compose run ingestor")


if __name__ == "__main__":

    if len(sys.argv) == 3:
        port = sys.argv[1]
        ips = sys.argv[2]
        rate = "10000"
        runScan(port, ips, rate)

    if len(sys.argv) == 4:
        port = sys.argv[1]
        ips = sys.argv[2]
        rate = sys.argv[3]
        runScan(port, ips, rate)

    moveToIngestor()
    ingestor()
    print("Done")

# Usage: python3 runScanner.py 80 193.157.195.0/23

    



