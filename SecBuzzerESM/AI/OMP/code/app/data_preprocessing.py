import pandas as pd
import ipaddress

class DataPreprocessing:


    def dataPreprocess(self, df):

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
        
        # # 塞選出內網（77網段下）的流量
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


    def run(self, nor_df, abnor_df):

        print('data preprocessing')
        if nor_df.empty:
            nor_data = []
        else:
            nor_data = self.dataPreprocess(nor_df)
        # print(nor_data)

        abnor_data = self.dataPreprocess(abnor_df)
        # print(abnor_data)
        # input()
        
        return nor_data, abnor_data    
    
