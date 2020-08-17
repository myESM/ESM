#Variable setting
deleteMonth="$(date -d '-13 month' +%Y-%m)"

#Delete  index
curl -X DELETE "localhost:19200/suricata-$deleteMonth*?pretty"
