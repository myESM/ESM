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

q_json = """
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

while not pipline_state:
    try:
        pipline_state = requests.put('http://elasticsearch:9200/_ingest/pipeline/my_timestamp_pipeline', 
                    data = q_json, headers=q_header).status_code 
    except:
        time.sleep(1)
print('[*] Pipe created!')
