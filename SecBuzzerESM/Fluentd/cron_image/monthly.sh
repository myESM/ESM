#Variable setting
createMonth="$(date -d '1 month' +%Y-%m)"
deleteMonth="$(date -d '-13 month' +%Y-%m)"

#Cteate template
curl -X PUT "localhost:19200/_template/suricata-$createMonth?pretty" -H 'Content-Type: application/json' -d'
{
        "index_patterns": ["suricata-'$createMonth'-*"],
        "settings":{
          "number_of_shards": 1,
          "number_of_replicas": 1,
          "index.lifecycle.name": "test_policy",
          "index.lifecycle.rollover_alias": "suricata-'$createMonth'",
          "refresh_interval": "30s"
        }
}
'

#Cteate index
curl -X PUT "localhost:19200/suricata-$createMonth-000001?pretty" -H 'Content-Type: application/json' -d'
{
  "aliases": {
    "suricata-'$createMonth'": {
      "is_write_index": true
    }
  }
}
'

#Delete  index
curl -X DELETE "localhost:19200/suricata-$deleteMonth*?pretty"

#Delete template
curl -X DELETE "localhost:19200/_template/suricata-$deleteMonth?pretty

reboot.sh:
createMonth="$(date +'%Y-%m')"
