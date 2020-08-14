import sys
import datetime
import configparser
import app.omp_freq_matrix as omp_freq_matrix
import app.load_csv as load_csv
import app.load_pcap as load_pcap
import app.one_mode_projection as one_mode_projection
import app.output_data as output_data
import app.pcap_to_csv as pcap_to_csv


class Main():

    
    def __init__(self):
        #load the parameters from config
        config = configparser.ConfigParser()
        config.read("config.ini")

        self.file_name = eval(config.get("pcap", "pcap_file_name"))
        # self.query_start = config.get("pcap", "query_start")
        analysis_time = datetime.datetime.now()-datetime.timedelta(hours = 12)
        self.query_start = analysis_time.strftime('%Y-%m-%dT%H:%M:%S.%f')
        self.period = int(config.get("pcap", "period"))
        self.network_segment = config.get("pcap", "network_segment")
        self.server = config.get("pcap", "server")


    def loadCsv(self, next_start, next_end):
        csvdata = load_csv.LoadCsv(self.period)
        abnor_df, nor_data, abnor_data, folder_name = csvdata.run(next_start, next_end)
        return abnor_df, nor_data, abnor_data, folder_name


    '''
    def loadPcap(self):
        pcapdata = load_pcap.LoadPcap(self.file_name, self.query_start, self.period, self.network_segment)
        abnor_df, nor_data, abnor_data, folder_name = pcapdata.run()
        return abnor_df, nor_data, abnor_data, folder_name
    '''


    def ompFreqMatrix(self, folder_name):
        # 判斷有沒有儲存 omp 矩陣及 frequency 矩陣的檔案，如果有就讀檔
        matrix = omp_freq_matrix.OmpFreqMatrix()
        all_nor_omp_m, all_nor_freq_m, all_nor_ip_list, nor_ip_list, omp_threshold, freq_item, freq_threshold = matrix.run(folder_name)
        return all_nor_omp_m, all_nor_freq_m, all_nor_ip_list, nor_ip_list, omp_threshold, freq_item, freq_threshold
    

    def oneModeProjection(self, all_nor_omp_m, nor_data, abnor_data, omp_threshold, freq_item, freq_threshold, all_nor_freq_m, all_nor_ip_list, nor_ip_list, folder_name, query_start):
        onemode = one_mode_projection.OneModeProjection()
        if len(all_nor_omp_m) == 0:
            all_abnor_omp_m, all_abnor_freq_m, all_abnor_ip_list, abnor_ip_list, all_value_matrix, all_infected_ip, all_dip_list, omp_threshold, freq_item, freq_threshold = onemode.runEmpty(nor_data, abnor_data, omp_threshold, freq_item, freq_threshold, query_start)
        else:        
            all_abnor_omp_m, all_abnor_freq_m, all_abnor_ip_list, abnor_ip_list, all_value_matrix, all_infected_ip, all_dip_list, omp_threshold, freq_item, freq_threshold = onemode.run(all_nor_omp_m, all_nor_freq_m, all_nor_ip_list, nor_ip_list, abnor_data, omp_threshold, freq_item, freq_threshold, folder_name, query_start)
        return all_abnor_omp_m, all_abnor_freq_m, all_abnor_ip_list, abnor_ip_list, all_value_matrix, all_infected_ip, all_dip_list, omp_threshold, freq_item, freq_threshold


    # output json
    def outputData(self, all_abnor_omp_m, all_abnor_freq_m, all_abnor_ip_list, abnor_ip_list, omp_threshold, freq_item, freq_threshold, all_value_matrix, all_infected_ip, all_dip_list, abnor_df, folder_name, query_start, query_end):
        output = output_data.OutputData(self.period, self.server)
        output.run(all_abnor_omp_m, all_abnor_freq_m, all_abnor_ip_list, abnor_ip_list, omp_threshold, freq_item, freq_threshold, all_value_matrix, all_infected_ip, all_dip_list, abnor_df, folder_name, query_start, query_end)
    
    
    def runPcapToCsc(self, query_start):
        pcaptocsv = pcap_to_csv.PcapToCsv()
        pcaptocsv.run(query_start)


    def run(self, query_start, query_end):
        # abnor_df, nor_data, abnor_data, folder_name = self.loadPcap()
        abnor_df, nor_data, abnor_data, folder_name = self.loadCsv(query_start, query_end)
        all_nor_omp_m, all_nor_freq_m, all_nor_ip_list, nor_ip_list, omp_threshold, freq_item, freq_threshold = self.ompFreqMatrix(folder_name)
        all_abnor_omp_m, all_abnor_freq_m, all_abnor_ip_list, abnor_ip_list, all_value_matrix, all_infected_ip, all_dip_list, omp_threshold, freq_item, freq_threshold = self.oneModeProjection(all_nor_omp_m, nor_data, abnor_data, omp_threshold, freq_item, freq_threshold, all_nor_freq_m, all_nor_ip_list, nor_ip_list, folder_name, query_start)
        self.outputData(all_abnor_omp_m, all_abnor_freq_m, all_abnor_ip_list, abnor_ip_list, omp_threshold, freq_item, freq_threshold, all_value_matrix, all_infected_ip, all_dip_list, abnor_df, folder_name, query_start, query_end)



if __name__ == "__main__":  
    
    pass
    
    # load_main = Main()

    # abnor_df, nor_data, abnor_data, folder_name = load_main.loadPcap()
    # all_nor_omp_m, all_nor_freq_m, all_nor_ip_list, nor_ip_list, omp_threshold, freq_item, freq_threshold = load_main.ompFreqMatrix(folder_name)
    # all_abnor_omp_m, all_abnor_freq_m, all_abnor_ip_list, abnor_ip_list, all_value_matrix, all_infected_ip, all_dip_list, omp_threshold, freq_item, freq_threshold = load_main.oneModeProjection(all_nor_omp_m, nor_data, abnor_data, omp_threshold, freq_item, freq_threshold, all_nor_freq_m, all_nor_ip_list, nor_ip_list, folder_name)
    # load_main.outputData(all_abnor_omp_m, all_abnor_freq_m, all_abnor_ip_list, abnor_ip_list, omp_threshold, freq_item, freq_threshold, all_value_matrix, all_infected_ip, all_dip_list, abnor_df, folder_name)
