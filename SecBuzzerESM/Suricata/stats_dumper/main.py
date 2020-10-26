import time
import os
import json
import requests
from pathlib import Path
from datetime import datetime
import socket

FIELDS = ["capture.kernel_packets",
          "capture.kernel_drops",
          "decoder.pkts",
          "decoder.bytes",
          "decoder.tcp",
          "decoder.udp",
          "decoder.icmpv4",
          "decoder.icmpv6",
          "detect.alert",]

STATS_PATH = "/var/log/suricata/stats.log"

ESM_API = os.getenv("ESM_API")
ORG_1_CODE = os.getenv("ORG_1_CODE")
ORG_2_CODE = os.getenv("ORG_2_CODE")
ORG_3_CODE = os.getenv("ORG_3_CODE")
HOSTNAME = None
HEADER = {'authorization': ESM_API}

def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")

def follow(thefile):
    '''generator function that yields new lines in a file
    '''
    # seek the end of the file
    thefile.seek(0, os.SEEK_END)
    
    # start infinite loop
    while True:
        # read last line of file
        line = thefile.readline()
        # sleep if file hasn't been updated
        if not line:
            time.sleep(0.1)
            continue
        yield line

old_print = print
def timestamped_print(*args, **kwargs):
  old_print(datetime.now(), *args, **kwargs)
print = timestamped_print

if __name__ == '__main__':
    if str2bool(os.getenv('DEV')):
        RMQ_SERVER = "https://test.api.secbuzzer.co"
        print("RUNNING WITH DEV MODE")
    else:
        RMQ_SERVER = "https://api.esm.secbuzzer.co"

    with open('/HOSTNAME', 'r') as f:
        HOSTNAME = f.readline().strip()

    queue_stats = requests.get(f"{RMQ_SERVER}/esmapi/queues/%2F/Suricata_Stats", headers=HEADER).json()
    print(queue_stats)
    if queue_stats.get('error'):
        print('Creating RMQ queue...')
        requests.put(f"{RMQ_SERVER}/esmapi/queues/%2F/Suricata_Stats", headers=HEADER)
        print('Creating RMQ queue success')

    while not Path(STATS_PATH).is_file():
        print('Waiting for stats.log!')
        time.sleep(1)

    print("Starting tail stats.log")
    logfile = open(STATS_PATH,"r")
    loglines = follow(logfile)
    # iterate over the generator
    json_Data = {}
    for line in loglines:
        if any(line.split('|')[0].strip() in _ for _ in FIELDS):
            json_Data.update({line.split('|')[0].strip(): line.split('|')[2].strip()})
            if len(json_Data) == len(FIELDS):
                json_Data.update({"ORG_1_CODE": ORG_1_CODE,
                                "ORG_2_CODE": ORG_2_CODE,
                                "ORG_3_CODE": ORG_3_CODE,
                                "HOSTNAME": HOSTNAME})
                datas = {"properties":{"Content-Type":"application/json"},"routing_key":"Suricata_Stats","payload":json.dumps(json_Data),"payload_encoding":"string"}
                resp = requests.post(f"{RMQ_SERVER}/esmapi/exchanges/%2F/amq.default/publish", headers=HEADER, data=json.dumps(datas)).json()
                print(json_Data)
                json_Data={}
