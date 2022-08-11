#!/bin/bash
printf "\n\nStarting containers:\n"
docker-compose -f docker-compose.yml up --build --remove-orphans

