#!/bin/sh
# ubuntu 권한으로 모든 명령어 실행
# sudo -u ubuntu sh <<EOF
git checkout main
git pull
echo "$ENV_CONTENT" | base64 -d > env
docker build -t sulmoon2yong-ai:lastest .
docker run -d --name sulmoon2yong-ai -p 8000:8000 sulmoon2yong-ai:lastest
# EOF