FROM ubuntu:20.04
ENV DEBIAN_FRONTEND noninteractive
# tag the image

RUN apt update && apt-get install -y \
nmap \
python3 \
net-tools \
python3-pip \
masscan \
libpcap-dev

COPY scan.py .
COPY requirements.txt .
COPY hosts.txt .

RUN mkdir /finalOutput
RUN python3 -m pip install -r requirements.txt

# Usikker på om jeg trenger disse
ENV IP={$ip}
ENV PORT={$port}

ENTRYPOINT ["python3", "scan.py"]


# DEBUG: docker run -it --entrypoint sh security_lab_robot_scanner 
# Running: docker run -v results:/finalOutput security_lab_robot_scanner 80,22,139,21,23

# run a docker container, and mount the directory results on the host, to the directory /finalOutput in the container
# Running: docker run -v results:/finalOutput security_lab_robot_scanner 80,22,139,21,23

# TODO: mounting av mappe til container funker ikke, må fikse dette !!!