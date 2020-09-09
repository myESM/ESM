API_KEY=`cat SecBuzzerESM.env | grep API_KEY_VALUE | cut -d = -f 2`
if [ -n "$API_KEY" ]
then
mkdir -p tmp/rules
current_rules_version=`curl -X POST "https://test.api.secbuzzer.co/esmapi/web/file/fileVersion" -d "{'TypeCode': 'it'}" -H "Content-Type: application/json" -H "accept: */*" -H "authorization: $API_KEY" | cut -d : -f 2 | cut -d \" -f 2`
curl -o rules.tgz "https://test.api.secbuzzer.co/esmapi/web/file/download/it/$current_rules_version" -H "accept: */*" -H "authorization: $API_KEY"
tar zxvf rules.tgz -C tmp/rules
sudo chown 1000:1000 /tmp/* -R
sudo rsync -r --delete tmp/rules/ Suricata/suricata/rules/
rm -rf tmp rules.tgz
docker-compose --env-file SecBuzzerESM.env -f Suricata/docker-compose.yml restart
else
echo No API key found, Suricata rules download fail, check SecBuzzerESM.env
fi