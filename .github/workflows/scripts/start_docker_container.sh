#!/bin/bash
set -e

# docker network create selenium-service-network

docker run -d --name selenium-service \
  -p 4444:4444 \
  -p 5900:5900 \
  -p 7900:7900 \
  --shm-size=2g \
  -t \
  --network selenium-service-network \
  --name chrome \
  seleniarm/standalone-chromium:114.0


cd ~/selenium-service
docker rm -f selenium-service || true
docker build -t selenium-service -f ./docker/app/Dockerfile .
docker run -d --name selenium-service \
  -p 5024:8080 \
  --network selenium-service-network \
  selenium-service
