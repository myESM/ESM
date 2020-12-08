import sys
import datetime
import configparser
import app.load_ES as load_ES
import app.feature_extract as feature_extract
import app.one_mode_projection as one_mode_projection
import app.output_data as output_data


class Main():


    def __init__(self):
        #load the parameters from config
        config = configparser.ConfigParser()
        config.read("config.ini")

        self.es_server = config.get("es", "es_server")
        self.es_port = config.get("es", "es_port")
        self.nu = float(config.get("es", "nu"))


    def loadES(self, es_index, start_time, end_time):
        ESdata = load_ES.LoadES(self.es_server, self.es_port)
        rel_train_dict, rel_test_dict, feature_train_mat, feature_test_mat, ip_list, rel_test, feature_test, rel_normal, feature_normal, test_df, nic_name = ESdata.run(es_index, start_time, end_time)
        return rel_train_dict, rel_test_dict, feature_train_mat, feature_test_mat, ip_list, rel_test, feature_test, rel_normal, feature_normal, test_df, nic_name


    def oneModeProjection(self, rel_train_dict, rel_test_dict, feature_train_mat, feature_test_mat, ip_list):
        onemode = one_mode_projection.OneModeProjection(self.nu)        
        normal_ip_list = onemode.run(rel_train_dict, rel_test_dict, feature_train_mat, feature_test_mat, ip_list)
        return normal_ip_list


    def outputData(self, rel_test, feature_test, rel_normal, feature_normal, normal_ip_list, ip_list, test_df, start_time, end_time, nic_name):
        output = output_data.OutputData(self.es_server, self.es_port)        
        output.run(rel_test, feature_test, rel_normal, feature_normal, normal_ip_list, ip_list, test_df, start_time, end_time, nic_name)


if __name__ == "__main__":  

    es_index = 'imbd-input-data-ip'
    start_time = '2019-12-10T03:00:00.000000+08:00'
    end_time = '2019-12-10T06:00:00.000000+08:00'
    # es_index = 'imbd-input-data-port'
    # start_time = '2017-07-07T02:50:00.000000+08:00'
    # end_time = '2017-07-07T03:00:00.000000+08:00'

    load_main = Main()
    rel_train_dict, rel_test_dict, feature_train_mat, feature_test_mat, ip_list, rel_test, feature_test, rel_normal, feature_normal, test_df, nic_name = load_main.loadES(es_index, start_time, end_time)
    normal_ip_list = load_main.oneModeProjection(rel_train_dict, rel_test_dict, feature_train_mat, feature_test_mat, ip_list)
    load_main.outputData(rel_test, feature_test, rel_normal, feature_normal, normal_ip_list, ip_list, test_df, start_time, end_time, nic_name)
    
