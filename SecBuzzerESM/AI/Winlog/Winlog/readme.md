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

## Response Codes

```
200: Success
404: Cannot be found
50X: Server Error
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

## Input Source

- Agent:
  - Winlogbeat
- Data Source:
  - Microsoft-Windows-Sysmon%4Operational.evtx
  - Microsoft-Windows-PowerShell%4Operational.evtx
  - Security.evtx

## Output Schema
| ES Fields                    |
| ---------------------------- |
| _index                       |
| _type                        |
| _id                          |
| _score                       |
| _source                      |
| timestamp                    |
| flow_id                      |
| in_iface                     |
| event_type                   |
| vlan                         |
| src_ip                       |
| src_port                     |
| dest_ip                      |
| dest_port                    |
| proto                        |
| metadata                     |
| flowbits                     |
| tx_id                        |
| alert                        |
| action                       |
| gid                          |
| signature_id                 |
| rev                          |
| signature                    |
| category                     |
| severity                     |
| metadata                     |
| by                           |
| created_at                   |
| http                         |
| hostname                     |
| url                          |
| http_user_agent              |
| http_content_type            |
| http_method                  |
| protocol                     |
| status                       |
| length                       |
| http_response_body_printable |
| http_response_body           |
| app_proto                    |
| flow                         |
| pkts_toserver                |
| pkts_toclient                |
| bytes_toserver               |
| bytes_toclient               |
| start                        |
| payload                      |
| payload_printable            |
| stream                       |
| log_time                     |
| _log_type                    |
| module                       |
| timestamp                    |
| user_data1                   |
| timestamp                    |
| winlog                       |
| opcode                       |
| version                      |
| user                         |
| name                         |
| domain                       |
| type                         |
| identifier                   |
| provider_guid                |
| event_data                   |
| LogonId                      |
| ParentProcessGuid            |
| ProcessGuid                  |
| ParentImage                  |
| User                         |
| ParentCommandLine            |
| TerminalSessionId            |
| CurrentDirectory             |
| ParentProcessId              |
| Product                      |
| Hashes                       |
| Description                  |
| IntegrityLevel               |
| FileVersion                  |
| CommandLine                  |
| LogonGuid                    |
| RuleName                     |
| Image                        |
| OriginalFileName             |
| UtcTime                      |
| ProcessId                    |
| Company                      |
| computer_name                |
| provider_name                |
| record_id                    |
| task                         |
| process                      |
| pid                          |
| thread                       |
| id                           |
| channel                      |
| event_id                     |
| api                          |
| event                        |
| kind                         |
| code                         |
| provider                     |
| action                       |
| created                      |
| host                         |
| name                         |
| log                          |
| file                         |
| path                         |
| level                        |
| ecs                          |
| version                      |
| agent                        |
| ephemeral_id                 |
| id                           |
| name                         |
| type                         |
| version                      |
| hostname                     |
| message                      |
| AuthenticationPackageName    |
| CreationUtcTime              |
| DestinationHostname          |
| DestinationIp                |
| DestinationIsIpv6            |
| DestinationPort              |
| DestinationPortName          |
| ElevatedToken                |
| ImpersonationLevel           |
| Initiated                    |
| IpAddress                    |
| IpPort                       |
| KeyLength                    |
| LmPackageName                |
| LogonProcessName             |
| LogonType                    |
| MessageNumber                |
| MessageTotal                 |
| Path                         |
| ProcessName                  |
| Protocol                     |
| RestrictedAdminMode          |
| ScriptBlockId                |
| ScriptBlockText              |
| SourceHostname               |
| SourceIp                     |
| SourceIsIpv6                 |
| SourcePort                   |
| SourcePortName               |
| SubjectDomainName            |
| SubjectLogonId               |
| SubjectUserName              |
| SubjectUserSid               |
| TargetDomainName             |
| TargetFilename               |
| TargetInfo                   |
| TargetLinkedLogonId          |
| TargetLogonGuid              |
| TargetLogonId                |
| TargetOutboundDomainName     |
| TargetOutboundUserName       |
| TargetServerName             |
| TargetUserName               |
| TargetUserSid                |
| TransmittedServices          |
| VirtualAccount               |
| WorkstationName              |