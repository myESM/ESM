#!/bin/sh
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# Get docker-ce binary from: https://download.docker.com/linux/static/stable/x86_64/
# eg: wget https://download.docker.com/linux/static/stable/x86_64/docker-17.09.0-ce.tgz

SYSTEMDDIR=/lib/systemd/system
SERVICEFILE=docker.service
DOCKERDIR=/usr/bin
DOCKERBIN=docker
SERVICENAME=docker
MAINPID='$MAINPID'

tar xvpf ./envimage/docker-*.tgz

echo "##binary : ${DOCKERBIN} copy to ${DOCKERDIR}"
mv ${DOCKERBIN}/* ${DOCKERDIR} >/dev/null 2>&1
which ${DOCKERBIN}

echo "##systemd service: ${SERVICEFILE}"
echo "##docker.service: create docker systemd file"
cat >${SYSTEMDDIR}/${SERVICEFILE} <<EOF
[Unit]
Description=Docker Application Container Engine
Documentation=http://docs.docker.com
After=network.target docker.socket
[Service]
Type=notify
WorkingDirectory=/usr/local/bin
ExecStart=/usr/bin/dockerd \
                -H tcp://0.0.0.0:4243 \
                -H unix:///var/run/docker.sock \
                --selinux-enabled=false \
                --log-opt max-size=1g
ExecReload=/bin/kill -s HUP $MAINPID
LimitNOFILE=infinity
LimitNPROC=infinity
LimitCORE=infinity
TimeoutStartSec=0
Delegate=yes
KillMode=process
Restart=on-failure
[Install]
WantedBy=multi-user.target
EOF

echo ""

systemctl daemon-reload
systemctl restart ${SERVICENAME}

echo "##Service enabled: ${SERVICENAME}"
systemctl enable ${SERVICENAME}

echo "## docker version"
docker version

echo "## Group add"
groupadd docker >/dev/null 2>&1 || true
chgrp docker /var/run/docker.sock
usermod -aG docker ${USER} >/dev/null 2>&1

rm -rf docker

echo "## install docker-compose "
cp ./envimage/docker-compose /usr/local/bin/
chmod +x /usr/local/bin/docker-compose