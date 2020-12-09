import numpy as np
import pandas as pd
import datetime
# import csv
# import os
import ipaddress
# from collections import Counter
from elasticsearch import Elasticsearch, helpers

from app.feature_extract import *


class LoadES:


    def __init__(self, es_server, es_port):
        
        self.es_server = es_server
        self.es_port = es_port


    def loadEsData(self, es_index, query_start, query_end):

        es = Elasticsearch([{"host":self.es_server, "port":self.es_port}])
        if es.indices.exists(index=es_index):
            
            search_query = { "query": { "bool": { "should": 
                                                 [{ "range": { "Timestamp": { 
                                                     "gte": query_start, "lte": query_end}}}]}}}

            res = helpers.scan(client = es, scroll = "2m", query = search_query, index = es_index,
                               preserve_order = True)

            data = []
            for item in res:
                info = item["_source"]
                data_dict = dict()
                data_dict["Time"] = info["Timestamp"] if "Timestamp" in info.keys() else None
                data_dict["SourceIP"] = info["Src IP"] if "Src IP" in info.keys() else None
                data_dict["DestinationIP"] = info["Dst IP"] if "Dst IP" in info.keys() else None
                data_dict["SourcePort"] = info["Src Port"] if "Src Port" in info.keys() else None
                data_dict["DestinationPort"] = info["Dst Port"] if "Dst Port" in info.keys() else None          
                data_dict["Protocol"] = info["Protocol"] if "Protocol" in info.keys() else None
                data.append(data_dict)
                # nic_name = info["nic_name"] if "nic_name" in info.keys() else None
                nic_name = 'experimental_data'
            df = pd.DataFrame(data)
        
        return df, nic_name
    

    def intranetFilter(self, df):
        # 過濾屬於“外網”ip的流量
        df['src_private'] = df["SourceIP"].apply(lambda x: ipaddress.ip_address(x).is_private)
        df['dst_private'] = df["DestinationIP"].apply(lambda x: ipaddress.ip_address(x).is_private)
        df = df.loc[(df['src_private']) & (df['dst_private'])]
        df.drop(['src_private', 'dst_private'], axis=1, inplace=True)
        df = df.reset_index(drop=True)

        return df
    
    
    def broadcastFilter(self, df):
        # 過濾屬於“廣播”ip的流量
        df = df.loc[df['SourceIP'].str.find('.255') == -1]
        df = df.loc[df['DestinationIP'].str.find('.255') == -1]
        df = df.reset_index(drop=True)

        return df


    def relDfToDict(self, rel):
        
        rel_dict = {}
        for i in range(len(rel)):
            rel_dict[list(rel['IP'])[i]] = list(rel['dst ip'])[i]
            
        return rel_dict


    def run(self, es_index, test_start_time, test_end_time):

        test_df, nic_name = self.loadEsData(es_index, test_start_time, test_end_time)

        test_df = self.intranetFilter(test_df)
        test_df = self.broadcastFilter(test_df)

        rel_test_all, feature_test_all = feature_run(test_df)

        try:
            rel_normal = pd.read_csv('normal_rel.csv')
            feature_normal = pd.read_csv('normal_feature.csv')

            def dipStrToSet(x):
                x_split = x[1:-1].split(', ')
                dip = set()
                for i in range(len(x_split)):
                    dip.add(x_split[i][1:-1])

                return dip
                
            rel_normal['dst ip'] = rel_normal["dst ip"].apply(lambda x: dipStrToSet(x))
            
        except:

            period = (datetime.datetime.strptime(test_end_time, '%Y-%m-%dT%H:%M:%S.%f+08:00') - datetime.datetime.strptime(test_start_time, '%Y-%m-%dT%H:%M:%S.%f+08:00')).seconds
            train_start_time = datetime.datetime.strptime(test_start_time, '%Y-%m-%dT%H:%M:%S.%f+08:00') - datetime.timedelta(seconds = period)
            train_start_time = train_start_time.strftime("%Y-%m-%dT%H:%M:%S.%f+08:00")
            print(train_start_time)
            train_end_time = datetime.datetime.strptime(test_end_time, '%Y-%m-%dT%H:%M:%S.%f+08:00') - datetime.timedelta(seconds = period)
            train_end_time = train_end_time.strftime("%Y-%m-%dT%H:%M:%S.%f+08:00")
            
            normal_df, _ = self.loadEsData(es_index, train_start_time, train_end_time)

            normal_df = self.intranetFilter(normal_df)
            normal_df = self.broadcastFilter(normal_df)

            rel_normal, feature_normal = feature_run(normal_df)
            
        ip_list = sorted(list(feature_normal['IP']) and list(feature_test_all['IP']))

        rel_train = rel_normal[rel_normal['IP'].isin(ip_list)]

        feature_train = feature_normal[feature_normal['IP'].isin(ip_list)]

        rel_test = rel_test_all[rel_test_all['IP'].isin(ip_list)]
        feature_test = feature_test_all[feature_test_all['IP'].isin(ip_list)]
        
        rel_initial = rel_test_all[~rel_test_all['IP'].isin(ip_list)]
        feature_initial = feature_test_all[~feature_test_all['IP'].isin(ip_list)]
        rel_normal = rel_normal.append(rel_initial, ignore_index=True)
        feature_normal = feature_normal.append(feature_initial, ignore_index=True)

        rel_train_dict = self.relDfToDict(rel_train)
        rel_test_dict = self.relDfToDict(rel_test)

        feature_train.drop(['IP'], axis=1, inplace=True)
        feature_train_mat = np.array(feature_train).tolist()
        
        feature_test_mat = feature_test.copy()
        feature_test_mat.drop(['IP'], axis=1, inplace=True)
        feature_test_mat = np.array(feature_test_mat).tolist()

        return rel_train_dict, rel_test_dict, feature_train_mat, feature_test_mat, ip_list, rel_test, feature_test, rel_normal, feature_normal, test_df, nic_name

