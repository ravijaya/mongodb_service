#!/bin/bash

docker-compose down
docker volume rm -f mongodb_datadrive  
docker image rm mongo:latest  mongodb_mongoseeder:latest
