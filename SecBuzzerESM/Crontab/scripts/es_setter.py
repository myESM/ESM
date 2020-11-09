import requests
import time
import json
from datetime import datetime
import os
# Delete
# curl -X DELETE http://elasticsearch:9200/_ingest/pipeline/my_timestamp_pipeline
# https://blog.csdn.net/UbuntuTouch/article/details/99702199

pipline_state = None

header = {
    "Content-Type": "application/json",
    'Connection': 'close'
}

reqs = {
  "http://elasticsearch:9200/_ingest/pipeline/my_timestamp_pipeline": """
  {
    "description": "Adds a field to a document with the time of ingestion",
    "processors": [
      {
        "set": {
          "field": "ingest_timestamp",
          "value": "{{_ingest.timestamp}}"
        }
      }
    ]
  }
  """,
  "http://elasticsearch:9200/_template/replicas_0":"""
  {
          "index_patterns": ["*"],
          "settings":{
            "number_of_replicas": 0
          }
  }
  """,
  "http://elasticsearch:9200/_ingest/pipeline/packetbeat":"""
  {
      "description": "Remove some packetbeat field :D",
      "processors": [
        {
          "remove": {
            "field": [
              "ecs",
              "agent",
              "event",
              "dns",
              "host.name"
            ],
            "ignore_failure": true
          }
        }
      ]
  }""",
  "http://elasticsearch:9200/_cluster/settings":"""{
    "persistent": {
      "search.max_buckets": 100000
    }
  }"""
}

old_print = print
def timestamped_print(*args, **kwargs):
  old_print("[*]",datetime.now(), os.path.basename(__file__), *args, **kwargs)
print = timestamped_print

while not pipline_state:
    try:
        resps = [requests.put(url, data = data, headers=header).status_code 
                for url, data in reqs.items()]
        print(resps)
        pipline_state = len(set(resps)) == 1 and 200 in set(resps)
    except:
        time.sleep(1)
print('done!')
