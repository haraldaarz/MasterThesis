FROM ubuntu:20.04
ENV DEBIAN_FRONTEND noninteractive

RUN apt update && apt-get install -y \
python3 python3-pip nmap net-tools \
masscan libpcap-dev

COPY scan.py .
COPY requirements.txt .
COPY hosts.txt .
RUN mkdir /finalOutput
RUN python3 -m pip install -r requirements.txt
ENV IP={$ip}
ENV PORT={$port}
ENTRYPOINT ["python3", "scan.py"] # or run the runscanner.py script file


# DEBUG: docker run -it --entrypoint sh security_lab_robot_scanner 
# Running: docker run -v results:/finalOutput security_lab_robot_scanner 80,22,139,21,23

# run a docker container, and mount the directory results on the host, to the directory /finalOutput in the container
# Running: sudo docker run -v $(pwd)/results:/outputs security_lab_robot_scanner 80