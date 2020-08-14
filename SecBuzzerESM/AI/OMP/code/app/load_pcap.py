import os
import dpkt
import socket
import datetime
import pandas as pd
import numpy as np
import ipaddress


class LoadPcap:


    def __init__(self, file_name, query_start, period, network_segment):
        
        self.file_name = file_name
        self.query_start = query_start
        self.period = period
        self.network_segment = network_segment


    def arpProcess(self, eth):
        arp = eth.arp
        src_ip = socket.inet_ntoa(arp.spa)
        src_port = np.nan
        dst_ip = socket.inet_ntoa(arp.tpa)
        dst_port = np.nan
        
        return [src_ip, src_port, dst_ip, dst_port]


    def normalProcess(self, eth):
        ip = eth.data
        if ip.v == 4:   
            src_ip = socket.inet_ntoa(ip.src)
            dst_ip = socket.inet_ntoa(ip.dst)
            
        elif ip.v == 6:
            src_ip = socket.inet_ntop(socket.AF_INET6, ip.src)
            dst_ip = socket.inet_ntop(socket.AF_INET6, ip.dst)
            try:
                src_ip = IPNetwork(src_ip).ipv4()
            except:
                pass
            try:
                dst_ip = IPNetwork(dst_ip).ipv4()
            except:
                pass
            src_ip = str(src_ip).split('/')[0]
            dst_ip = str(dst_ip).split('/')[0]
              
        try:
            src_port = ip.data.sport
            dst_port = ip.data.dport
        except:
            src_port = np.nan
            dst_port = np.nan
            
        return [src_ip, src_port, dst_ip, dst_port]


    def pcapProcess(self, pcap):
        pcap_list = list()
        count = 0
        for ts, buf in pcap:

            count += 1
            if count % 200000 == 0:
                print(count/10000)
                
            time = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%dT%H:%M:%S.%f+08:00")
            
            try:
                eth = dpkt.ethernet.Ethernet(buf)
            except:
                print('pass')
                
            try:
                # 2054 是 ARP
                if eth.type == 2054:
                    pcap_list.append([time]+self.arpProcess(eth))

                else:
                    pcap_list.append([time]+self.normalProcess(eth))

            except:
                pass

        return pd.DataFrame(pcap_list, columns=["Time","Source","SrcPort","Destination","DstPort"])        


    def readPcap(self, filename):
        df = pd.DataFrame()
        for f in filename:
            file = open("data/" + f, "rb")
            pcap = dpkt.pcap.Reader(file)
            df_pcap = self.pcapProcess(pcap)
            df = pd.concat([df, df_pcap])
        
        # print(df)
        return df


    def timeFilter(self, df, start_time, end_time):
        # df過濾時間
        df_time = df.loc[(df.Time >= start_time) & (df.Time < end_time)]

        return df_time

    '''
    def dataPreprocess(self, df):

        # 這裡最後要改成撈內網全部的流量或改成可以動態調整要全內網或部分網段。
        # # 過濾屬於內網ip的流量
        # group = df.groupby(["Source", "Destination"]).size().reset_index(name='Count')
        
        # group['src_private'] = group['Source'].apply(lambda x: ipaddress.ip_address(x).is_private)
        # group['dst_private'] = group['Destination'].apply(lambda x: ipaddress.ip_address(x).is_private)
        # group = group.loc[(group['src_private']) & (group['dst_private'])]
        # group.drop(['src_private', 'dst_private'], axis=1, inplace=True)
        # df_omp = group.reset_index(drop=True)

        network_segment = self.network_segment.split(',')
        
        # 將相同["Srcip", "Dstip"] 的groupby 在一起
        group = dict(df.groupby(["Source", "Destination"]).size())
        
        # 過濾出內網（77網段下）的流量
        src_dst = []
        for k in group.keys():

            segment_s = False
            segment_d = False
            
            for i in network_segment:
                if k[0].find(i) == 0:
                    segment_s = True
                if k[1].find(i) == 0:
                    segment_d = True
                    
            if segment_s == True and segment_d == True:
                src_dst.append([k[0], k[1], group[k]])
                          
        # 再次組成dataframe
        df_omp = pd.DataFrame(src_dst, columns = ["Source", "Destination", "Count"])


        return df_omp
    '''

    
    def dataPreprocess(self, df):

        # 這裡最後要改成撈內網全部的流量或改成可以動態調整要全內網或部分網段。
        # 過濾屬於內網ip的流量
        group = df.groupby(["Source", "Destination"]).size().reset_index(name='Count')
        
        group['src_private'] = group['Source'].apply(lambda x: ipaddress.ip_address(x).is_private)
        group['dst_private'] = group['Destination'].apply(lambda x: ipaddress.ip_address(x).is_private)
        group = group.loc[(group['src_private']) & (group['dst_private'])]
        group.drop(['src_private', 'dst_private'], axis=1, inplace=True)
        df_omp = group.reset_index(drop=True)


        # network_segment = self.network_segment.split(',')
        
        # # 將相同["Srcip", "Dstip"] 的groupby 在一起
        # group = dict(df.groupby(["Source", "Destination"]).size())
        
        # # 過濾出內網（77網段下）的流量
        # src_dst = []
        # for k in group.keys():

        #     segment_s = False
        #     segment_d = False
            
        #     for i in network_segment:
        #         if k[0].find(i) == 0:
        #             segment_s = True
        #         if k[1].find(i) == 0:
        #             segment_d = True
                    
        #     if segment_s == True and segment_d == True:
        #         src_dst.append([k[0], k[1], group[k]])
                          
        # # 再次組成dataframe
        # df_omp = pd.DataFrame(src_dst, columns = ["Source", "Destination", "Count"])


        return df_omp
    
    

    def run(self):
        print(self.query_start) 
        print("========== load data ==========")
        
        
        # filename
        filename = []
        # file_time_now = datetime.datetime.now()
        # file_time = file_time_now
        file_time = datetime.datetime.strptime(self.query_start, '%Y-%m-%dT%H:%M:%S.%f')
        file_time = file_time - datetime.timedelta(hours = 1)
        file_cnt = self.period + 1
        for _ in range(file_cnt):
            linux_filename = file_time - datetime.timedelta(hours = 8)
            filename.append(linux_filename.strftime('%m-%d-%H') + '.pcap')
            file_time = file_time + datetime.timedelta(hours = 1)

        print('filename: ' + str(filename))
        
        df = self.readPcap(filename)

        # df = self.readPcap(self.file_name)

        start_time = datetime.datetime.strptime(self.query_start, '%Y-%m-%dT%H:%M:%S.%f')
        end_time = start_time + datetime.timedelta(hours = self.period)
        now_end = end_time.strftime("%Y-%m-%dT%H:%M:%S.%f") 

        abnor_df = self.timeFilter(df, self.query_start, now_end)
        abnor_data = self.dataPreprocess(abnor_df)
        # print(abnor_data)
        abnor_iplist = list(abnor_data['Source']) + list(abnor_data['Destination'])
        abnor_ip_list = sorted(list(set(abnor_iplist)))

        # 控制多少比例的 IP 數量為上班/下班
        # 怎麼知道公司總共有多少 ip
        work_ip_cnt = 254 * 0.29527

        if len(abnor_ip_list) > work_ip_cnt:
            week_threshold = 'weekday'
        else:
            week_threshold = 'weekend'


        if int(self.query_start[11:13]) >= 8 and int(self.query_start[11:13]) < 20:
            work_break = 'work'
        elif int(self.query_start[11:13]) < 8 or int(self.query_start[11:13]) >= 20:
            work_break = 'break'


        folder_name = './' + week_threshold + '_' + work_break + '/'
        filepath = folder_name + 'omp_and_frequency.csv'
        print('folder name: ' + week_threshold + '_' + work_break)

        if os.path.isfile(filepath):
            # print('no empty')

            nor_data = []

        else:
            print('first time')


            # filename
            filename = []
            file_time = datetime.datetime.strptime(self.query_start, '%Y-%m-%dT%H:%M:%S.%f') - datetime.timedelta(hours = 24)
            file_time = file_time - datetime.timedelta(hours = 1)
            file_cnt = self.period + 1
            for _ in range(file_cnt):
                linux_filename = file_time - datetime.timedelta(hours = 8)
                filename.append(linux_filename.strftime('%m-%d-%H') + '.pcap')
                file_time = file_time + datetime.timedelta(hours = 1)
            
            print('normal filename: ' + str(filename))
            
            df = self.readPcap(filename)

            # 以前一個小時為比較時間 Ｖ
            # 與前一天同一個時間區間比較 Ｘ
            nor_start_time = start_time - datetime.timedelta(hours = 1)
            nor_query_start = nor_start_time.strftime("%Y-%m-%dT%H:%M:%S.%f")
            nor_end_time = end_time - datetime.timedelta(hours = 1)
            nor_end_time = nor_end_time.strftime("%Y-%m-%dT%H:%M:%S.%f")

            nor_df = self.timeFilter(df, nor_query_start, nor_end_time)
            nor_data = self.dataPreprocess(nor_df)
            # print(nor_data)
        
        print('start time: ' + str(self.query_start)[:19])

        return abnor_df, nor_data, abnor_data, folder_name

