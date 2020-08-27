#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# CSTI-ChenHan Lin
# Have a good day :D

import datetime
import os
import psutil
import requests
from datetime import datetime

ES_ADR = 'elasticsearch'
ES_PORT = 9200
ES_ADR_PORT = f'http://{ES_ADR}:{ES_PORT}'
DELETE_STANDARD = 85 # 容量滿85%自動移除 Log
INDEICES_PREFIX = ['winlogbeat', 'cic']

def tprint(*text):
    now = datetime.now().strftime("[*] %Y/%m/%d %H:%M:%S ")
    print(now, ' '.join(str(_) for _ in text))

def get_es_indices(index_prefix:str = None) -> list:
    """取得所有 index name"""
    if index_prefix:
        es = requests.get(f'{ES_ADR_PORT}/_stats').json()
        return sorted([index_name for index_name in es['indices'] 
                        if index_name.startswith(index_prefix)])
    else:
        es = requests.get(f'{ES_ADR_PORT}/_stats').json()
        return sorted([index_name for index_name in es['indices']])

def del_es_index(index_name:str=None) -> dict:
    """移除指定 index"""
    if index_name:
        return requests.delete(f'{ES_ADR_PORT}/{index_name}').json()
    else:
        return None

def indices_available(indices:list) -> int:
    """
    回傳還有資料的 index 數量
    """
    available = []
    for index in indices:
        if get_es_indices(index)[:-1]:
            available.append(True)
        else:
            available.append(False)
    return sum(available)

def check_disk(counter:int=0):
    """檢查硬碟空間, 超過 85% 移除 index"""
    disk_used = psutil.disk_usage('/es_volume/').percent
    if disk_used > DELETE_STANDARD:
        if indices_available(INDEICES_PREFIX):
            for index in INDEICES_PREFIX:
                index_data = get_es_indices(index)[:-1]
                if index_data:
                    print(index_data[0], del_es_index(index_data[0]))
            check_disk(counter)
            counter += 1
    else:
        tprint(f'DiskUsed: {disk_used} %\n')
        if counter: tprint(f'Remove {counter} index')


def main():
    check_disk()

if __name__ == '__main__':
    main()
