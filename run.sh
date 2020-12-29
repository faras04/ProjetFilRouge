#! /usr/bin/env bash

# Start all containers
echo "Starting docker ."
docker-compose up -d --build

#Ctr c to stop and remove all containers
read -r -d '' _ </dev/tty
echo '\n\nTearing down the Docker environment, please wait.\n\n'

docker-compose -f docker-compose.yml down $*



