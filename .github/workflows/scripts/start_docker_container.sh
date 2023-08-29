#!/bin/bash
set -e

# # 引数がない場合は、環境変数を利用する
# if [ $# -eq 0 ]; then

# else

# fi


cd ~/selenium-service
docker rm -f selenium-service || true
docker build -t selenium-service -f ./docker/app/Dockerfile .
docker run -d --name selenium-service \
  -p 5024:8080 \
  selenium-service
