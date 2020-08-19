import requests
import time
import json

# Delete
# curl -X DELETE http://elasticsearch:9200/_ingest/pipeline/my_timestamp_pipeline
# https://blog.csdn.net/UbuntuTouch/article/details/99702199

pipline_state = None

q_header = {
    "Content-Type": "application/json",
    'Connection': 'close'
}

pipeline_settings = """
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
"""

replica_settings =  """
{
        "index_patterns": ["*"],
        "settings":{
          "number_of_replicas": 0
        }
}
"""

while not pipline_state:
    try:
        replica_state = requests.put('http://elasticsearch:9200/_template/replicas_0?pretty', 
                      data = replica_settings, headers=q_header).status_code
        print('replica_state:', replica_state)
        pipline_state = requests.put('http://elasticsearch:9200/_ingest/pipeline/my_timestamp_pipeline', 
                    data = pipeline_settings, headers=q_header).status_code
        print('pipline_state:', pipline_state) 
    except:
        time.sleep(1)
print('[*] es_setter done!')
