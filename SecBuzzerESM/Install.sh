#!/bin/sh
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

DOCKER_VERSION=18.09.3
COMPOSE_VERSION=1.25.3
GRAFANA_PIE_CHART_VERSION=1.5.0

sudo apt update
sudo apt install -y curl


echo "[*] Download grafana plugin"
rm -rf ES/grafana_plugins
mkdir -p ES/grafana_plugins
git -C './ES/grafana_plugins/' clone https://github.com/grafana/piechart-panel.git --branch release-$GRAFANA_PIE_CHART_VERSION 

if [ -f "/usr/bin/docker" ]; then
    echo "[*] Already install docker!"
else
    echo "[*] Download docker"
    wget https://download.docker.com/linux/static/stable/x86_64/docker-$DOCKER_VERSION.tgz -P './envimage/'
    echo "[*] Download docker-compose"
    curl -L "https://github.com/docker/compose/releases/download/$COMPOSE_VERSION/docker-compose-Linux-x86_64" -o ./envimage/docker-compose
    echo "[*] Install docker & docker-compose"
    source install_docker.sh
fi

echo "[*] Build & Pull docker images"
find . -type f -name "docker-compose.yml" -exec docker-compose -f {} build \;
find . -type f -name "docker-compose.yml" -exec docker-compose -f {} pull \;

sudo mv /etc/sysctl.conf.bak /etc/sysctl.conf 2>/dev/null
sudo cp -n /etc/sysctl.conf{,.bak}
sudo sh -c "echo vm.max_map_count=262144 >> /etc/sysctl.conf"

sudo sysctl -w vm.max_map_count=262144

sudo sh -c "echo 'net.core.somaxconn = 1024
net.core.netdev_max_backlog = 5000
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
net.ipv4.tcp_wmem = 4096 12582912 16777216
net.ipv4.tcp_rmem = 4096 12582912 16777216
net.ipv4.tcp_max_syn_backlog = 8096
net.ipv4.tcp_slow_start_after_idle = 0
net.ipv4.tcp_tw_reuse = 1
net.ipv4.ip_local_port_range = 10240 65535' >> /etc/sysctl.conf"
sudo sysctl -p

sudo mv /etc/security/limits.conf.bak /etc/security/limits.conf 2>/dev/null
sudo cp -n /etc/security/limits.conf{,.bak}
sudo sh -c "echo 'root soft nofile 655360
root hard nofile 655360
* soft nofile 655360
* hard nofile 655360' >> /etc/security/limits.conf"

ln -s ../SecBuzzerESM.env ES/.env 2>/dev/nul
ln -s ../SecBuzzerESM.env Fluentd/.env 2>/dev/nul
ln -s ../SecBuzzerESM.env Suricata/.env 2>/dev/nul
ln -s ../SecBuzzerESM.env Crontab/.env 2>/dev/nul
ln -s ../SecBuzzerESM.env WEB/.env 2>/dev/nul
ln -s ../SecBuzzerESM.env AI/.env 2>/dev/nul

mkdir -p /opt/Logs/ES/volume/es
mkdir -p /opt/Logs/ES/volume/es1
mkdir -p /opt/Logs/ES/volume/es2
mkdir -p /opt/Logs/Suricata
mkdir -p /opt/Logs/Fluentd
mkdir -p /opt/Logs/Buffers

chown 1000 /opt/Logs -R

rm -rf envimage
sudo docker network create esm_network