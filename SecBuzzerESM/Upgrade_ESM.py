# -*- coding: UTF-8 -*-
from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path
import subprocess
import sys
import os

parser = ArgumentParser()
parser.add_argument("-p", "--path", help="ESM's path", dest="ESM_Path", default="/opt/SecBuzzerESM")
parser.add_argument("-C", "--cache", help="Install with cache", action="store_true")
parser.add_argument("-F", "--full", help="Full upgrade, remove all images and run Install.sh", action="store_true")
parser.add_argument("-M", "--medium", help="Medium upgrade, rebuild images and pull images", action="store_true")
parser.add_argument("-S", "--small", help="Small upgrade, just update files", action="store_true")
args = parser.parse_args()
ESMPATH = args.ESM_Path
FULL_UPGRADE = args.full
MEDIUM_UPGRADE = args.medium
SMALL_UPGRADE = args.small

vers = None
lastest_ver = None
prev_ver = None

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def tprint(*text):
    now = datetime.now().strftime("[*] %Y/%m/%d %H:%M:%S ")
    print(now, ' '.join(str(_) for _ in text) + bcolors.ENDC)

def init():
    global lastest_ver, prev_ver, yamls

    euid = os.geteuid()
    if euid != 0:
        tprint(f'{bcolors.FAIL}請使用 root 執行')
        sys.exit()
    
    # Check ESM path
    if not Path(ESMPATH).is_dir():
        tprint(f'{bcolors.FAIL}找不到 ESM 路徑, 可使用以下指令來修改 ESM 路徑')
        tprint(f'{bcolors.WARNING}python3 Upgrade_ESM.py -p <Absolute ESM path>')
        sys.exit(1)

    # grab the arg and docker-compose files
    yamls = [_ for _ in Path(ESMPATH).glob('*/docker-compose.yml')]
    
    # get Version from HISTORY.md
    with open('./HISTORY.md', 'r') as f:
        vers = [_.split(' ')[1].strip("V").strip() for _ in f.readlines() if "# V" in _]
        lastest_ver = vers[0].split('.')

    if not Path(ESMPATH+'/HISTORY.md').is_file() and not FULL_UPGRADE:
        tprint(f'{bcolors.FAIL}版本判斷失敗, 請使用 -F 參數來進行完整更新')
        sys.exit(1)

    with open(ESMPATH+'/HISTORY.md', 'r') as f:
        vers = [_.split(' ')[1].strip("V").strip() for _ in f.readlines() if "# V" in _]
        prev_ver = vers[0].split('.')

    tprint(f'{bcolors.HEADER}{".".join(prev_ver)} -> {".".join(lastest_ver)}')

def update():
    cache = '' if args.cache else '--no-cache'
    if lastest_ver == prev_ver:
        tprint(f'{bcolors.OKGREEN}已經是最新版了')
        sys.exit()

    # 更新前關閉 Container 們
    containers_count = str(subprocess.check_output('docker ps', shell=True)).count(r'\n')
    if containers_count > 3:
        tprint(f'{bcolors.OKBLUE}關閉ESM...')
        for yml in Path(ESMPATH).glob('*/docker-compose.yml'):
            subprocess.call(f'docker-compose -f {yml} --log-level ERROR down', shell=True)

    if lastest_ver[0] != prev_ver[0] or FULL_UPGRADE:
        # Exec Install.sh
        # rsync + esm.env
        # remove all images
        # sys.exit
        # 本次升級需重新設定 SecBuzzerESM.env
        subprocess.call(f'rsync -a --exclude=HISTORY.md . {ESMPATH}', shell=True)
        subprocess.call('docker rmi -f $(docker images -q) > /dev/null', shell=True)
        subprocess.call('bash Install.sh', shell=True)
        tprint(f'{bcolors.OKGREEN}更新完成')
        subprocess.call(f'rsync -ra HISTORY.md {ESMPATH}', shell=True)
        tprint(f'{bcolors.WARNING}本次升級需重新設定 SecBuzzerESM.env, 設定完畢後執行 Update_Suricata_rules.sh')
        sys.exit()

    if lastest_ver[1] != prev_ver[1] or MEDIUM_UPGRADE:
        # rsync
        # no-cache install all images
        # sys.exit
        subprocess.call(f'rsync -ra --exclude=SecBuzzerESM.env --exclude=HISTORY.md . {ESMPATH}', shell=True)
        for path in yamls:
            subprocess.call(f'docker-compose -f {path} --log-level ERROR build {cache}', shell=True)
            subprocess.call(f'docker-compose -f {path} --log-level ERROR pull', shell=True)
        subprocess.call('docker rmi $(sudo docker images -f "dangling=true" -q) > /dev/null', shell=True)
        tprint(f'{bcolors.OKGREEN}更新完成')
        subprocess.call(f'rsync -ra HISTORY.md {ESMPATH}', shell=True)
        sys.exit()

    if lastest_ver[2] != prev_ver[2] or SMALL_UPGRADE:
        subprocess.call(f'rsync -a --exclude=HISTORY.md --exclude=SecBuzzerESM.env . {ESMPATH}', shell=True)
        tprint(f'{bcolors.OKGREEN}更新完成')
        subprocess.call(f'rsync -ra HISTORY.md {ESMPATH}', shell=True)
        sys.exit()

    tprint(f'{bcolors.FAIL}更新失敗, 請洽 ESM 工程師')
    sys.exit(1)
    
if __name__ == "__main__":
    init()
    update()
