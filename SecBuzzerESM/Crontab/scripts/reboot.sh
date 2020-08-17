#Create pipline
curl -X PUT "elasticsearch:9200/_ingest/pipeline/my_timestamp_pipeline?pretty" -H 'Content-Type: application/json' -d'
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
}'
echo "[*] Create timestamp pipeline"