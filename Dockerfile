FROM ubuntu:20.04
ENV DEBIAN_FRONTEND noninteractive
# tag the image


RUN apt update && apt-get install -y \
nmap \
python3 \
net-tools

COPY scan2.py .

# Usikker på om jeg trenger disse
ENV IP={$ip}
ENV PORT={$port}



ENTRYPOINT ["python3", "scan2.py"]


