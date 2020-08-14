# ETA1

## Prerequest
- Python 3.6.5

## Install library with pip

you can use `pip3 install` to install below packages

- pandas==0.25.0
- numpy==1.18.4
- elasticsearch==6.3.1

or you can use `pip3 install -r requirements.txt`

## config.ini

Parameters listed below could be changed with requirement.

```
[ES]
es_server = 192.168.70.120
es_port = 9201
```

## Run Code

```
python3 eta1_api.py
```


## API Example

- API route: eta1/api/v1.0
- API example
	- index
	- start_time
		- format: YYYY-mm-ddTHH:MM:SS.ffffff+08:00
	- end_time
 		- format: YYYY-mm-ddTHH:MM:SS.ffffff+08:00


```
http://localhost:5000/eta1/api/v1.0?index=cic_20200804&start_time=2020-08-04T11:25:00.000000%2B08:00&end_time=2020-08-04T11:30:00.000000%2B08:00
```

```
curl -i http://localhost:5000/eta1/api/v1.0\?index\=cic_20200804\&start_time\=2020-08-04T11:25:00.000000%2B08:00\&end_time\=2020-08-04T11:30:00.00000%2B08:00
```