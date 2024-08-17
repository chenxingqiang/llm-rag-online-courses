#!/bin/bash

# Update package lists
sudo apt-get update

# Install Python and pip
sudo apt-get install -y python3 python3-pip

# Install required Python packages
pip3 install -r requirements.txt

# Install Docker
sudo apt-get install -y docker.io

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Set up the database
docker-compose up -d db

echo "Environment setup complete!"