#!/bin/bash
set -e

cd ~/selenium-service
docker rm -f selenium-service || true
docker build -t selenium-service -f ./docker/app/Dockerfile .
docker run -d --name selenium-service \
  -p 5024:8080 \
  selenium-service
