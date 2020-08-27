# ETA1

## Prerequest

An `Python3` environment. If you want to run it on docker, recommand using `python:3.8.5-buster`(gcc is needed).

## Install library with pip
You can use `pip3 install` to install packages below

- wheel==0.31.1
- Cython==0.28.2
- elasticsearch==6.3.1
- Flask==1.0.2
- xgboost==1.0.0
- scikit-learn==0.23.1
- pandas==0.25.0
- numpy==1.18.4

or you can use `pip3 install -r requirements.txt`

[NOTE] There may be an error message for build pandas, but it doesn't matter.

## config.ini

Parameters listed below could be changed with requirement.

```
[ES]
es_server = 192.168.70.120
es_port = 9201
```

## Run Code

```
python3 eta_attack_api.py
```

## API Example

- API route: eta_attack/api/v1.0
- API example
	- index
	- start_time
		- format: YYYY-mm-ddTHH:MM:SS.ffffff+08:00
	- end_time
 		- format: YYYY-mm-ddTHH:MM:SS.ffffff+08:00


```
http://localhost:5000/eta_attack/api/v1.0?index=cic_20200804&start_time=2020-08-04T11:25:00.000000%2B08:00&end_time=2020-08-04T11:30:00.000000%2B08:00
```

```
curl -i http://localhost:5000/eta_attack/api/v1.0\?index\=cic_20200804\&start_time\=2020-08-04T11:25:00.000000%2B08:00\&end_time\=2020-08-04T11:30:00.00000%2B08:00
```

## Response Code
Code | Description
-----|--------------
200  | Success
404  | Not Found
500  | Internal Server Error

## Input Schema
Below table is an example of input schema from ES.

Key                         | Value
----------------------------|---------------
Src Port                    | 59175
Dst Port                    | 9201
Flow Duration               | 27843
Total Fwd Packet            | 5
Total Bwd packets           | 3
Total Length of Fwd Packet  | 2683.0
Total Length of Bwd Packet  | 323.0
Fwd Packet Length Max       | 1460.0
Fwd Packet Length Min       | 0.0
Fwd Packet Length Mean      | 536.6
Fwd Packet Length Std       | 739.5321494025801
Bwd Packet Length Max       | 323.0
Bwd Packet Length Min       | 0.0
Bwd Packet Length Mean      | 107.66666666666667
Bwd Packet Length Std       | 186.48413694824913
Flow Bytes/s                | 107962.50404051288
Flow Packets/s              | 287.32536005459184
Flow IAT Mean               | 3977.5714285714284
Flow IAT Std                | 6941.2158602832405
Flow IAT Max                | 19513.0
Flow IAT Min                | 24.0
Fwd IAT Total               | 27843.0
Fwd IAT Mean                | 6960.75
Fwd IAT Std                 | 12053.697893869195
Fwd IAT Max                 | 25006.0
Fwd IAT Min                 | 24.0
Bwd IAT Total               | 23218.0
Bwd IAT Mean                | 11609.0
Bwd IAT Std                 | 11177.943996996943
Bwd IAT Max                 | 19513.0
Bwd IAT Min                 | 3705.0
Fwd PSH Flags               | 0
Fwd URG Flags               | 0
Fwd Header Length           | 112
Bwd Header Length           | 72
Fwd Packets/s               | 179.5783500341199
Bwd Packets/s               | 107.74701002047193
Packet Length Min           | 0.0
Packet Length Max           | 1460.0
Packet Length Mean          | 334.0
Packet Length Std           | 583.915019501982
Packet Length Variance      | 340956.74999999994
FIN Flag Count              | 1
SYN Flag Count              | 2
PSH Flag Count              | 2
ACK Flag Count              | 7
URG Flag Count              | 0
Down/Up Ratio               | 0.0
Average Packet Size         | 375.75
Fwd Segment Size Avg        | 536.6
Bwd Segment Size Avg        | 107.66666666666667
Subflow Fwd Packets         | 0
Subflow Fwd Bytes           | 335
Subflow Bwd Packets         | 0
Subflow Bwd Bytes           | 40
Fwd Init Win Bytes          | 64240
Bwd Init Win Bytes          | 501
Fwd Act Data Pkts           | 2
Fwd Seg Size Min            | 20
Active Mean                 | 0
Active Std                  | 0
Active Max                  | 0
Active Min                  | 0
Idle Mean                   | 1.596511622913498E15
Idle Std                    | 0.0
Idle Max                    | 1.596511622913498E15
Idle Min                    | 1.596511622913498E15

## Output Schema
Below table is an example of output schema to ES.

Key                 | Value
--------------------|---------------
flow_id             | XyPZBXEBOI2XA3yCwRPD
timestamp           | 2020-03-23T13:24:39.144408+08:00
event_type          | alert
alert.category      | Endpoint Denial of Service
alert.severity      | 10
alert.signature     | CSTI ETA1 - ATT&CK Endpoint Denial of Service - T1499
src_ip              | 192.168.70.196
dest_ip             | 192.168.70.1
src_port            | 138
dest_port           | 138
alert.action        | N/A
proto               | tcp
module              | ETA-ATTACK
in_iface            | [From Input]
alert.signature_id  | 20110002
log_type            | traffic
reference           | https://attack.mitre.org/techniques/T1204/
log_time            | 2020-03-11T10:02:56.762791+08:00
alert.gid           | 0
dump_status         | 0
ingest_timestamp    | 2020-03-23T05:24:39.144408Z
