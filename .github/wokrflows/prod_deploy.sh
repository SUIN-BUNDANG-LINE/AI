#!/bin/sh
# ubuntu 권한으로 모든 명령어 실행
sudo -u ubuntu sh <<EOF
git checkout main
git pull
echo "$ENV_CONTENT" | base64 -d > .env.local
EOF