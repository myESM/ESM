API_KEY=`cat SecBuzzerESM.env | grep API_KEY_VALUE | cut -d = -f 2`
mkdir -p tmp/rules
rules_version=`curl -X POST "https://api.hub.secbuzzer.co/esmapi/web/file/fileVersion" -H "accept: */*" -H "authorization: $API_KEY" | cut -d : -f 2 | cut -d \" -f 2`
curl -o rules.tgz "https://api.hub.secbuzzer.co/esmapi/web/file/download/$rules_version" -H "accept: */*" -H "authorization: $API_KEY"
tar zxvf rules.tgz -C tmp/rules
sudo chown 1000:1000 /tmp/* -R
sudo rsync -r --delete tmp/rules/ Suricata/suricata/rules/
rm -rf tmp rules.tgz
docker-compose --env-file SecBuzzerESM.env -f Suricata/docker-compose.yml restart