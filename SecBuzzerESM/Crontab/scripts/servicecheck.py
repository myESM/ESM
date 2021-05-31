# -*- coding: utf-8 -*-

import docker
import os
import json
import requests
from datetime import datetime
from pprint import pprint
ESM_API = os.getenv("ESM_API")
ORG_1_CODE = os.getenv("ORG_1_CODE")
ORG_2_CODE = os.getenv("ORG_2_CODE")
ORG_3_CODE = os.getenv("ORG_3_CODE")
HOSTNAME = None
RMQ_SERVER = None
HEADER = {'Content-Type': 'application/json', 'authorization': ESM_API}
client = docker.DockerClient(base_url='unix://var/run/docker.sock')

old_print = print
def timestamped_print(*args, **kwargs):
  old_print("[*]",datetime.now(), os.path.basename(__file__), *args, **kwargs)
print = timestamped_print

def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")

def init():
    global HOSTNAME
    global RMQ_SERVER
    
    if str2bool(os.getenv('DEV', 'Null')):
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
        "ORG_1_CODE": ORG_1_CODE,
        "ORG_2_CODE": ORG_2_CODE,
        "ORG_3_CODE": ORG_3_CODE,
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