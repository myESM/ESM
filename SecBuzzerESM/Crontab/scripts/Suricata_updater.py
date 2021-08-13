# -*- coding: UTF-8 -*-
import requests
import time
import os
import json
import shutil
import hashlib
import subprocess
import random
import sys
from datetime import datetime

esm_srv_url = 'https://api.esm.cyber.cstilab.co'

esm_api_key = None
local_rules_version = None
current_rules_version = None

header = {
    'accept': '*/*',
    'Content-Type': 'application/json',
}

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def safeListGet (l, idx, default=None):
  try:
    return l[idx]
  except IndexError:
    return default

def getApiKey() -> int:
    """
    讀取 /.env 內的 API_KEY_VALUE
    """
    with open('/.env', 'r') as f:
        for line in f.readlines():
            if 'API_KEY_VALUE' in line:
                key_line = line.split('=')
                key = safeListGet(key_line, 1)
                if key:
                    return key.strip()  # 回傳去除換行符後的結果
                else:
                    return None

old_print = print
def timestamped_print(*args, **kwargs):
  old_print("[*]",datetime.now(), os.path.basename(__file__), *args, **kwargs)
print = timestamped_print

def downloadRulesAndCheck(version:int, path:str='/tmp/rules.tgz'):
    """Download rules file and check md5 hash
    param: Rules version
    param: save file path
    """
    file_md5 = requests.get(f'{esm_srv_url}/esmapi/web/file/getmd5/it/{current_rules_version}/',
    headers=header).json().get('md5')
    response = requests.get(f'{esm_srv_url}/esmapi/web/file/download/it/{version}', headers=header, stream=True)
    with open(path, 'wb') as f:
        shutil.copyfileobj(response.raw, f)
    if file_md5 == md5(path):
        return True
    else:
        return False

if __name__ == "__main__":
    time.sleep(random.randint(0,15))

    esm_api_key = getApiKey()
    if esm_api_key:
        header.update({'authorization': esm_api_key})
    else:
        print('ESM API key not found! Bye~')
        sys.exit(1)
    
    try:
        version_check = requests.post(f'{esm_srv_url}/esmapi/web/file/fileVersion',
        headers=header, json={'TypeCode': 'it'}).json().get('FileVersion')
        current_rules_version = version_check
    except:
        print('Rule Server Connection fail, Bye!')
        sys.exit(1)

    if not current_rules_version: # can't get latest version
        print('Get current rules version fail, Bye~')
        sys.exit(1)

    lv_path = "/tmp/local_rules_version" # local version file path
    if os.path.isfile(lv_path):
        with open(lv_path, 'r') as f:
            local_rules_version = f.readline().strip()
    else:
        local_rules_version = 0
    
    if current_rules_version != local_rules_version:
        print(f'New version found! rules will update to {current_rules_version}')
        for i in range(6): 
            if i: print('Rules download fail, Retry',i)  # print retry times
            download_status = downloadRulesAndCheck(current_rules_version)
            if download_status:
                subprocess.call('mkdir -p /tmp/rules', shell=True)
                subprocess.call('tar zxf /tmp/rules.tgz -C /tmp/rules', shell=True)
                subprocess.call('chown 1000:1000 /tmp/* -R',shell=True)
                subprocess.call('rsync -a --delete /tmp/rules /Suricata_rules/',shell=True)
                subprocess.call('rm -rf /tmp/rules /tmp/rules.tgz',shell=True)
                print('Restarting Suricata')
                time.sleep(3)
                subprocess.call('curl -XPOST --unix-socket /var/run/docker.sock -H "Content-Type: application/json" http://localhost/containers/suricata/restart',shell=True)
                subprocess.call('rm /tmp/local_rules_version 2>/dev/null',shell=True)
                subprocess.call(f'echo {current_rules_version} > /tmp/local_rules_version',shell=True)
                print('Done!')
                break
            else:
                continue
        else:
            print('Md5 check fail or file download fail :(')
            sys.exit(1)