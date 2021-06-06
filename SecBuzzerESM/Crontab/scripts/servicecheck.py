# -*- coding: utf-8 -*-

import docker
import os
import json
import requests
from datetime import datetime
from pprint import pprint

HOSTNAME = None
RMQ_SERVER = None
CONFIG = None
HEADER = None
client = docker.DockerClient(base_url='unix://var/run/docker.sock')

old_print = print
def timestamped_print(*args, **kwargs):
  old_print("[*]",datetime.now(), os.path.basename(__file__), *args, **kwargs)
print = timestamped_print

def init():
    global HOSTNAME
    global RMQ_SERVER
    global CONFIG
    global HEADER
    with open('/.env') as f: # Read and init the SecBuzzerESM.env
        CONFIG = {line.split('=')[0]:line.split('=')[1].strip() for line in f.readlines() if not line.startswith('#')}

    HEADER = {'Content-Type': 'application/json', 'authorization': CONFIG.get("API_KEY_VALUE", "")}

    if CONFIG.get('DEV_MODE'):
        RMQ_SERVER = "https://test.api.secbuzzer.co"
        print("RUNNING WITH DEV MODE")
    else:
        RMQ_SERVER = "https://api.esm.secbuzzer.co"
    if not HOSTNAME:
        with open('/hostname', 'r') as f:
            HOSTNAME = f.readline().strip()

    queue_stats = requests.get(f"{RMQ_SERVER}/esmapi/queues/%2F/Service_Info", headers=HEADER).json()
    # print(queue_stats)
    if queue_stats.get('error'):
        print('Creating RMQ queue...')
        requests.put(f"{RMQ_SERVER}/esmapi/queues/%2F/Service_Info", headers=HEADER)
        print('Creating RMQ queue success')

def main():
    # pprint(client.df())
    _DATA = {
        "ORG_1_CODE": CONFIG.get("ORG_1_CODE", 'TEST'),
        "ORG_2_CODE": CONFIG.get("ORG_2_CODE", 'TEST'),
        "ORG_3_CODE": CONFIG.get("ORG_3_CODE", ''),
        "HOSTNAME": HOSTNAME
    }
    # pprint(client.df())
    _DATA.update(client.df())
    # pprint(_DATA)
    _DATA = json.dumps(_DATA)
    datas = json.dumps({"properties":{"Content-Type":"application/json"},"routing_key":"Service_Info","payload":_DATA,"payload_encoding":"string"})
    resp = requests.post(f"{RMQ_SERVER}/esmapi/exchanges/%2F/amq.default/publish", headers=HEADER, data=datas).json()
    print(resp)
if __name__ == "__main__":
    init()
    main()