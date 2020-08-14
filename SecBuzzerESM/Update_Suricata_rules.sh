mkdir -p tmp
rules_version=`curl -X POST "https://test.api.secbuzzer.co/esmapi/web/file/fileVersion" -H "accept: */*" -H "authorization: bNC7vJwbrRXUyKnEPf2SeC9IWbu3fCqt" | cut -d : -f 2 | cut -d \" -f 2`
curl -o rules.tgz "https://test.api.secbuzzer.co/esmapi/web/file/download/$rules_version" -H "accept: */*" -H "authorization: bNC7vJwbrRXUyKnEPf2SeC9IWbu3fCqt"
tar zxvf rules.tgz -C tmp
find tmp -type f -name "*.rules" -exec rsync -a --progress --remove-source-files {} Suricata/suricata/rules/ \;
rm -rf tmp rules.tgz
docker-compose --env-file SecBuzzerESM.env -f Suricata/docker-compose.yml restart