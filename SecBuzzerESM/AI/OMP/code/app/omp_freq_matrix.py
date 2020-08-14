import pandas as pd
import numpy as np


class OmpFreqMatrix:
        

    def getOmpFreqMatrix(self, folder_name):
        
        # 讀 omp 矩陣及 frequency 矩陣
        all_omp_m = []
        all_freq_m = []
        all_ip_list = []
        nor_ip_list = []

        try:
            filename = folder_name + 'omp_and_frequency'
            csv = pd.read_csv(filename + ".csv")
            
        except:
            return all_omp_m, all_freq_m, all_ip_list, nor_ip_list

        else:
            all_ip_list = list(csv.loc[csv['ip_list'].notnull()]['ip_list'])
            nor_ip_list = list(csv.loc[csv['nor_ip_list'].notnull()]['nor_ip_list'])

            omp_list = list(csv['omp'])
            freq_list = list(csv['frequency'])

            for i in range(len(all_ip_list)):
                all_omp_m.append(omp_list[len(all_ip_list)*i:len(all_ip_list)*i+len(all_ip_list)])
                all_freq_m.append(freq_list[len(all_ip_list)*i:len(all_ip_list)*i+len(all_ip_list)])

            return all_omp_m, all_freq_m, all_ip_list, nor_ip_list


    def getThreshold(self, folder_name):

        omp_threshold = []
        freq_item = []
        freq_threshold = []

        try:
            filename = folder_name + 'threshold'
            csv = pd.read_csv(filename + ".csv")

        except:
            return omp_threshold, freq_item, freq_threshold

        else:
            omp_threshold = list(csv.loc[csv['omp_threshold'].notnull()]['omp_threshold'])
            freq_item = list(csv.loc[csv['freq_item'].notnull()]['freq_item'])
            freq_threshold = list(csv.loc[csv['freq_threshold'].notnull()]['freq_threshold'])

            return omp_threshold, freq_item, freq_threshold


    def run(self, folder_name):
        
        all_omp_m, all_freq_m, all_ip_list, nor_ip_list = self.getOmpFreqMatrix(folder_name)
        
        omp_threshold, freq_item, freq_threshold = self.getThreshold(folder_name)

        return all_omp_m, all_freq_m, all_ip_list, nor_ip_list, omp_threshold, freq_item, freq_threshold
