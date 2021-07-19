#!/bin/sh
set -euo pipefail
# set -ex # for debug
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

DOCKER_VERSION=18.09.3
COMPOSE_VERSION=1.25.3
GRAFANA_PIE_CHART_VERSION=1.5.0

sudo apt update
sudo apt install -y curl

get_script_dir () {
     SOURCE="${BASH_SOURCE[0]}"
     # While $SOURCE is a symlink, resolve it
     while [ -h "$SOURCE" ]; do
          DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
          SOURCE="$( readlink "$SOURCE" )"
          # If $SOURCE was a relative symlink (so no "/" as prefix, need to resolve it relative to the symlink base directory
          [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE"
     done
     DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
     echo "$DIR"
}

BASEDIR=$(get_script_dir)

echo "[*] Download grafana plugin"
rm -rf $BASEDIR/ES/grafana_plugins
mkdir -p $BASEDIR/ES/grafana_plugins
git -C $BASEDIR/ES/grafana_plugins/ clone https://github.com/grafana/piechart-panel.git --branch release-$GRAFANA_PIE_CHART_VERSION 

if [ -f "/usr/bin/docker" ] && [ -f "/usr/local/bin/docker-compose" ]; then
    echo "[*] Already install docker!"
else
    rm -rf $BASEDIR/envimage/
    echo "[*] Download docker"
    wget https://download.docker.com/linux/static/stable/x86_64/docker-$DOCKER_VERSION.tgz -P "$BASEDIR/envimage/"
    echo "[*] Download docker-compose"
    curl -L "https://github.com/docker/compose/releases/download/$COMPOSE_VERSION/docker-compose-Linux-x86_64" -o $BASEDIR/envimage/docker-compose
    echo "[*] Install docker & docker-compose"
    source $BASEDIR/install_docker.sh
fi

echo "[*] Build & Pull docker images"
find $BASEDIR -type f -name "docker-compose.yml" -exec docker-compose -f {} --log-level ERROR build \;
find $BASEDIR -type f -name "docker-compose.yml" -exec docker-compose -f {} --log-level ERROR pull \;

sudo mv /etc/sysctl.conf.bak /etc/sysctl.conf 2>/dev/null || true
sudo cp -n /etc/sysctl.conf{,.bak}

sudo sh -c "echo 'vm.max_map_count=262144
net.core.somaxconn = 1024
net.core.netdev_max_backlog = 5000
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
net.ipv4.tcp_wmem = 4096 12582912 16777216
net.ipv4.tcp_rmem = 4096 12582912 16777216
net.ipv4.tcp_max_syn_backlog = 8096
net.ipv4.tcp_slow_start_after_idle = 0
net.ipv4.tcp_tw_reuse = 1
net.ipv4.udp_mem = 4096 12582912 16777216
net.ipv4.udp_rmem_min = 16384
net.ipv4.udp_wmem_min = 16384
net.ipv4.ip_local_port_range = 10240 65535' >> /etc/sysctl.conf"
sudo sysctl -p

sudo mv /etc/security/limits.conf.bak /etc/security/limits.conf 2>/dev/null || true
sudo cp -n /etc/security/limits.conf{,.bak}
sudo sh -c "echo 'root soft nofile 655360
root hard nofile 655360
* soft nofile 655360
* hard nofile 655360' >> /etc/security/limits.conf"

find $BASEDIR -maxdepth 1 -mindepth 1 -type d -exec ln -s ../SecBuzzerESM.env {}/.env \; 2>/dev/null || true

API_KEY=`cat $BASEDIR/SecBuzzerESM.env | grep API_KEY_VALUE | cut -d = -f 2`
if [ -n "$API_KEY" ]
then
mkdir -p tmp/rules
current_rules_version=`curl -X POST "https://api.esm.cyber.cstilab.co/esmapi/web/file/fileVersion" -d "{'TypeCode': 'it'}" -H "Content-Type: application/json" -H "accept: */*" -H "authorization: $API_KEY" | cut -d : -f 2 | cut -d \" -f 2`
curl -o rules.tgz "https://api.esm.cyber.cstilab.co/esmapi/web/file/download/it/$current_rules_version" -H "accept: */*" -H "authorization: $API_KEY"
tar zxvf rules.tgz -C tmp/rules
sudo chown 1000:1000 tmp/* -R
sudo rsync -r --delete tmp/rules/ Suricata/suricata/rules/
rm -rf tmp rules.tgz
else
echo No API key found,Suricata rules download fail, check SecBuzzerESM.env
fi

mkdir -p /opt/Logs/ES/volume/es
mkdir -p /opt/Logs/Suricata
mkdir -p /opt/Logs/Fluentd
mkdir -p /opt/Logs/Buffers

chown 1000 /opt/Logs -R
chmod go-w $BASEDIR/Packetbeat/packetbeat.docker.yml

rm -rf envimage
sudo docker network create esm_network 2>/dev/null || true

echo "Disable Swap"
swapoff -a
sed -i 's/.*swap.*/#&/' /etc/fstab

echo "Done!"