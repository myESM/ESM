#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import configparser
import logging
from datetime import datetime

from src.main.db.elasticsearch_connector import ElasticsearchConnector
from src.main.windows_rules import user_execution_1A1
from src.main.windows_rules import masquerading_1A2
from src.main.windows_rules import non_standard_port_1A3
from src.main.windows_rules import command_line_interface_1B1
from src.main.windows_rules import powershell_1B2
from src.main.windows_rules import file_and_directory_discovery_2A1
from src.main.windows_rules import automated_collection_2A2
from src.main.windows_rules import data_from_local_system_2A3
from src.main.windows_rules import data_compressed_2A4
from src.main.windows_rules import data_staged_2A5
from src.main.windows_rules import remote_file_copy_3A1
from src.main.windows_rules import obfuscated_files_or_information_3A2
from src.main.windows_rules import component_object_model_hijacking_3B1
from src.main.windows_rules import bypass_user_accounnt_control_3B2
from src.main.windows_rules import commomly_used_port_3B3
from src.main.windows_rules import standard_application_layer_protocol_3B4
from src.main.windows_rules import modify_registry_3C1
from src.main.windows_rules import remote_file_copy_4A1
from src.main.windows_rules import powershell_4A2
from src.main.windows_rules import decode_files_or_information_4A3
from src.main.windows_rules import process_discovery_4B1
from src.main.windows_rules import file_deletion_4B2
from src.main.windows_rules import file_deletion_4B3
from src.main.windows_rules import file_deletion_4B4
from src.main.windows_rules import file_and_directory_discovery_4C1
from src.main.windows_rules import system_owner_or_user_discovery_4C2
from src.main.windows_rules import system_information_discovery_4C3
from src.main.windows_rules import system_network_configuration_discovery_4C4
from src.main.windows_rules import process_discovery_4C5
from src.main.windows_rules import system_information_discovery_4C6
from src.main.windows_rules import security_software_discovery_4C7
from src.main.windows_rules import security_software_discovery_4C8
from src.main.windows_rules import permission_groups_discovery_4C9
from src.main.windows_rules import execution_through_api_4C10
from src.main.windows_rules import permission_groups_discovery_4C11
from src.main.windows_rules import execution_through_api_4C12
from src.main.windows_rules import new_service_5A1
from src.main.windows_rules import registry_run_keys_or_startup_folder_5B1
from src.main.windows_rules import private_keys_6B1
from src.main.windows_rules import screen_capture_7A1
from src.main.windows_rules import clipboard_data_7A2
from src.main.windows_rules import input_capture_7A3
from src.main.windows_rules import data_compressed_7B2
from src.main.windows_rules import data_encrypted_7B3
from src.main.windows_rules import remote_system_discovery_8A1
from src.main.windows_rules import windows_remote_management_8A2
from src.main.windows_rules import process_discovery_8A3
from src.main.windows_rules import remote_file_copy_8B1
from src.main.windows_rules import valid_accounts_8C1
from src.main.windows_rules import windows_admin_shares_8C2
from src.main.windows_rules import service_execution_8C3
from src.main.windows_rules import remote_file_copy_9A1
from src.main.windows_rules import remote_file_copy_9A2
from src.main.windows_rules import powershell_9B1
from src.main.windows_rules import file_and_directory_discovery_9B2
from src.main.windows_rules import automated_collection_9B3
from src.main.windows_rules import data_from_local_system_9B4
from src.main.windows_rules import data_staged_9B5
from src.main.windows_rules import data_encrypted_9B6
from src.main.windows_rules import data_compressed_9B7
from src.main.windows_rules import file_deletion_9C1
from src.main.windows_rules import file_deletion_9C2
from src.main.windows_rules import file_deletion_9C3
from src.main.windows_rules import file_deletion_9C4
from src.main.windows_rules import service_execution_10A1
from src.main.windows_rules import virtualization_evasion_11A3
from src.main.windows_rules import system_information_discovery_11A4
from src.main.windows_rules import peripheral_device_discovery_11A5
from src.main.windows_rules import system_owner_user_discovery_11A6
from src.main.windows_rules import system_network_configuration_discovery_11A7
from src.main.windows_rules import process_discovery_11A8
from src.main.windows_rules import file_and_directory_discovery_11A9
from src.main.windows_rules import decode_files_or_information_11A10
from src.main.windows_rules import powershell_11A12
from src.main.windows_rules import commomly_used_port_11A13
from src.main.windows_rules import standard_application_layer_protocol_11A14
from src.main.windows_rules import file_and_directory_discovery_12A1
from src.main.windows_rules import security_software_discovery_12B1
from src.main.windows_rules import system_information_discovery_13A1
from src.main.windows_rules import system_network_configuration_discovery_13B1
from src.main.windows_rules import system_owner_user_discovery_13C1
from src.main.windows_rules import process_discovery_13D1
from src.main.windows_rules import component_object_model_hijacking_14A1
from src.main.windows_rules import bypass_user_accounnt_control_14A2
from src.main.windows_rules import modify_registry_14A3
from src.main.windows_rules import process_discovery_14B2
from src.main.windows_rules import system_owner_user_discovery_15A1
from src.main.windows_rules import remote_system_discovery_16A1
from src.main.windows_rules import execution_through_api_16B2
from src.main.windows_rules import windows_remote_management_16C1
from src.main.windows_rules import valid_accounts_16C2
from src.main.windows_rules import email_collection_17A1
from src.main.windows_rules import data_staged_17B2
from src.main.windows_rules import data_compressed_17C1
from src.main.windows_rules import web_service_18A1
from src.main.windows_rules import rundll32_20A1
from src.main.windows_rules import windows_management_instrumentation_event_subscription_20A2
from src.main.windows_rules import pass_the_ticket_20A2
from src.main.windows_rules import windows_remote_management_20B2
from src.main.windows_rules import create_account_20B3

#loginng setting
#LOG_FILENAME = datetime.now().strftime("output-%Y-%m-%d_%H_%M_%S.log")
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s : %(message)s')

# loading config parameter
config = configparser.ConfigParser()
config.read("config.ini")
ES_HOST = config.get("elasticsearch", "es_host")
ES_PORT = config.get("elasticsearch", "es_port")
ES_OUTPUT_INDEX = eval(config.get("elasticsearch", "es_output_index_prefix"))
if len(str(datetime.today().month)) == 1:
  ES_OUTPUT_INDEX = ES_OUTPUT_INDEX + str(datetime.today().year) + "-0" + str(datetime.today().month)
else:
  ES_OUTPUT_INDEX = ES_OUTPUT_INDEX + str(datetime.today().year) + "-" + str(datetime.today().month)

def winlog_rule_based(es_index, es_start_time, es_end_time):
  #start time
  start_time = datetime.now()

  es_connector = ElasticsearchConnector(ES_HOST, ES_PORT)
  ES_INPUT_INDEX = es_index

  user_execution_1A1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  masquerading_1A2(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  non_standard_port_1A3(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  command_line_interface_1B1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  powershell_1B2(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  file_and_directory_discovery_2A1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  automated_collection_2A2(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  data_from_local_system_2A3(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  data_compressed_2A4(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  data_staged_2A5(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  remote_file_copy_3A1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  obfuscated_files_or_information_3A2(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  component_object_model_hijacking_3B1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  bypass_user_accounnt_control_3B2(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  commomly_used_port_3B3(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  standard_application_layer_protocol_3B4(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  modify_registry_3C1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  remote_file_copy_4A1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  powershell_4A2(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  decode_files_or_information_4A3(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  process_discovery_4B1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  file_deletion_4B2(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  file_deletion_4B3(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  file_deletion_4B4(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  file_and_directory_discovery_4C1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  system_owner_or_user_discovery_4C2(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  system_information_discovery_4C3(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  system_network_configuration_discovery_4C4(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  process_discovery_4C5(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  system_information_discovery_4C6(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  security_software_discovery_4C7(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  security_software_discovery_4C8(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  permission_groups_discovery_4C9(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  execution_through_api_4C10(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  permission_groups_discovery_4C11(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  execution_through_api_4C12(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  new_service_5A1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  registry_run_keys_or_startup_folder_5B1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  private_keys_6B1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  screen_capture_7A1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  clipboard_data_7A2(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  input_capture_7A3(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  data_compressed_7B2(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  data_encrypted_7B3(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  remote_system_discovery_8A1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  windows_remote_management_8A2(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  process_discovery_8A3(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  remote_file_copy_8B1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  valid_accounts_8C1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  windows_admin_shares_8C2(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  service_execution_8C3(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  remote_file_copy_9A1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  remote_file_copy_9A1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  powershell_9B1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  file_and_directory_discovery_9B2(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  automated_collection_9B3(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  data_from_local_system_9B4(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  data_staged_9B5(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  data_encrypted_9B6(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  data_compressed_9B7(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  file_deletion_9C1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  file_deletion_9C2(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  file_deletion_9C3(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  file_deletion_9C4(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  service_execution_10A1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  virtualization_evasion_11A3(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  system_information_discovery_11A4(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  peripheral_device_discovery_11A5(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  system_owner_user_discovery_11A6(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  system_network_configuration_discovery_11A7(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  process_discovery_11A8(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  file_and_directory_discovery_11A9(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  decode_files_or_information_11A10(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  powershell_11A12(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  commomly_used_port_11A13(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  standard_application_layer_protocol_11A14(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  file_and_directory_discovery_12A1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  security_software_discovery_12B1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  system_information_discovery_13A1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  system_network_configuration_discovery_13B1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  system_owner_user_discovery_13C1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  process_discovery_13D1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  component_object_model_hijacking_14A1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  bypass_user_accounnt_control_14A2(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  modify_registry_14A3(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  process_discovery_14B2(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  system_owner_user_discovery_15A1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  remote_system_discovery_16A1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  execution_through_api_16B2(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  windows_remote_management_16C1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  valid_accounts_16C2(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  email_collection_17A1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  data_staged_17B2(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  data_compressed_17C1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  web_service_18A1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  rundll32_20A1(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  windows_management_instrumentation_event_subscription_20A2(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  pass_the_ticket_20A2(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  windows_remote_management_20B2(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)
  create_account_20B3(es_connector, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time)

  # execute time
  end_time = datetime.now() - start_time
  logging.info("Spending time={0}".format(end_time))

if __name__ == "__main__":
  es_index = "winlogbeat-utica"
  es_start_time = "2020-08-05T00:00:00"
  es_end_time = "2020-08-05T23:59:59"

  #run main
  winlog_rule_based(es_index, es_start_time, es_end_time)
