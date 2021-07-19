import apscheduler
import json
import os
import requests
import subprocess
import time
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

ESM_API = os.getenv("ESM_API")
ORG_1_CODE = os.getenv("ORG_1_CODE")
ORG_2_CODE = os.getenv("ORG_2_CODE")
ORG_3_CODE = os.getenv("ORG_3_CODE")
IF_NAME = os.getenv("IF_NAME")
HEADER = {'authorization': ESM_API}
HOSTNAME = None
RMQ_SERVER = None

old_print = print
def timestamped_print(*args, **kwargs):
  old_print(datetime.now(), *args, **kwargs)
print = timestamped_print

def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")

def init():
    global RMQ_SERVER
    global HOSTNAME
    if str2bool(os.getenv('DEV', 'Flase')):
        RMQ_SERVER = "https://api.esm.cyber.cstilab.co"
        print("RUNNING WITH DEV MODE")
    else:
        RMQ_SERVER = "https://api.esm.cyber.cstilab.co"

    with open('/HOSTNAME', 'r') as f:
        HOSTNAME = f.readline().strip()

    queue_stats = requests.get(f"{RMQ_SERVER}/esmapi/queues/%2F/VNSTAT", headers=HEADER).json()

    if queue_stats.get('error'):
        print('Creating RMQ queue...')
        requests.put(f"{RMQ_SERVER}/esmapi/queues/%2F/VNSTAT", headers=HEADER)
        print('Creating RMQ queue success')

def main():
    global STATISTICS
    STATISTICS = None
    scheduler = BackgroundScheduler()
    job = scheduler.add_job(traffic_statistics, 'interval', seconds=900, max_instances=2, next_run_time=datetime.now())
    scheduler.start()

    while True:
        if STATISTICS:
            _ = json.loads(STATISTICS)
            DATA = {
                'rx':{'bytespersecond': _['rx']['bytespersecond'],
                    'bytes': _['rx']['bytes'],
                    'packets': _['rx']['packets'],
                },
                'tx':{'bytespersecond': _['tx']['bytespersecond'],
                    'bytes': _['tx']['bytes'],
                    'packets': _['tx']['packets'],
                },
            }
            DATA.update({"ORG_1_CODE": ORG_1_CODE,
                            "ORG_2_CODE": ORG_2_CODE,
                            "ORG_3_CODE": ORG_3_CODE,
                            "HOSTNAME": HOSTNAME})
            print(DATA)
            datas = {"properties":{"Content-Type":"application/json"},"routing_key":"VNSTAT","payload":json.dumps(DATA),"payload_encoding":"string"}    
            resp = requests.post(f"{RMQ_SERVER}/esmapi/exchanges/%2F/amq.default/publish", headers=HEADER, data=json.dumps(datas)).json()
            print(resp)
        STATISTICS, _ = None, None
        time.sleep(5)

def traffic_statistics():
    global STATISTICS
    global IF_NAME
    STATISTICS = subprocess.check_output( ['vnstat','-tr', '900','-i', IF_NAME, '--json'] )

if __name__ == '__main__':
    init()
    main()