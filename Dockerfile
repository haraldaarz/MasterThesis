FROM ubuntu:20.04
ENV DEBIAN_FRONTEND noninteractive
# tag the image


RUN apt update && apt-get install -y \
nmap \
python3 \
net-tools

COPY scan.py .

ENTRYPOINT ["python3", "scan.py"]
