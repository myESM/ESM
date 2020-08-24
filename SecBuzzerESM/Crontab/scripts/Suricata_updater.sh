#/bin/bash

sleep $[ ( $RANDOM % 15 ) + 1 ]s
ESM_API=`cat /.env | grep API_KEY_VALUE | cut -d = -f 2`
current_rules_version=`curl -X POST "https://api.secbuzzer.co/esmapi/web/file/fileVersion" -H "accept: */*" -H "authorization: $ESM_API" | cut -d : -f 2 | cut -d \" -f 2`
local_rules_version=$(</tmp/local_rules_version)
if [ "$current_rules_version" != "$local_rules_version" ]
then
    echo "[*] New version found! rules update to $current_rules_version"
    curl -o /tmp/rules.tgz "https://api.secbuzzer.co/esmapi/web/file/download/$current_rules_version" -H "accept: */*" -H "authorization: $ESM_API"
    mkdir -p /tmp/rules
    tar zxf /tmp/rules.tgz -C /tmp/rules
    chown 1000:1000 /tmp/* -R
    rsync -a --delete /tmp/rules /Suricata_rules/
    rm -rf /tmp/rules /tmp/rules.tgz
    echo "[*] Restarting Suricata"
    sleep 3s
    curl -XPOST --unix-socket /var/run/docker.sock -H 'Content-Type: application/json' http://localhost/containers/suricata/restart
    rm /tmp/local_rules_version
    echo $current_rules_version > /tmp/local_rules_version
    echo "[*] Done!"
fi