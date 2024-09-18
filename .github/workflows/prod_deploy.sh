#!/bin/sh
# ubuntu 권한으로 모든 명령어 실행
# sudo -u ubuntu sh <<EOF
git checkout main
git pull
echo "$ENV_CONTENT" > .env
docker build -t suinbundnagline/sulmoon2yong-ai:lastest .
docker run -d --name suinbundnagline/sulmoon2yong-ai:latest -p 8000:8000 sulmoon2yong-ai-server
docker image prune -f
# EOF