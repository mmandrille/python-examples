#!/bin/bash
printf "\n\nStopping containers:\n"
docker-compose -f docker-compose.yml --compatibility stop

