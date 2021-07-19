#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import json
import os
import ipaddress
import random
import time
from datetime import datetime, timedelta
from collections import Counter
from apscheduler.schedulers.blocking import BlockingScheduler
from pytz import utc

scheduler = BlockingScheduler()

ESIPPORT = 'elasticsearch:9200'
HOMENET_STR = os.getenv("HOME_NET")
WAIT_SEC = random.randint(1,30)
HOMENETS = HOMENET_STR.strip().replace('"', '').replace("'", "").strip('[').strip(']').split(',')

print('HOMENETS:', HOMENETS)
ESM_API = os.getenv("ESM_API")
ORG_1_CODE = os.getenv("ORG_1_CODE")
ORG_2_CODE = os.getenv("ORG_2_CODE")
ORG_3_CODE = os.getenv("ORG_3_CODE")
HOSTNAME = None
HEADER = {'Content-Type': 'application/json', 'authorization': ESM_API}

old_print = print
def timestamped_print(*args, **kwargs):
  old_print("[*]",datetime.now(), os.path.basename(__file__), *args, **kwargs)
print = timestamped_print

def check_ip_valid(iporcidr):
    try:
        if ipaddress.ip_network(iporcidr):
            return True
    except:
        return False

def check_home_ip(ip):
    """
    Check ip is in HOME_NET
    """
    for _ in HOMENETS:
        if ipaddress.ip_address(ip) in ipaddress.ip_network(_):
            return True
    return False

def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")

def main():
    global HOMENETS
    global Counter

    if str2bool(os.getenv('DEV', 'Null')):
        RMQ_SERVER = "https://api.esm.cyber.cstilab.co"
        WAIT_SEC = 0
    else:
        RMQ_SERVER = "https://api.esm.cyber.cstilab.co"

    queue_stats = requests.get(f"{RMQ_SERVER}/esmapi/queues/%2F/Packet_Statistics", headers=HEADER).json()
    # print(queue_stats)
    if queue_stats.get('error'):
        print('Creating RMQ queue...')
        requests.put(f"{RMQ_SERVER}/esmapi/queues/%2F/Packet_Statistics", headers=HEADER)
        print('Creating RMQ queue success')

    with open('/HOSTNAME', 'r') as f:
        HOSTNAME = f.readline().strip()

    print('waiting', WAIT_SEC, 'sec')
    time.sleep(WAIT_SEC)
    HOMENETS = [_ for _ in HOMENETS if check_ip_valid(_)]
    DATE = datetime.utcnow() - timedelta(hours=1)
    try:
        # Get Top 20 Source Port
        data = '{"query":{"bool":{"must":[{"range":{"@timestamp":{"gt":"'+DATE.strftime('%Y-%m-%dT%H')+':00:00.000Z","lt":"'+DATE.strftime('%Y-%m-%dT%H')+':59:59.999Z"}}}]}},"size":0,"track_total_hits": false,"aggs": {"my_buckets": {"composite": {"size": 99999,"sources": [{"source.port": {"terms": {"field": "source.port"}}}]}}}}'
        resp = requests.post(f"http://{ESIPPORT}/packetbeat-{DATE.strftime('%Y.%m.%d')}/_search", data=data, headers=HEADER).json()
        splist = Counter({_['key']['source.port']: _['doc_count'] for _ in resp['aggregations'].get('my_buckets')['buckets']})
        t20sp = [{'port': _[0], 'count': _[1]} for _ in splist.most_common(20)]
        # Total Source Port 
        totalsp = len(splist)

        # Get Top 20 Destination Port
        data = '{"query":{"bool":{"must":[{"range":{"@timestamp":{"gt":"'+DATE.strftime('%Y-%m-%dT%H')+':00:00.000Z","lt":"'+DATE.strftime('%Y-%m-%dT%H')+':59:59.999Z"}}}]}},"size":0,"track_total_hits": false,"aggs": {"my_buckets": {"composite": {"size": 99999,"sources": [{"destination.port": {"terms": {"field": "destination.port"}}}]}}}}'
        resp = requests.post(f"http://{ESIPPORT}/packetbeat-{DATE.strftime('%Y.%m.%d')}/_search", data=data, headers=HEADER).json()
        dplist = Counter({_['key']['destination.port']: _['doc_count'] for _ in resp['aggregations'].get('my_buckets')['buckets']})
        t20dp = [{'port': _[0], 'count': _[1]} for _ in dplist.most_common(20)]
        # Total Destination Port 
        totaldp = len(dplist)

        # Get Top 20 Socure IP
        data = '{"query":{"bool":{"must":[{"range":{"@timestamp":{"gt":"'+DATE.strftime('%Y-%m-%dT%H')+':00:00.000Z","lt":"'+DATE.strftime('%Y-%m-%dT%H')+':59:59.999Z"}}}]}},"size":0,"track_total_hits": false,"aggs": {"my_buckets": {"composite": {"size": 3000,"sources": [{"source.ip": {"terms": {"field": "source.ip"}}}]}}}}'
        resp = requests.post(f"http://{ESIPPORT}/packetbeat-{DATE.strftime('%Y.%m.%d')}/_search", data=data, headers=HEADER).json()
        bip = ['::', '0.0.0.0'] # ip black list
        siplist = Counter({_['key']['source.ip']: _['doc_count'] for _ in resp['aggregations'].get('my_buckets')['buckets'] if not _['key']['source.ip'] in bip})
        t20sip = [{'ip': _[0], 'count': _[1]} for _ in siplist.most_common(20)]
        # Total Source IP 
        totalsip = len(siplist)

        # Get Top 20 Destination IP
        data = '{"query":{"bool":{"must":[{"range":{"@timestamp":{"gt":"'+DATE.strftime('%Y-%m-%dT%H')+':00:00.000Z","lt":"'+DATE.strftime('%Y-%m-%dT%H')+':59:59.999Z"}}}]}},"size":0,"track_total_hits": false,"aggs": {"my_buckets": {"composite": {"size": 99999,"sources": [{"destination.ip": {"terms": {"field": "destination.ip"}}}]}}}}'
        resp = requests.post(f"http://{ESIPPORT}/packetbeat-{DATE.strftime('%Y.%m.%d')}/_search", data=data, headers=HEADER).json()
        bip = ['::', '0.0.0.0']
        diplist = Counter({_['key']['destination.ip']: _['doc_count'] for _ in resp['aggregations'].get('my_buckets')['buckets'] if not _['key']['destination.ip'] in bip})
        t20dip = [{'ip': _[0], 'count': _[1]} for _ in diplist.most_common(20)]
        # Total Destination IP
        totaldip = len(diplist)
    except KeyError as e:
        print('Error:', e)
        print('ES connect error')

    HOME_IP = [ip for ip in siplist if check_home_ip(ip)]

    _DATA = {
        'Source':{
            'Top20IP': t20sip,
            'Top20Port': t20sp,
            'TotalIP': totalsip,
            'TotalPort': totalsp,
        },
        'Destination':{
            'Top20IP': t20dip,
            'Top20Port': t20sp,
            'TotalIP': totaldip,
            'TotalPort': totaldp,
        },
        'TotalHomeIP': len(HOME_IP),
        'HomeIP': HOME_IP,
        "ORG_1_CODE": ORG_1_CODE,
        "ORG_2_CODE": ORG_2_CODE,
        "ORG_3_CODE": ORG_3_CODE,
        "HOSTNAME": HOSTNAME
    }
    # {"properties":{"Content-Type":"application/json"},"routing_key":"network_statistics","payload":json.dumps(_DATA),"payload_encoding":"string"}
    datas = json.dumps({"properties":{"Content-Type":"application/json"},"routing_key":"Packet_Statistics","payload":json.dumps(_DATA),"payload_encoding":"string"})
    # print(_DATA)
    resp = requests.post(f"{RMQ_SERVER}/esmapi/exchanges/%2F/amq.default/publish", headers=HEADER, data=datas).json()
    print(resp)

if __name__ == "__main__":
    if str2bool(os.getenv('DEV', 'Null')):
        print("RUNNING WITH DEV MODE")
    job = scheduler.add_job(main, 'interval', hours=1, timezone=utc)
    scheduler.start()