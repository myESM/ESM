# Winlog

## Prerequisite

- Python : 3.8.5

## Install library with pip

```
$ pip3 install -r requirements.txt
```

## config.ini
```
[elasticsearch]
es_host = 192.168.70.120
es_port = 9203
es_output_index_prefix = "winlog-"
```

## Run Code

```
$ python3 winlog_api.py
```
## API example
 - API route : winlog/api/v1.0
 - API parameters:
   - index
   - start_time
     - format: YYYY-mm-ddTHH:MM:SS
   - end_time
     - format: YYYY-mm-ddTHH:MM:SS
```
http://localhost:5000/winlog/api/v1.0?index=winlogbeat_20200804&start_time=2020-07-15T00:00:00&end_time=2020-07-17T23:59:59
```
```
$curl -i http://localhost:5000/winlog/api/v1.0?index=winlogbeat_20200804&start_time=2020-07-15T00:00:00&end_time=2020-07-17T23:59:59
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 18
Server: Werkzeug/1.0.1 Python/3.8.5
Date: Wed, 05 Aug 2020 08:26:14 GMT

{"result":"Done"}
```