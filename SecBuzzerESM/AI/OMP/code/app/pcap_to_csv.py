import glob
import pandas as pd
import dpkt
import datetime
import socket
import ipaddress
import os
import numpy as np



class PcapToCsv:


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
            file = open(f, "rb")
            pcap = dpkt.pcap.Reader(file)
            df_pcap = self.pcapProcess(pcap)
            df = pd.concat([df, df_pcap])
        
        return df


    def filterIntranetTraffic(self, df):
        df = df.dropna(subset=['Source', 'Destination', 'Time'])
        df['src_private'] = df['Source'].apply(lambda x: ipaddress.ip_address(x).is_private)
        df['dst_private'] = df['Destination'].apply(lambda x: ipaddress.ip_address(x).is_private)
        df = df.loc[(df['src_private']) & (df['dst_private'])]
        df.drop(['src_private', 'dst_private'], axis=1, inplace=True)
        df = df.reset_index(drop=True)

        return df


    def run(self, file_time):
        
        file_time = file_time - datetime.timedelta(hours = 8)
        file_time = file_time.strftime("%m-%d-%H")

        file_list = glob.glob('./data/' + file_time + '*.pcap*')
        file_list.sort()
        print(file_list)
        df = self.readPcap(file_list)
        # df = self.filterIntranetTraffic(df)
        
        # file_time = file_time - datetime.timedelta(hours = 8)
        # file_time = file_time.strftime("%m-%d-%H")
        csv_filename = glob.glob('./data/' + file_time + '*.csv')
        csv_name = file_time + '_' + str(len(csv_filename))
        df.to_csv('./data/' + csv_name + '.csv', index=False)
        
        # remove pcap file
        print(file_list)
        for filename in file_list:
            os.remove(filename)

