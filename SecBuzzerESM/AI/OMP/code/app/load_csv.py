import pandas as pd
import csv
import numpy as np
import datetime
import os
import glob
import ipaddress


class LoadCsv:
    

    def __init__(self, period):
        self.period = period


    def readCsv(self, filename):
        # read csv file
        df = pd.DataFrame()
        for f in filename:
            try:
                df_list = pd.read_csv('./' + f)
            except:
                df_list = pd.DataFrame()

            df = pd.concat([df, df_list])

        return df


    def timeFilter(self, df, start_time, end_time):
        # filter time
        df_time = df.loc[(df.Time >= start_time) & (df.Time < end_time)].reset_index(drop = True)

        return df_time


    def dataPreprocess(self, df, whitelist):
        output_df = pd.DataFrame()
        df = df.dropna(subset=['Source', 'Destination', 'Time'])

        # groupby
        group = df.groupby(["Source", "Destination"]).size().reset_index(name='Count')
        
        # filter intranet ip
        group_intranet = group.copy()
        
        group_intranet['src_private'] = group_intranet['Source'].apply(lambda x: ipaddress.ip_address(x).is_private)
        group_intranet['dst_private'] = group_intranet['Destination'].apply(lambda x: ipaddress.ip_address(x).is_private)
        
        group_intranet = group_intranet.loc[(group_intranet['src_private']) & (group_intranet['dst_private'])]
        group_intranet.drop(['src_private', 'dst_private'], axis=1, inplace=True)
        group_intranet = group_intranet.reset_index(drop=True)

        output_df = pd.concat([output_df, group_intranet])

        # filter whitelist ip
        group_whitelist = group.copy()

        group_whitelist['src_whitelist'] = group_whitelist['Source'].apply(lambda x: True if x in whitelist else False)
        group_whitelist['dst_whitelist'] = group_whitelist['Destination'].apply(lambda x: True if x in whitelist else False)
        
        group_whitelist = group_whitelist.loc[(group_whitelist['src_whitelist']) & (group_whitelist['dst_whitelist'])]
        group_whitelist.drop(['src_whitelist', 'dst_whitelist'], axis=1, inplace=True)
        group_whitelist = group_whitelist.reset_index(drop=True)    
        
        output_df = pd.concat([output_df, group_whitelist]).reset_index(drop=True)
        
        return output_df


    def run(self, next_start, next_end):

        print('Analytics start time: ' + next_start)
        
        print("========== load data ==========")        

        filename = []
        file_time = datetime.datetime.strptime(next_start, '%Y-%m-%dT%H:%M:%S.%f+08:00')
        file_time = file_time - datetime.timedelta(hours = 1)
        file_cnt = self.period + 1
        for _ in range(file_cnt):
            linux_filename = file_time - datetime.timedelta(hours = 8)
            filename += glob.glob('./data/' + linux_filename.strftime('%m-%d-%H') + '*.csv')
            file_time = file_time + datetime.timedelta(hours = 1)
        print('filename: ' + str(filename))

        df = self.readCsv(filename)
        abnor_df = self.timeFilter(df, next_start, next_end)
        # print('Abnormal dataframe: ')
        # print(abnor_df)
        # input()


        # print("========== abnormal dataframe filter intranet/whitelist ip ==========")
        # # load whitelist ip
        # try:
        #     whitelist_df = pd.read_csv('whitelist.csv')
        #     whitelist = list(whitelist_df.whitelist)
        # except:
        #     whitelist = []

        whitelist = ['220.1.51.2', '220.1.52.2', '220.1.53.2', '220.1.54.2', '220.1.55.2', '220.1.56.2', '220.1.57.2']


        abnor_data = self.dataPreprocess(abnor_df, whitelist)
        # print('group abnormal dataframe with Source, Destination ip: ')
        print(abnor_data)

        abnor_ip_list = list(abnor_data['Source']) + list(abnor_data['Destination'])
        abnor_ip_list = sorted(list(set(abnor_ip_list)))


        # 判斷週末
        # 以 ip 數量統計
        # 控制多少比例的 IP 數量為上班/下班
        # 需統計（觀察）一週公司流量才知道總共有多少 ip
        work_ip_cnt = 254 * 0.02
        if len(abnor_ip_list) > work_ip_cnt:
            week_threshold = 'weekday'
        else:
            week_threshold = 'weekend'

        # 以星期區分
        # if datetime.datetime.strptime(next_start, '%Y-%m-%dT%H:%M:%S.%f+08:00').isoweekday() == 6 or datetime.datetime.strptime(next_start, '%Y-%m-%dT%H:%M:%S.%f+08:00').isoweekday() == 7:
        #     week_threshold = 'weekend'
        # else:
        #     week_threshold = 'weekday'

        # 判斷上下班
        if int(next_start[11:13]) >= 8 and int(next_start[11:13]) < 20:
            work_break = 'work'
        elif int(next_start[11:13]) < 8 or int(next_start[11:13]) >= 20:
            work_break = 'break'

        # if int(next_start[11:13]) == 8:
        #     work_break = 'work'
        # elif int(next_start[11:13]) == 20:
        #     work_break = 'break'

        folder_name = './' + week_threshold + '_' + work_break + '/'
        filepath = folder_name + 'omp_and_frequency.csv'
        print('folder name: ' + week_threshold + '_' + work_break)



        if os.path.isfile(filepath):
            print('Data already exists in this time interval. ')
            
            nor_data = []
            # nor_df = pd.DataFrame()


        else:
            print('The first data in this time interval. ')

            # filename
            filename = []
            file_time = datetime.datetime.strptime(next_start, '%Y-%m-%dT%H:%M:%S.%f+08:00') - datetime.timedelta(hours = 1)
            file_time = file_time - datetime.timedelta(hours = 1)
            file_cnt = self.period + 1
            for _ in range(file_cnt):
                linux_filename = file_time - datetime.timedelta(hours = 8)
                filename += glob.glob('./data/' + linux_filename.strftime('%m-%d-%H') + '*.csv')
                file_time = file_time + datetime.timedelta(hours = 1)
            
            print('normal filename: ' + str(filename))
            
            df = self.readCsv(filename)


            # 與前一天同一個時間區間比較 Ｘ
            nor_start_time = datetime.datetime.strptime(next_start, '%Y-%m-%dT%H:%M:%S.%f+08:00') - datetime.timedelta(hours = 1)
            nor_start_time = nor_start_time.strftime('%Y-%m-%dT%H:%M:%S.%f+08:00')
            nor_end_time = datetime.datetime.strptime(next_end, '%Y-%m-%dT%H:%M:%S.%f+08:00') - datetime.timedelta(hours = 1)
            nor_end_time = nor_end_time.strftime('%Y-%m-%dT%H:%M:%S.%f+08:00')
            # print('Analytics start time: ' + nor_start_time)
            # print(nor_start_time)
            nor_df = self.timeFilter(df, nor_start_time, nor_end_time)

            print("========== normal dataframe filter intranet/whitelist ip ==========")
            nor_data = self.dataPreprocess(nor_df, whitelist)
            print(nor_data)


            # if datetime.datetime.strptime(next_start, '%Y-%m-%dT%H:%M:%S.%f+08:00').isoweekday() == 1:
            #     period = 72
            # elif datetime.datetime.strptime(next_start, '%Y-%m-%dT%H:%M:%S.%f+08:00').isoweekday() == 6:
            #     period = 144
            # else:
            #     period = 24

            # nor_start_time = datetime.datetime.strptime(next_start, '%Y-%m-%dT%H:%M:%S.%f+08:00') - datetime.timedelta(hours = self.period)
            # nor_start_time = nor_start_time.strftime("%Y-%m-%dT%H:%M:%S.%f+08:00")
            # nor_end_time = datetime.datetime.strptime(next_end, '%Y-%m-%dT%H:%M:%S.%f+08:00') - datetime.timedelta(hours = self.period)
            # nor_end_time = nor_end_time.strftime("%Y-%m-%dT%H:%M:%S.%f+08:00")
            
            # print(nor_start_time)
            
            # nor_df = self.timeFilter(df, nor_start_time, nor_end_time)

            # print(nor_df)
            # input()


        # return nor_df, abnor_df, folder_name

        return abnor_df, nor_data, abnor_data, folder_name

