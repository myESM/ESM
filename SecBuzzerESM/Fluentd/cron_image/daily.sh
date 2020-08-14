#Variable setting
createDay="$(date +'%Y-%m-%d' -d'+1 day')"
deleteDay="$(date +'%Y-%m-%d' -d'-365 day')"

#Cteate tomorrow template
curl -X PUT "localhost:19200/_template/lm-$createDay?pretty" -H 'Content-Type: application/json' -d'
{
        "index_patterns": ["lm-'$createDay'-*"],
        "settings":{
          "number_of_shards": 1,
          "number_of_replicas": 1,
          "index.lifecycle.name": "test_policy",
          "index.lifecycle.rollover_alias": "lm-'$createDay'",
	  "refresh_interval": "30s"
        }
}
'

#Cteate tomorrow index
curl -X PUT "localhost:19200/lm-$createDay-000001?pretty" -H 'Content-Type: application/json' -d'
{
  "aliases": {
    "lm-'$createDay'": {
      "is_write_index": true
    }
  }
}
'

#Delete ninety days ago index
curl -X DELETE "localhost:19200/lm-$deleteDay*?pretty"

#Delete ninety days ago template
curl -X DELETE "localhost:19200/_template/lm-$deleteDay?pretty"

