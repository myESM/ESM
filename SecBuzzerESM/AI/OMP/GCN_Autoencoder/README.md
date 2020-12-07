# One mode projection (GCN+Autoencoder)

## Prerequest
- Python 3.7

## Install library with pip
```
pip3 install -r requirements.txt
```

## Config.ini
```
[es]
es_server = 192.168.70.24
es_port = 19200
nu = 0.0001
```

## Run code
```
python3 main.py
```

## API Example

- API route: omp_gcn/api/v1.0
- API example
    - index
    - start_time
        - format: YYYY-mm-ddTHH:MM:SS.ffffff+08:00
    - end_time
        - format: YYYY-mm-ddTHH:MM:SS.ffffff+08:00


```
http://localhost:5000/omp_gcn/api/v1.0?index=imbd-input-data-ip&start_time=2019-12-10T03:00:00.000000%2B08:00&end_time=2019-12-10T06:00:00.000000%2B08:00
```

## Input Schema

Key                         | Value
----------------------------|---------------
Src IP                      | 192.168.77.195
Dst IP                      | 192.168.77.187
Src Port                    | 59175
Dst Port                    | 71
Protocol                    | 6
Timestamp                   | 2019-12-10T04:19:27.843876+08:00


## Output Schema

Key                         | Value
----------------------------|---------------
src_ip                      | 192.168.77.195
event_type                  | alert
alert.category              | Network Service Scanning
alert.signature_id          | 20310001
alert.signature             | CSTI IMBD1 - Network Service Scanning
alert.severity              | 2
start_time                  | 2019-12-10T03:00:00.000000+08:00
end_time                    | 2019-12-10T06:00:00.000000+08:00
module                      | IMBD
log_type                    | traffic
in_iface                    | [From Input]
timestamp                   | 2020-08-24T10:58:56.869390+08:00
ingest_timestamp            | 2020-08-24T02:58:56.869390Z
user_data2                  | ["192.168.77.187:71", "192.168.77.187:72", "192.168.77.187:73", "192.168.77.187:74", "192.168.77.187:75"]

