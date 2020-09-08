# -*- coding: UTF-8 -*-
from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path
import subprocess
import sys

parser = ArgumentParser()
parser.add_argument("-p", "--path", help="ESM's path", dest="ESM_Path", default="/opt/SecbuzzerESM")
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
    # Check ESM path
    global lastest_ver, prev_ver, yamls
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
        prev_ver = vers[1].split('.')
    tprint(f'{bcolors.HEADER}{".".join(prev_ver)} -> {".".join(lastest_ver)}')

def update():
    cache = '' if args.cache else '--no-cache'
    if lastest_ver[0] != prev_ver[0] or FULL_UPGRADE:
        # Exec Install.sh
        # rsync + esm.env
        # remove all images
        # sys.exit
        # 本次升級需重新設定 SecBuzzerESM.env
        subprocess.call(f'rsync -a --progress . {ESMPATH}', shell=True)
        subprocess.call('docker rmi -f $(docker images -q) > /dev/null', shell=True)
        subprocess.call('bash Install.sh', shell=True)
        tprint(f'{bcolors.OKGREEN}更新完成')
        tprint(f'{bcolors.WARNING}本次升級需重新設定 SecBuzzerESM.env, 設定完畢後執行 Update_Suricata_rules.sh')
        sys.exit()
    if lastest_ver[1] != prev_ver[1] or MEDIUM_UPGRADE:
        # rsync
        # no-cache install all images
        # sys.exit
        subprocess.call(f'rsync -a --progress --exclude=SecBuzzerESM.env . {ESMPATH}', shell=True)
        for path in yamls:
            subprocess.call(f'docker-compose -f {path} build {cache}', shell=True)
            subprocess.call(f'docker-compose -f {path} pull', shell=True)
        subprocess.call('docker rmi $(sudo docker images -f "dangling=true" -q) > /dev/null', shell=True)
        tprint(f'{bcolors.OKGREEN}更新完成')        
        sys.exit()

    if lastest_ver[2] != prev_ver[2] or SMALL_UPGRADE:
        subprocess.call(f'rsync -a --progress --exclude=SecBuzzerESM.env . {ESMPATH}', shell=True)
        tprint(f'{bcolors.OKGREEN}更新完成')
        sys.exit()

    tprint(f'{bcolors.FAIL}更新失敗, 請洽 ESM 工程師')
    sys.exit(1)
    
if __name__ == "__main__":
    init()
    update()