#!/bin/sh
# ubuntu 권한으로 모든 명령어 실행
sudo -u ubuntu sh <<EOF
git checkout main
git pull
echo "$ENV_CONTENT" > .env
docker stop sulmoon2yong-ai-server
docker rm sulmoon2yong-ai-server
docker build -t suinbundangline/sulmoon2yong-ai:lastest .
docker run -d --name sulmoon2yong-ai-server -p 8000:8000 suinbundangline/sulmoon2yong-ai:lastest 
docker image prune -af
EOF