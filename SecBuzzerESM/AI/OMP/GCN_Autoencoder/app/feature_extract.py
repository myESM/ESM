import numpy as np
import pandas as pd
import ipaddress
from collections import Counter


def getOMPDict(df):

    dic = {}
    for ip in set(df['SourceIP']):
        dic[ip] = set(df[df['SourceIP'] == ip]['DestinationIP'])
        dic[ip].add(ip)
    dic_df = pd.DataFrame({'IP':list(dic.keys()), 'dst ip':list(dic.values())})

    return dic_df


def portCount(ip_df):   
    s = 0
    m = 0
    l = 0
    n = 0
    for port in list(ip_df['SourcePort']):
        try:
            if int(port) <= 1023:
                s = s+1
            elif int(port) >= 1024 and port <= 49151:
                m = m+1
            elif int(port) >= 49152:
                l = l+1
        except:
            n = n+1
            
    return [s, m, l, n]


def protocalCount(ip_df, protocol_list):
    protocol = Counter(ip_df["Protocol"])
    protocal_count = np.zeros(len(protocol_list))
    try:
        for k,v in protocol.items():
            protocal_count[protocol_list.index(str(k))] = v
    except:
        pass
    
    return protocal_count.tolist()


def feature(df):
    protocol_list = sorted(list(set(df["Protocol"])))
    protocol_list_new = [str(x) for x in protocol_list]
    ip_list = sorted(list(set(df['SourceIP'])))
    
    port_count = []
    protocal_count = []

    for ip in ip_list:
        ip_df = df[df['SourceIP'] == ip]
        port_count.append(portCount(ip_df))
        protocal_count.append(protocalCount(ip_df, protocol_list_new))

    print(port_count)
    print(protocal_count)

    port_dataframe = pd.DataFrame(port_count)
    port_dataframe.columns = ['Well_Known_Port', 'Registered_Port', 'Dynamic_Port', 'Null_Port']
    prot_dataframe = pd.DataFrame(protocal_count)    
    prot_dataframe.columns = protocol_list_new

    features_df = pd.concat([pd.DataFrame({'IP':ip_list}), port_dataframe, prot_dataframe], axis=1)

    return features_df


def feature_run(df):

    dic = getOMPDict(df)
    features_df = feature(df)

    return dic, features_df

