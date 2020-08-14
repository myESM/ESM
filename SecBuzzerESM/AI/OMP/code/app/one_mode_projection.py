import numpy as np
import pandas as pd
from scipy.sparse import csgraph
from sklearn.cluster import KMeans

from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource, LinearColorMapper, ColorBar, PrintfTickFormatter, BasicTicker, LogColorMapper
from bokeh.transform import transform

class OneModeProjection:


    def getOMPDict(self, data, ip_list):
        # 建立one mode projection 相似矩陣
        '''
        Return:
            {'147.32.80.13': {'147.32.80.13': 0, '147.32.87.36': 2}}
        '''
        
        dic = {}

        for i in range(len(data)):
            if data['Source'][i] not in dic.keys():
                dic[data['Source'][i]] = {}
                dic[data['Source'][i]][data['Source'][i]] = 0
            dic[data['Source'][i]][data['Destination'][i]] = data['Count'][i]

        for ip in ip_list:
            if ip not in dic.keys():
                dic[ip] = {}
                dic[ip][ip] = 0

        return dic       

        
    def getOMPSimilarityMatrix(self, dic, ip):
        #OneModeProjection 相似度矩陣：彼此共同連線的比例，雙向矩陣
        
        similarity_matrix = np.zeros((len(ip), len(ip)))

        for i in range(0, len(ip)):
            for j in range(0, len(ip)):  
                similarity_matrix[i][j] = float(len(dic[ip[i]].keys() & dic[ip[j]].keys())) / float(len(dic[ip[i]].keys() | dic[ip[j]].keys()))

        return similarity_matrix
    

    def getIpAndNumber(self, ip_list):
        '''
        Return:
            ip_number : {'147.32.80.13': 0, '147.32.80.9': 1}
            number_ip : {0: '147.32.80.13', 1: '147.32.80.9'}
        ''' 
        
        ip_number = {}
        number_ip = {}
        for i, element in enumerate(ip_list):
            ip_number[element] = i
            number_ip[i] = element
        
        return ip_number, number_ip
    

    def getAllFreqSimilarityMatrix(self, dic, ip_number):
        #Frequency Similarity Matrix：彼此有互相連線的給值1，單向矩陣
        s_matrix  = np.zeros((len(ip_number.keys()), len(ip_number.keys())))
        for k in dic.keys():
            for v in dic[k]:
                s_matrix[ip_number[k]][ip_number[v]] = 1

        return s_matrix 


    def getEigenByLaplacian(self, smilarity_matrix) :
        # 相似矩陣分群
        # 計算evalues, evectors

        laplacian = csgraph.laplacian(smilarity_matrix, normed=True)
        [evalues, evectors] = np.linalg.eigh(laplacian)

        return [evalues, evectors]

    
    def findK2(self, evalues):
        #計算分群數
    
        return sum(evalues < 0.2)
    
    
    def kmeans(self, k, matrix):
        #分群
    
        k_means = KMeans(init='k-means++', n_init=10, n_clusters= k)
        k_means.fit(matrix)

        return k_means
    

    def distributionIp(self, labels_, ip_list):
        '''
        Return:
            {0: ['147.32.80.9', '147.32.86.77'], 1: ['147.32.84.165']}
        '''
        
        groups = {}
        for i in range(len(labels_)):
            if labels_[i] not in groups.keys():
                groups[labels_[i]] = []
            groups[labels_[i]].append(ip_list[i])

        return groups

    
    def getFreqSimilarityMatrix(self, dic, sip_number, dip_number, infected_ip, dip_list):
        #Frequency Similarity Matrix：彼此有互相連線的給值1，單向矩陣
        
        s_matrix  = np.zeros((len(sip_number.keys()), len(dip_number.keys())))
        for k in dic.keys():
            if k in infected_ip:
                for v in dic[k]:
                    if v in dip_list:
                        s_matrix[sip_number[k]][dip_number[v]] = 1
        
        return s_matrix
    

    def mat(self, output_name, nodesX, nodesY, counts):

        xname = []
        yname = []

        for node1 in nodesX:
            for node2 in nodesY:
                xname.append(node1)
                yname.append(node2)

        source = ColumnDataSource(data=dict(
            xnames=xname,
            ynames=yname,
            count=counts.flatten(),
        ))


        colors = ["#FFFFFF", "#CCCCFF", "#9999FF", "#5555FF", "#0000FF", "#0000CC", "#0000AA", "#000088", "#000000"]

        exp_cmap = LogColorMapper(palette=colors, low = 0, high = 10)
        # exp_cmap = LogColorMapper(palette=colors, low = np.min(counts), high = np.max(counts))

        p = figure(title="Matrix Figure",
                   x_axis_location="above", tools="hover,save",
                   x_range=nodesX, y_range=list(reversed(nodesY)))

        p.rect(x='xnames', y='ynames', width=0.9, height=0.9,
               source=source, line_color=None, fill_color=transform('count', exp_cmap))

        p.plot_width = 800
        p.plot_height = 800
        p.grid.grid_line_color = None
        p.axis.axis_line_color = None
        p.axis.major_tick_line_color = None
        p.axis.major_label_text_font_size = "5pt"
        p.axis.major_label_standoff = 0
        p.xaxis.major_label_orientation = np.pi / 3

        #圖例
        color_bar = ColorBar(color_mapper=exp_cmap, location=(0, 0),
                             ticker=BasicTicker(desired_num_ticks=len(colors)), 
                             formatter=PrintfTickFormatter(format="%d"))

        p.add_layout(color_bar, 'right')

        #游標所指“點”的說明格式
        p.select_one(HoverTool).tooltips = [
            ('names', '@ynames -> @xnames'),
            ('count', '@count'),
        ]

        output_file(output_name + ".html", title=output_name)
        
        show(p)  # show the plot


    def frequencyMatrixEmpty(self, all_ip, infected_ip, abnor_df, nor_dict, abnor_dict, threshold, group_number, query_start):
        
        #取出要分析的 IP
        all_dip_list = abnor_df.loc[abnor_df['Source'].isin(infected_ip), 'Destination'].tolist()
        all_dip_list = sorted(list(set(all_dip_list)))

        dip_list = []
        #dstip必須在所有dip_list中
        for i in all_dip_list:
            if i in all_ip:
                dip_list.append(i)

        sip_number, number_sip = self.getIpAndNumber(infected_ip)
        dip_number, number_dip = self.getIpAndNumber(dip_list)

        nor_smatrix = self.getFreqSimilarityMatrix(nor_dict, sip_number, dip_number, infected_ip, dip_list)
        abnor_smatrix = self.getFreqSimilarityMatrix(abnor_dict, sip_number, dip_number, infected_ip, dip_list)

        server_ip = ['0.0.0.0', '255.255.255.255']
        # server_ip = ['192.168.70.254', '192.168.70.255']

        #如果diff_matrix值為1從abnor查count，為-1從nor查count
        '''如果只考慮目前時間所出現的異常就忽略-1'''
        diff_matrix = abnor_smatrix - nor_smatrix
        value_matrix = diff_matrix.copy()
        output_matrix = np.zeros((len(diff_matrix), len(diff_matrix[0])))
        for i in range(len(diff_matrix)):
            for j in range(len(diff_matrix[0])):
                if diff_matrix[i][j] == 1:
                    value_matrix[i][j] = abnor_dict[number_sip[i]][number_dip[j]]
                    if number_sip[i] not in server_ip and number_dip[j] not in server_ip:
                        output_matrix[i][j] = 1


        output_matrix = np.array(output_matrix)
        output_mean = np.mean(output_matrix.flatten())

        #threshold
        #如果大於20%的格子有值 且 總格子數大於5 可能為異常群
        '''這裡有刻意改成8，為了實驗方便，注意之後要改回來'''
        if sum(output_matrix.flatten()) > len(output_matrix)*len(output_matrix[0])*threshold and sum(output_matrix.flatten()) > 3.0:
            value_matrix_t = value_matrix.T
            name = query_start[8:10] + '_' + query_start[11:13] + '_' + str(group_number)
            # self.mat(name, dip_list, infected_ip, value_matrix_t)
        else:
            output_matrix = []
            

        return output_matrix, infected_ip, dip_list, output_mean


    def runEmpty(self, nor_df, abnor_df, omp_threshold, freq_item, freq_threshold, query_start):

        abnor_iplist = list(abnor_df['Source']) + list(abnor_df['Destination'])
        abnor_ip_list = sorted(list(set(abnor_iplist)))

        # 取出所有的srcip, dstip
        iplist = list(nor_df['Source']) + list(nor_df['Destination']) + list(abnor_df['Source']) + list(abnor_df['Destination'])
        ip_list = sorted(list(set(iplist)))



        
        # 建立one mode projection 相似矩陣
        nor_dict = self.getOMPDict(nor_df, ip_list)
        abnor_dict = self.getOMPDict(abnor_df, ip_list)
                
        nor_smatrix = self.getOMPSimilarityMatrix(nor_dict, ip_list)
        abnor_smatrix = self.getOMPSimilarityMatrix(abnor_dict, ip_list)
        
        ip_number, _ = self.getIpAndNumber(ip_list)   
        all_abnor_freq_m = self.getAllFreqSimilarityMatrix(abnor_dict, ip_number)



        # 相似矩陣值改為0 與1
        omp_zero_one_matrix = np.array(abnor_smatrix)
        omp_zero_one_matrix[omp_zero_one_matrix > 0] = 1
        
        
        diff_matrix = abs(abnor_smatrix - nor_smatrix)

        print('ip number: ' + str(len(ip_list)))
        # print(ip_list)

        #  Plot Result
        # diff_matrix, abnor_smatrix, nor_smatrix
        diff_matrix_T = diff_matrix.T
        name = "omp_diff_matrix"
        # self.mat(name, ip_list, ip_list, diff_matrix_T)


        smatrix_value = sum(diff_matrix.flatten())
        print("diff_matrix value sum : ")
        print(smatrix_value)
        

        '''缺一段threshold定義'''
        if len(omp_threshold) == 0:
            threshold = 0
        else:
            # threshold = np.mean(freq_threshold)
            #threshold = np.percentile(omp_threshold, 95)
            threshold = omp_threshold
        # threshold = 10.0

        normal_omp_m = []
        normal_freq_m = []
        normal_ip_list = []
        all_output_matrix = []
        all_infected_ip = []
        all_dip_list = []


        '''先以smatrix_value寫一個版本'''
        omp_threshold.append(smatrix_value)
        '''如果smatrix_value 或smatrix_count 超過threshold，接著往下做，不然就retuen。'''
        if smatrix_value < threshold:
            
            normal_omp_m = abnor_smatrix
            normal_freq_m = all_abnor_freq_m
            normal_ip_list = ip_list

            return normal_omp_m, normal_freq_m, normal_ip_list, abnor_ip_list, all_output_matrix, all_infected_ip, all_dip_list, omp_threshold, freq_item, freq_threshold

        
        else:
            
            # 相似矩陣分群
            [evalues, evectors] = self.getEigenByLaplacian(abnor_smatrix)
            largest_k = self.findK2(evalues)
            print("abnormal group count =  ", largest_k)
            evectors = np.transpose(evectors)
            kmeans = self.kmeans(largest_k, omp_zero_one_matrix)
            # print("abnormal group label =  ", kmeans.labels_)
            groups =  self.distributionIp(kmeans.labels_, ip_list)


            if len(freq_item) == 0:
                next_item = 1
            else:
                next_item = freq_item[-1] + 1

            if len(freq_threshold) == 0:
                threshold = 99999
            else:
                threshold = np.mean(freq_threshold)


            
            # frequency 相似矩陣檢測
            for group_number, group_ip_list in groups.items():
            
                output_matrix, infected_ip, dip_list, mean_matrix = self.frequencyMatrixEmpty(ip_list, group_ip_list, abnor_df, nor_dict, abnor_dict, threshold, group_number, query_start)
            
                
                freq_item.append(next_item)
                if np.isnan(mean_matrix):
                    mean_matrix = 0
                freq_threshold.append(mean_matrix)

                if len(output_matrix) != 0:
                    all_output_matrix.append(output_matrix)
                    all_infected_ip.append(infected_ip)
                    all_dip_list.append(dip_list)

            

            # 如果 all_output_matrix 有值，表示 abnor 的行為異常，不輸出矩陣的file
            # if len(all_output_matrix) == 0:
                
            normal_omp_m = abnor_smatrix
            normal_freq_m = all_abnor_freq_m
            normal_ip_list = ip_list

            
            return normal_omp_m, normal_freq_m, normal_ip_list, abnor_ip_list, all_output_matrix, all_infected_ip, all_dip_list, omp_threshold, freq_item, freq_threshold            


    def frequencyMatrix(self, all_ip, infected_ip, abnor_df, abnor_dict, all_freq_m, all_ip_list, threshold, group_number, query_start):

        
        #取出要分析的 IP
        all_dip_list = abnor_df.loc[abnor_df['Source'].isin(infected_ip), 'Destination'].tolist()
        all_dip_list = sorted(list(set(all_dip_list)))
        
        dip_list = []
        #dstip必須在所有dip_list中
        for i in all_dip_list:
            if i in all_ip:
                dip_list.append(i)
        

        sip_number, number_sip = self.getIpAndNumber(infected_ip)
        dip_number, number_dip = self.getIpAndNumber(dip_list)

        abnor_smatrix = self.getFreqSimilarityMatrix(abnor_dict, sip_number, dip_number, infected_ip, dip_list)
        
        all_ip_number, _ = self.getIpAndNumber(all_ip_list)
        
        nor_smatrix  = np.zeros((len(infected_ip), len(dip_list)))
        #從大矩陣去抓出群的小矩陣再進行比對
        #如果對應不到就要給0
        for s in infected_ip:
            for d in dip_list:
                try:
                    nor_smatrix[sip_number[s]][dip_number[d]] = all_freq_m[all_ip_number[s]][all_ip_number[d]]
                except:
                    pass
        
        server_ip = ['0.0.0.0', '255.255.255.255']
        # server_ip = ['192.168.70.254', '192.168.70.255']

        #如果diff_matrix值為1從abnor查count，為-1從nor查count
        '''只考慮目前時間的輸出再多一個output_matrix，之後把value_matrix(為了畫圖)刪掉。'''

        '''考慮加在這裡把output行或列有 192.168.70.254, 192.168.70.255, 192.168.30.255 的全部改為0
            這些異常ip會列在哪裡'''

        diff_matrix = abnor_smatrix - nor_smatrix
        value_matrix = diff_matrix.copy()
        output_matrix = np.zeros((len(diff_matrix), len(diff_matrix[0])))
        for i in range(len(diff_matrix)):
            for j in range(len(diff_matrix[0])):
                if diff_matrix[i][j] == 1:
                    value_matrix[i][j] = abnor_dict[number_sip[i]][number_dip[j]]
                    if number_sip[i] not in server_ip and number_dip[j] not in server_ip:
                        output_matrix[i][j] = 1

                    '''或是可以把功能加在這裡'''



        output_matrix = np.array(output_matrix)
        output_mean = np.mean(output_matrix.flatten())

        #  Plot Result
        # diff_matrix, abnorsmatrix, norsmatrix
        # value_matrix_t = value_matrix.T
        # self.mat("diff_matrix", dip_list, infected_ip, value_matrix_t)
        
        #threshold
        #如果大於20%的格子有值 且 總格子數大於5 表示為異常群
        if sum(output_matrix.flatten()) > len(output_matrix)*len(output_matrix[0])*threshold and sum(output_matrix.flatten()) > 3.0:
        
            print('This is a suspicious group.')
            value_matrix_t = value_matrix.T
            name = query_start[8:10] + '_' + query_start[11:13] + '_' + str(group_number)
            self.mat(name, dip_list, infected_ip, value_matrix_t)

        else:
            
            output_matrix = []
        
            
        return output_matrix, infected_ip, dip_list, output_mean


    def run(self, all_omp_m, all_freq_m, all_ip_list, nor_ip_list, abnor_df, omp_threshold, freq_item, freq_threshold, folder_name, query_start):

        abnor_iplist = list(abnor_df['Source']) + list(abnor_df['Destination'])
        abnor_ip_list = sorted(list(set(abnor_iplist)))
        
        # 取出所有的srcip, dstip
        iplist = nor_ip_list + list(abnor_df['Source']) + list(abnor_df['Destination'])
        ip_list = sorted(list(set(iplist)))



        abnor_dict = self.getOMPDict(abnor_df, ip_list)
        
        ip_number, _ = self.getIpAndNumber(ip_list)   
        all_ip_number, _ = self.getIpAndNumber(all_ip_list)

        nor_smatrix  = np.zeros((len(ip_list), len(ip_list)))
        # 以ip對應檔案的矩陣，建立正常矩陣，如果對應不到就要給0
        for s in ip_list:
            for d in ip_list:
                if s == d:
                    nor_smatrix[ip_number[s]][ip_number[d]] = 1
                    continue
                try:
                    nor_smatrix[ip_number[s]][ip_number[d]] = all_omp_m[all_ip_number[s]][all_ip_number[d]]
                except:
                    pass

        abnor_smatrix = self.getOMPSimilarityMatrix(abnor_dict, ip_list)

        # 建立 abnor 完整 ip 的 frequency 矩陣，如果行為正常要存入 csv
        all_abnor_freq_m = self.getAllFreqSimilarityMatrix(abnor_dict, ip_number)

        

        # 將值壓縮為 0 與 1，在分群使用。
        omp_zero_one_matrix = np.array(abnor_smatrix)
        omp_zero_one_matrix[omp_zero_one_matrix > 0] = 1

        diff_matrix = abs(abnor_smatrix - nor_smatrix)

        print('ip number: ' + str(len(ip_list)))
        print(ip_list)



        # Plot Result
        # diff_matrix, abnor_smatrix, nor_smatrix
        diff_matrix_T = diff_matrix.T
        name = "omp_diff_matrix"
        # self.mat(name, ip_list, ip_list, diff_matrix_T)

        smatrix_value = sum(diff_matrix.flatten())
        print("diff_matrix value sum: " + str(round(smatrix_value, 3)))

        # diff_zero_one_matrix = np.array(diff_matrix)
        # diff_zero_one_matrix[diff_zero_one_matrix > 0] = 1
        # smatrix_count = sum(diff_zero_one_matrix.flatten())
        # print("diff_matrix count sum : ")
        # print(smatrix_count)


        '''缺一段threshold定義'''
        if len(omp_threshold) == 0:
            threshold = 99999
        else:
            # threshold = np.mean(omp_threshold)
            
            if len(omp_threshold) <= 5:
                threshold = np.percentile(omp_threshold, 95)
            else:
                threshold = np.percentile(omp_threshold[:-5], 95)
            
            #threshold = np.percentile(omp_threshold[:-5], 95)
    
        # threshold = 10.0

        normal_omp_m = []
        normal_freq_m = []
        normal_ip_list = []
        all_output_matrix = []
        all_infected_ip = []
        all_dip_list = []


        '''先以smatrix_value寫一個版本'''
        '''如果smatrix_value 或smatrix_count 超過threshold，接著往下做，不然就retuen。'''
        omp_threshold.append(smatrix_value)
        if smatrix_value < threshold:
            
            normal_omp_m = abnor_smatrix
            normal_freq_m = all_abnor_freq_m
            normal_ip_list = ip_list

            return normal_omp_m, normal_freq_m, normal_ip_list, abnor_ip_list, all_output_matrix, all_infected_ip, all_dip_list, omp_threshold, freq_item, freq_threshold


        else:

            # 相似矩陣分群
            [evalues, evectors] = self.getEigenByLaplacian(abnor_smatrix)
            largest_k = self.findK2(evalues)
            print("abnormal group count: ", largest_k)
            evectors = np.transpose(evectors)
            kmeans = self.kmeans(largest_k, omp_zero_one_matrix)
            # print("abnormal group label =  ", kmeans.labels_)
            groups =  self.distributionIp(kmeans.labels_, ip_list)


            if len(freq_item) == 0:
                next_item = 1
            else:
                next_item = freq_item[-1] + 1

            if len(freq_threshold) == 0:
                threshold = 0.2
            else:
                threshold = np.mean(freq_threshold)

            # 對群個別運算
            for group_number, group_ip_list in groups.items():
                
                output_matrix, infected_ip, dip_list, mean_matrix = self.frequencyMatrix(ip_list, group_ip_list, abnor_df, abnor_dict, all_freq_m, all_ip_list, threshold, group_number, query_start)

   
                freq_item.append(next_item)
                if np.isnan(mean_matrix):
                    mean_matrix = 0
                freq_threshold.append(mean_matrix)


                if len(output_matrix) != 0:
                    all_output_matrix.append(output_matrix)
                    all_infected_ip.append(infected_ip)
                    all_dip_list.append(dip_list)

            '''紀錄alert次數，超過Ｎ次，強迫紀錄這次的 omp matrix, freq matrix'''
            try:
                filename = folder_name + 'alert_count'
                csv = pd.read_csv(filename + ".csv")
                alert_count = int(csv['alert_count'])
            except:
                alert_count = 0

            # 如果 all_output_matrix 有值，表示 abnor 的行為異常，不輸出矩陣的file
            if len(all_output_matrix) == 0 or alert_count == 3:

                normal_omp_m = abnor_smatrix
                normal_freq_m = all_abnor_freq_m
                normal_ip_list = ip_list
                
                count = 0

            elif alert_count < 3:

                count = alert_count + 1

            print('number of continuous alert: ' + str(count))
            alert_count_df = pd.DataFrame({'alert_count':[str(count)]})
            filename = folder_name + 'alert_count'
            alert_count_df.to_csv(filename + '.csv', index=False)
            
            return normal_omp_m, normal_freq_m, normal_ip_list, abnor_ip_list, all_output_matrix, all_infected_ip, all_dip_list, omp_threshold, freq_item, freq_threshold


