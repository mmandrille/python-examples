#!/bin/bash
printf "\nStarting containers:\n"
docker-compose -f docker-compose.yml up

# printf "\nShowing Console:\n"
# docker logs -f producer consumer # Will be stay here until we control+c it...

# printf "\nStopping containers:\n"
# docker-compose -f docker-compose.yml stop

