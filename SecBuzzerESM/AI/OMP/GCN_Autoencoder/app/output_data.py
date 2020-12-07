import pandas as pd
import datetime
# import csv
from elasticsearch import Elasticsearch


class OutputData:


    def __init__(self, es_server, es_port):
        
        self.es_server = es_server
        self.es_port = es_port


    def esOutput(self, alert_ip_list, test_df, start_time, end_time, nic_name):
    
        times = datetime.datetime.now()
        timestamp = times.strftime("%Y-%m-%dT%H:%M:%S.%f+08:00")
        ingest_timestamp = times - datetime.timedelta(hours = 8)
        ingest_timestamp = ingest_timestamp.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

        esoutput = []
        
        for sip in alert_ip_list:
            sip_df = test_df[test_df['SourceIP'] == sip]
            
            dst_group = sip_df.groupby(by=['DestinationIP', 'DestinationPort'], dropna=False).size().reset_index(name='Count')
            dip_port = []

            for dst in range(1, len(dst_group)):
                try:
                    dip_port.append(dst_group['DestinationIP'][dst] + ':' + str(int(dst_group['DestinationPort'][dst])))
                except:
                    dip_port.append(dst_group['DestinationIP'][dst] + ':')

            output = {}
            output['flow_id'] = ""
            output['log_time'] = ""
            output['src_ip'] = sip
            output['src_port'] = 0
            output['dest_ip'] = ""
            output['dest_port'] = 0
            output['proto'] = ""
            output['in_iface'] = nic_name
            output['timestamp'] = timestamp
            output['event_type'] = "alert"

            output['alert'] = {}
            output['alert']['category'] = "Network Service Scanning"
            output['alert']['severity'] = 2
            output['alert']['signature'] = "Network Service Scanning"
            output['alert']['action'] = ""
            output['alert']['signature_id'] = 20310001
            output['alert']['gid'] = 0

            output['reference'] = ""
            output['module'] = "IMBD"
            output['log_type'] = "traffic"
            output['dump_status'] = "0"
            output['ingest_timestamp'] = ingest_timestamp

            output['start_time'] = start_time
            output['end_time'] = end_time

            output['user_data2'] = dip_port

            esoutput.append(output)
        
        es = Elasticsearch([{"host":self.es_server, "port":self.es_port}])
        indexname = 'imbd-alert-' + start_time[:7]
        for row in esoutput:
            es.index(index = indexname, body = row, doc_type = "_doc")


    def run(self, rel_test, feature_test, rel_normal, feature_normal, normal_ip_list, ip_list, test_df, start_time, end_time, nic_name):

        alert_ip_list = set(ip_list) - set(normal_ip_list)
        self.esOutput(alert_ip_list, test_df, start_time, end_time, nic_name)

        if len(normal_ip_list) != 0:
            # 正常的IP要處理存進csv
            rel_update = rel_test[rel_test['IP'].isin(normal_ip_list)]
            feature_update = feature_test[feature_test['IP'].isin(normal_ip_list)]

            rel_normal = rel_normal[~rel_normal['IP'].isin(normal_ip_list)]
            feature_normal = feature_normal[~feature_normal['IP'].isin(normal_ip_list)]

            rel_output = pd.concat([rel_normal, rel_update])
            feature_output = pd.concat([feature_normal, feature_update])

            rel_output.to_csv('normal_rel.csv', index=False)
            feature_output.to_csv('normal_feature.csv', index=False)

        else:
            rel_normal.to_csv('normal_rel.csv', index=False)
            feature_normal.to_csv('normal_feature.csv', index=False)

