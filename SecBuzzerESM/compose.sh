#!/bin/bash
if [ "$1" = "up" -o "$1" = "u" ]
then
    cmd="up -d"
elif [ "$1" = "down" -o "$1" = "d" ]
then
    cmd="down"
fi

docker-compose --env-file SecBuzzerESM.env -f ES/docker-compose.yml $cmd
docker-compose --env-file SecBuzzerESM.env -f Fluentd/docker-compose.yml $cmd
docker-compose --env-file SecBuzzerESM.env -f Suricata/docker-compose.yml $cmd
docker-compose --env-file SecBuzzerESM.env -f Crontab/docker-compose.yml $cmd
docker-compose --env-file SecBuzzerESM.env -f AI/docker-compose.yml $cmd
docker-compose --env-file SecBuzzerESM.env -f WEB/docker-compose.yml $cmd
