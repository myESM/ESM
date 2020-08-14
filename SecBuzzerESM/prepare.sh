DOCKER_VERSION=18.09.3
COMPOSE_VERSION=1.25.3
GRAFANA_PIE_CHART_VERSION=1.5.0

# requirements check
command -v docker >/dev/null 2>&1 || { echo >&2 "[*] 請確認是否有安裝 Docker"; exit 1; }
command -v docker-compose >/dev/null 2>&1 || { echo >&2 "[*] 請確認是否有安裝 Docker-compose"; exit 1; }

echo "[*] Build & Pull docker images"
find . -type f -name "docker-compose.yml" -exec docker-compose -f {} build \;
find . -type f -name "docker-compose.yml" -exec docker-compose -f {} pull \;

echo [*] Packaging all images
mkdir -p envimage
docker save $(docker images | sed '1d' | awk '{print $1 ":" $2 }') | gzip > './envimage/SecBuzzerESM.tgz'

echo [*] Download grafana plugin
mkdir -p ES/grafana_plugins
git -C './ES/grafana_plugins/' clone https://github.com/grafana/piechart-panel.git --branch release-$GRAFANA_PIE_CHART_VERSION 

echo [*] Download docker
wget https://download.docker.com/linux/static/stable/x86_64/docker-$DOCKER_VERSION.tgz -P './envimage/'

echo [*] Download docker-compose
curl -L "https://github.com/docker/compose/releases/download/$COMPOSE_VERSION/docker-compose-Linux-x86_64" -o ./envimage/docker-compose