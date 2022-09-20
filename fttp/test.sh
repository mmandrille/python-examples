#!/bin/bash
printf "\nStarting containers:\n"
docker-compose -f docker-compose.yml up --detach

printf "\nRunning Python Script:\n"
python fttp_test.py

printf "\nStopping containers:\n"
docker-compose -f docker-compose.yml stop
