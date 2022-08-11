#!/bin/bash
printf "\n\nStarting containers:"
docker-compose -f docker-compose.yml --compatibility up --build --remove-orphans

