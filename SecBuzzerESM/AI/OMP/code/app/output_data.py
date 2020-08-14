import pandas as pd
import numpy as np
import datetime
import json
import csv
import os
import glob


class OutputData:


    def __init__(self, period, server):
        
        self.period = period
        self.server = server
        
    '''
    def jsonOutput(self, all_value_matrix, all_infected_ip, all_dip_list, abnor_df, folder_name):

        start_time = datetime.datetime.strptime(self.query_start, '%Y-%m-%dT%H:%M:%S.%f')
        end_time = start_time + datetime.timedelta(hours = self.period)
        now_end = end_time.strftime("%Y-%m-%dT%H:%M:%S.%f")


        output = {}

        output['StartTime'] = self.query_start
        output['EndTime'] = now_end

        output['arp_scan'] = {}
        output['arp_scan']['Source'] = {}
        output['arp_scan']['Destination'] = {}

        output['Suspicious'] = {}
        output['Suspicious']['Source'] = {}
        output['Suspicious']['Destination'] = {}

        cnt = 0

        for vmatrix_number in range(len(all_value_matrix)):
            if len(all_value_matrix[vmatrix_number]) != 0:
                
                #被認為是惡意要輸出的matrix
                for sip in all_infected_ip[vmatrix_number]:
                    #sip：'147.32.84.165'
                    src_df = abnor_df.loc[abnor_df['Source'].str.find(sip) == 0]

                    for dip in all_dip_list[vmatrix_number]:
                        #dip：'109.200.239.148', '112.205.182.117', '115.97.135.112'
                        
                        dst_df = src_df.loc[src_df['Destination'].str.find(dip) == 0]
                        
                        dst_df_dropna = dst_df.dropna() 
                        dst_df_na = pd.concat([dst_df, dst_df_dropna]).drop_duplicates(keep=False)

                        dict_src_dst_group = dict(dst_df_dropna.groupby(["SrcPort", "DstPort"]).size())


                        if len(dst_df_na) != 0:

                            if sip not in output['arp_scan']['Source'].keys():
                                output['arp_scan']['Source'][sip] = {}
                            output['arp_scan']['Source'][sip][dip] = {}
                            
                            output['arp_scan']['Source'][sip][dip]['SrcPort'] = "NaN"
                            output['arp_scan']['Source'][sip][dip]['DstPort'] = "NaN"

                            output['arp_scan']['Source'][sip][dip]['Time'] = list(dst_df_na['Time'])
                            cnt = cnt + len(list(dst_df_na['Time']))

                        if len(dict_src_dst_group.keys()) != 0:

                            if sip not in output['Suspicious']['Source'].keys():
                                output['Suspicious']['Source'][sip] = {}
                            output['Suspicious']['Source'][sip][dip] = {}
                            
                            count_sport = 1

                            for k in dict_src_dst_group:
                                
                                output['Suspicious']['Source'][sip][dip]['SrcPort' + str(count_sport)] = k[0]
                                output['Suspicious']['Source'][sip][dip]['DstPort' + str(count_sport)] = k[1]
                                
                                sport = dst_df_dropna.loc[dst_df_dropna['SrcPort'] == k[0]]
                                sport_dport = sport.loc[sport['DstPort'] == k[1]]
                                
                                output['Suspicious']['Source'][sip][dip]['Time' + str(count_sport)] = list(sport_dport['Time'])
                                count_sport += 1
                                cnt = cnt + len(list(sport_dport['Time']))


                for dip in all_dip_list[vmatrix_number]:       
                    
                    dst_df = abnor_df.loc[abnor_df['Destination'].str.contains(dip)]
                    for sip in all_infected_ip[vmatrix_number]:
            
                        src_df = dst_df.loc[dst_df['Source'].str.contains(sip)]
            
                        src_df_dropna = src_df.dropna() 
                        src_df_na = pd.concat([src_df, src_df_dropna]).drop_duplicates(keep=False)

                        dict_src_dst_group = dict(src_df_dropna.groupby(["SrcPort", "DstPort"]).size())
            
                        if len(src_df_na) != 0:

                            if dip not in output['arp_scan']['Destination'].keys():
                                output['arp_scan']['Destination'][dip] = {}
                            output['arp_scan']['Destination'][dip][sip] = {}
                            
                            output['arp_scan']['Destination'][dip][sip]['SrcPort'] = "NaN"
                            output['arp_scan']['Destination'][dip][sip]['DstPort'] = "NaN"
                    
                            output['arp_scan']['Destination'][dip][sip]['Time'] = list(src_df_na['Time'])
                            

                        if len(dict_src_dst_group.keys()) != 0:
            
                            if dip not in output['Suspicious']['Destination'].keys():
                                output['Suspicious']['Destination'][dip] = {}
                            output['Suspicious']['Destination'][dip][sip] = {}
                            
                            count_dport = 1  
            
                            for k in dict_src_dst_group:
                                output['Suspicious']['Destination'][dip][sip]['SrcPort' + str(count_dport)] = k[0]
                                output['Suspicious']['Destination'][dip][sip]['DstPort' + str(count_dport)] = k[1]
                                
                                sport = src_df.loc[src_df['SrcPort'] == k[0]]
                                sport_dport = sport.loc[sport['DstPort'] == k[1]]
                        
                                output['Suspicious']['Destination'][dip][sip]['Time' + str(count_dport)] = list(sport_dport['Time'])
                                count_dport += 1
                        

        print(cnt)           

        # filename = folder_name + 'suspicious_alert_' + self.query_start[8:10] + '_' + self.query_start[11:13]
        # with open(filename+'.json','a') as outfile:
        #     json.dump(output,outfile,ensure_ascii=False)
        #     outfile.write('\n')
    ''' 


    def esOutput(self, all_value_matrix, all_infected_ip, all_dip_list, abnor_df, folder_name, query_start, query_end):

        # start_time = datetime.datetime.strptime(self.query_start, '%Y-%m-%dT%H:%M:%S.%f')
        # end_time = start_time + datetime.timedelta(hours = self.period)
        # start_time = query_start.strftime("%Y-%m-%dT%H:%M:%S.%f+08:00")
        # end_time = query_end.strftime("%Y-%m-%dT%H:%M:%S.%f+08:00")

        complete_time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f+08:00")

        esoutput = []

        decile = 254 / 10.0

        for vmatrix_number in range(len(all_value_matrix)):
            if len(all_value_matrix[vmatrix_number]) != 0:
                for sip in all_infected_ip[vmatrix_number]:
                    src_df = abnor_df.loc[abnor_df['Source'].str.find(sip) == 0]

                    # 加入計算風險指數
                    dst_cnt = len(set(src_df.Destination) & set(all_dip_list[vmatrix_number]))
                    if dst_cnt == 0:
                        score = 0.0
                    else:
                        score = round(dst_cnt / decile) 


                    for dip in all_dip_list[vmatrix_number]:
                        dst_df = src_df.loc[src_df['Destination'].str.find(dip) == 0]
                        
                        dst_df_dropna = dst_df.dropna()
                        dict_src_dst_group = dict(dst_df_dropna.groupby(["SrcPort", "DstPort"]).size())

                        if len(dict_src_dst_group.keys()) != 0:
                            for k in dict_src_dst_group:
                                sport = dst_df_dropna.loc[dst_df_dropna['SrcPort'] == k[0]]
                                sport_dport = sport.loc[sport['DstPort'] == k[1]]
                                for log_time in sport_dport['Time']:
                                    output = {}
                                    output['Start_Time'] = query_start
                                    output['End_Time'] = query_end
                                    output['Category'] = "Suspicious"
                                    output['Source_IP'] = sip
                                    output['Destination_IP'] = dip
                                    output['Source_Port'] = str(int(k[0]))
                                    output['Destination_Port'] = str(int(k[1]))
                                    output['Time'] = log_time
                                    output['Score'] = score
                                    output['Complete_Time'] = complete_time
                                    
                                    esoutput.append(output)

                        # 取出port是nan的
                        dst_df_na = pd.concat([dst_df, dst_df_dropna]).drop_duplicates(keep=False)

                        if len(dst_df_na) != 0:
                            for log_time in dst_df_na['Time']:
                                output = {}
                                output['Start_Time'] = query_start
                                output['End_Time'] = query_end
                                output['Category'] = "arp_scan"
                                output['Source_IP'] = sip
                                output['Destination_IP'] = dip
                                output['Source_Port'] = "NaN"
                                output['Destination_Port'] = "NaN"
                                output['Time'] = log_time
                                output['Score'] = score
                                output['Complete_Time'] = complete_time

                                esoutput.append(output)

        print(len(esoutput))

        from elasticsearch import Elasticsearch		
        
        es = Elasticsearch(self.server)
      
        filename = 'omp-alert-' + query_start[:10]
        for row in esoutput:
            es.index(index = filename, body = row, doc_type = "traffic")
                

                        
    def ompAndFreq(self, all_omp_m, all_freq_m, all_ip_list, abnor_ip_list, folder_name):

        for _ in range(len(all_ip_list) * (len(all_ip_list)-1)):
            all_ip_list.append('NaN')
            
        for _ in range(len(all_ip_list) - len(abnor_ip_list)):
            abnor_ip_list.append('NaN')

        print(len(all_ip_list))

        df = pd.DataFrame({'omp' : all_omp_m.flatten().tolist(), 'frequency': all_freq_m.flatten().tolist(), 'ip_list': all_ip_list, 'nor_ip_list': abnor_ip_list})
        filename = folder_name + 'omp_and_frequency'
        df.to_csv(filename + '.csv', index=False)
        

    def threshold(self, omp_threshold, freq_item, freq_threshold, folder_name):

        if len(freq_threshold) > len(omp_threshold):
            for _ in range(len(freq_threshold) - len(omp_threshold)):
                omp_threshold.append('NaN')
        elif len(freq_threshold) < len(omp_threshold):
            for _ in range(len(omp_threshold) - len(freq_threshold)):
                freq_item.append('NaN')
                freq_threshold.append('NaN')

        threshold_df = pd.DataFrame({'omp_threshold': omp_threshold,'freq_item': freq_item,'freq_threshold': freq_threshold})
        filename = folder_name + 'threshold'
        threshold_df.to_csv(filename + '.csv', index=False)


    def allabnormatrix(self, all_infected_ip):

        print('all abnormal matrix ...')
        
        output_row = []
        for sip in all_infected_ip:
            output_row += sip

        output_row.sort()

    def removecsv(self, query_end):
        
        end_time = datetime.datetime.strptime(query_end, "%Y-%m-%dT%H:%M:%S.%f+08:00")
        # rm_end = end_time - datetime.timedelta(hours = self.period * 3)
        rm_end = end_time - datetime.timedelta(hours = 24)
        file_time = rm_end - datetime.timedelta(hours = 1)
        file_cnt = self.period

        filename = []
        for _ in range(file_cnt):
            linux_filename = file_time - datetime.timedelta(hours = 8)
            filename += glob.glob('./data/' + linux_filename.strftime('%m-%d-%H') + '*.csv')
            file_time = file_time + datetime.timedelta(hours = 1)

        print(filename)

        for name in filename:
            os.remove(name)
  

    def run(self, all_omp_m, all_freq_m, all_ip_list, abnor_ip_list, omp_threshold, freq_item, freq_threshold, all_value_matrix, all_infected_ip, all_dip_list, abnor_df, folder_name, query_start, query_end):
        
        # print('number of alert group:' + str(len(all_value_matrix)))
        if len(all_value_matrix) != 0:
            # self.jsonOutput(all_value_matrix, all_infected_ip, all_dip_list, abnor_df, folder_name)
            self.esOutput(all_value_matrix, all_infected_ip, all_dip_list, abnor_df, folder_name, query_start, query_end)

        if len(all_omp_m) != 0:
            print('copy')
            print()
            self.ompAndFreq(all_omp_m, all_freq_m, all_ip_list, abnor_ip_list, folder_name)

        self.threshold(omp_threshold, freq_item, freq_threshold, folder_name)

        self.allabnormatrix(all_infected_ip)

        self.removecsv(query_end)

