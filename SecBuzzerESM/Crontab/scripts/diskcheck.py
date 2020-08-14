#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# CSTI-ChenHan Lin
# Have a good day :D

import datetime
import os
import psutil
import requests

ES_ADR = 'elasticsearch'
ES_PORT = 9200
ES_ADR_PORT = f'http://{ES_ADR}:{ES_PORT}'
DELETE_STANDARD = 85 # 容量滿85%自動移除 Log

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

def check_disk(counter:int=0):
    """檢查硬碟空間, 超過 85% 移除 index"""
    disk_used = psutil.disk_usage('/es_volume/').percent
    if disk_used > DELETE_STANDARD:
        if get_es_indices('lm'):
            del_es_index(get_es_indices('lm')[0])
            counter += 1
            check_disk(counter)
        else:
            print(f'Delete {counter} indices, Index is empty, DiskUsed: {disk_used} %\n\n')
    else:
        print(f'DiskUsed: {disk_used} %\n')

def main():
    print(f'** {datetime.date.today()} **')
    check_disk()

if __name__ == '__main__':
    main()
