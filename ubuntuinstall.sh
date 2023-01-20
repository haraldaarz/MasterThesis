sudo apt update -y && sudo apt upgrade -y

sudo apt install 

# install docker
sudo apt install docker.io -y

# Add user to docker group
sudo usermod -aG docker ${USER}

# Possibly need to run a new shell

# Install docker-compose
sudo apt install docker-compose

# Git clone elk_nmap
git clone https://github.com/bennettwarner/elk_nmap

# Change directory to elk_nmap
cd elk_nmap

# Run docker-compose
docker-compose up --build -d

# Git clone the scanner repo
git clone https://github.com/haraldaarz/MasterThesis


# Web interface
# git clone or cd and docker-compose up -d


# run a scan, and then run the ingestor

# after ingesting, visit IP:5601, 

# add index pattern, *nmap*

# copy dashboard template

