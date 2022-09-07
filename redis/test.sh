#!/bin/bash
printf "\nStarting containers:\n"
docker-compose -f docker-compose.yml up --detach

# Define enviroment Variables:
export REDIS_URL=localhost
export REDIS_PORT=6379
export TIMES=25
# Launch our code
python3 -m venv venv
source venv/bin/activate
pip install -r requierements.txt
python try_redis.py

# Stopping containers
docker-compose -f docker-compose.yml stop