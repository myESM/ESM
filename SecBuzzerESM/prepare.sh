#!/bin/bash
set -euo pipefail

DOCKER_VERSION=18.09.3
COMPOSE_VERSION=1.25.3
GRAFANA_PIE_CHART_VERSION=1.5.0
shell_path=$(dirname "$BASH_SOURCE")

# requirements check
command -v docker >/dev/null 2>&1 || { echo >&2 "[*] 請確認是否有安裝 Docker"; exit 1; }
command -v docker-compose >/dev/null 2>&1 || { echo >&2 "[*] 請確認是否有安裝 Docker-compose"; exit 1; }

echo "[*] Delete All images"
docker rmi $(docker images -q) >/dev/null || true

echo "[*] Build & Pull docker images"
for path in `find . -type f -name "docker-compose.yml"`
do
docker-compose -f $path --log-level ERROR build
docker-compose -f $path --log-level ERROR pull
done

echo [*] Packaging all images
mkdir -p $shell_path'/envimage'
docker save $(docker images | sed '1d' | awk '{print $1 ":" $2 }') | gzip > $shell_path'/envimage/SecBuzzerESM.tgz'

echo [*] Download grafana plugin
mkdir -p $shell_path'/ES/grafana_plugins'
git -C $shell_path'/ES/grafana_plugins/' clone https://github.com/grafana/piechart-panel.git --branch release-$GRAFANA_PIE_CHART_VERSION 

echo [*] Download docker
curl -s --fail --show-error -L https://download.docker.com/linux/static/stable/x86_64/docker-$DOCKER_VERSION.tgz -o $shell_path"/envimage/docker-$DOCKER_VERSION.tgz"

echo [*] Download docker-compose
curl -s --fail --show-error -L "https://github.com/docker/compose/releases/download/$COMPOSE_VERSION/docker-compose-Linux-x86_64" -o $shell_path'/envimage/docker-compose'
