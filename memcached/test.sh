#!/bin/bash
printf "\nStarting containers:\n"
docker-compose -f docker-compose.yml up --detach

# Define enviroment Variables:
export MEMCACHE_URL=localhost:11211
export TIMES=25
# Launch our code
python3 -m venv venv
source venv/bin/activate
pip install -r requierements.txt
python memcache.py

# Stopping containers
docker-compose -f docker-compose.yml stop