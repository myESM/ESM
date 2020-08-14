# -*- coding: utf-8 -*-
import json
import logging
from datetime import datetime

from src.main.windows_rules_setting import user_execution_1A1_query
from src.main.windows_rules_setting import masquerading_1A2_query
from src.main.windows_rules_setting import non_standard_port_1A3_query
from src.main.windows_rules_setting import command_line_interface_1B1_query
from src.main.windows_rules_setting import powershell_1B2_query
from src.main.windows_rules_setting import file_and_directory_discovery_2A1_query
from src.main.windows_rules_setting import automated_collection_2A2_query
from src.main.windows_rules_setting import data_from_local_system_2A3_query
from src.main.windows_rules_setting import data_compressed_2A4_query
from src.main.windows_rules_setting import data_staged_2A5_query
from src.main.windows_rules_setting import remote_file_copy_3A1_query
from src.main.windows_rules_setting import obfuscated_files_or_information_3A2_query
from src.main.windows_rules_setting import component_object_model_hijacking_3B1_query
from src.main.windows_rules_setting import bypass_user_accounnt_control_3B2_query
from src.main.windows_rules_setting import commomly_used_port_3B3_query
from src.main.windows_rules_setting import standard_application_layer_protocol_3B4_query
from src.main.windows_rules_setting import modify_registry_3C1_query
from src.main.windows_rules_setting import remote_file_copy_4A1_query
from src.main.windows_rules_setting import powershell_4A2_query
from src.main.windows_rules_setting import decode_files_or_information_4A3_query
from src.main.windows_rules_setting import process_discovery_4B1_query
from src.main.windows_rules_setting import file_deletion_4B2_query
from src.main.windows_rules_setting import file_deletion_4B3_query
from src.main.windows_rules_setting import file_deletion_4B4_query
from src.main.windows_rules_setting import file_and_directory_discovery_4C1_query
from src.main.windows_rules_setting import system_owner_or_user_discovery_4C2_query
from src.main.windows_rules_setting import system_information_discovery_4C3_query
from src.main.windows_rules_setting import system_network_configuration_discovery_4C4_query
from src.main.windows_rules_setting import process_discovery_4C5_query
from src.main.windows_rules_setting import system_information_discovery_4C6_query
from src.main.windows_rules_setting import security_software_discovery_4C7_query
from src.main.windows_rules_setting import security_software_discovery_4C8_query
from src.main.windows_rules_setting import permission_groups_discovery_4C9_query
from src.main.windows_rules_setting import execution_through_api_4C10_query
from src.main.windows_rules_setting import permission_groups_discovery_4C11_query
from src.main.windows_rules_setting import execution_through_api_4C12_query
from src.main.windows_rules_setting import new_service_5A1_query
from src.main.windows_rules_setting import registry_run_keys_or_startup_folder_5B1_query
from src.main.windows_rules_setting import private_keys_6B1_query
from src.main.windows_rules_setting import screen_capture_7A1_query
from src.main.windows_rules_setting import clipboard_data_7A2_query
from src.main.windows_rules_setting import input_capture_7A3_query
from src.main.windows_rules_setting import data_compressed_7B2_query
from src.main.windows_rules_setting import data_encrypted_7B3_query
from src.main.windows_rules_setting import remote_system_discovery_8A1_query
from src.main.windows_rules_setting import windows_remote_management_8A2_query
from src.main.windows_rules_setting import process_discovery_8A3_query
from src.main.windows_rules_setting import remote_file_copy_8B1_query
from src.main.windows_rules_setting import valid_accounts_8C1_query
from src.main.windows_rules_setting import windows_admin_shares_8C2_query
from src.main.windows_rules_setting import service_execution_8C3_query
from src.main.windows_rules_setting import remote_file_copy_9A1_query
from src.main.windows_rules_setting import remote_file_copy_9A2_query
from src.main.windows_rules_setting import powershell_9B1_query
from src.main.windows_rules_setting import file_and_directory_discovery_9B2_query
from src.main.windows_rules_setting import automated_collection_9B3_query
from src.main.windows_rules_setting import data_from_local_system_9B4_query
from src.main.windows_rules_setting import data_staged_9B5_query
from src.main.windows_rules_setting import data_encrypted_9B6_query
from src.main.windows_rules_setting import data_compressed_9B7_query
from src.main.windows_rules_setting import file_deletion_9C1_query
from src.main.windows_rules_setting import file_deletion_9C2_query
from src.main.windows_rules_setting import file_deletion_9C3_query
from src.main.windows_rules_setting import file_deletion_9C4_query
from src.main.windows_rules_setting import service_execution_10A1_query

def suricata_output_format():
  """
  Parameters:
    NULL

  Returns:
    Suricata output format dictonary
  """
  suricata_fields = {}
  suricata_fields["timestamp"] = ""
  suricata_fields["flow_id"] = ""
  suricata_fields["in_iface"] = ""
  suricata_fields["event_type"] = "alert"
  suricata_fields["vlan"] = []
  suricata_fields["src_ip"] = ""
  suricata_fields["src_port"] = ""
  suricata_fields["dest_ip"] = ""
  suricata_fields["dest_port"] = ""
  suricata_fields["proto"] = ""
  suricata_fields["metadata"] = {"flowbits" : []}
  suricata_fields["tx_id"] = ""
  suricata_fields["alert"] = {
                              "action" : "",
                              "gid" : "",
                              "signature_id" : "",
                              "rev" : "",
                              "signature" : "",
                              "category" : "",
                              "severity" : "",
                              "metadata" : {
                                "by" : [],
                                "created_at" : []
                                }
                              }
  suricata_fields["http"] = {
                              "hostname": "",
                              "url": "",
                              "http_user_agent": "",
                              "http_content_type": "",
                              "http_method": "",
                              "protocol": "",
                              "status": "",
                              "length": "",
                              "http_response_body_printable": "",
                              "http_response_body": ""
                            }
  suricata_fields["app_proto"] = ""
  suricata_fields["flow"] = {
                              "pkts_toserver": "",
                              "pkts_toclient": "",
                              "bytes_toserver": "",
                              "bytes_toclient": "",
                              "start": ""
                            }
  suricata_fields["payload"] = ""
  suricata_fields["payload_printable"] = ""
  suricata_fields["stream"] = ""
  suricata_fields["log_time"] = ""
  suricata_fields["_log_type"] = ""
  suricata_fields["module"] = "winlog"
  suricata_fields["@timestamp"] = ""
  return suricata_fields

def user_execution_1A1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "User Execution - T1204"
  query_list = user_execution_1A1_query(es_start_time, es_end_time)
  for query_str in query_list:
    result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
    result_length = result["hits"]["total"]["value"]
    if result_length > 0:
      for res in result["hits"]["hits"]:
        res = res["_source"]
        res_hashes = res["winlog"]["event_data"]["Hashes"]
        # ToDo: virustotal API
        res_md5 = res_hashes.split(",")[0].split("=")[1]
        res_sha256 = res_hashes.split(",")[1].split("=")[1]
        res_imphash = res_hashes.split(",")[2].split("=")[1]

        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210001"
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("user_execution_1A1 finished.")
  return True

def masquerading_1A2(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Masquerading - T1036"
  query_list = masquerading_1A2_query(es_start_time, es_end_time)
  for query_str in query_list:
    result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
    result_length = result["hits"]["total"]["value"]
    if result_length > 0:
      for res in result["hits"]["hits"]:
        res = res["_source"]
        if "\u202e" in res["winlog"]["event_data"]["Image"]:
          suricata_output = suricata_output_format()
          suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
          suricata_output["alert"]["category"] = TECHNIQUE
          suricata_output["alert"]["signature_id"] = "20210002"
          suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
          suricata_output["log_time"] = res["@timestamp"]
          suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
          suricata_output["user_data1"] = res
          es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("masquerading_1A2 finished.")
  return True

def non_standard_port_1A3(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Non-Standard Port - T1571"
  WINDOWS_COMMON_PORT_LIST = ["20", "21", "22","23", "25", "50", "51", "53", "67", "68", "69", "80", "110", "119", "123", "135", "136", "137", "138", "139", "143", "161", "162", "389", "443", "3389", "5985"]
  query_str = non_standard_port_1A3_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if res["winlog"]["event_data"]["DestinationPort"] not in WINDOWS_COMMON_PORT_LIST:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210003"
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("non_standard_port_1A3 finished.")
  return True

def command_line_interface_1B1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Command and Scripting Interpreter: Windows Command Shell - T1059.003"
  query_str = command_line_interface_1B1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210004"
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("command_line_interface_1B1 finished.")
  return True

def powershell_1B2(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Command and Scripting Interpreter: PowerShell - T1059.001"
  query_str = powershell_1B2_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210005"
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("powershell_1B2 finished.")
  return True

def file_and_directory_discovery_2A1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "File and Directory Discovery - T1083"
  query_str = file_and_directory_discovery_2A1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210006"
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("file_and_directory_discovery_2A1 finished.")
  return True

def automated_collection_2A2(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Automated Collection - T1119"
  query_str = automated_collection_2A2_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210007"
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("automated_collection_2A2 finished.")
  return True

def data_from_local_system_2A3(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Data from Local System - T1005"
  query_str = data_from_local_system_2A3_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210008"
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("data_from_local_system_2A3 finished.")
  return True

def data_compressed_2A4(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Archive Collected Data - T1560"
  query_str = data_compressed_2A4_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210009"
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("data_compressed_2A4 finished.")
  return True

def data_staged_2A5(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Data Staged - T1074"
  query_str = data_staged_2A5_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Compress-Archive" in res["winlog"]["event_data"]["ScriptBlockText"]:
        if "-DestinationPath" in res["winlog"]["event_data"]["ScriptBlockText"]:
          if ".zip" in res["winlog"]["event_data"]["ScriptBlockText"]:
            suricata_output = suricata_output_format()
            suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
            suricata_output["alert"]["category"] = TECHNIQUE
            suricata_output["alert"]["signature_id"] = "20210010"
            suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
            suricata_output["log_time"] = res["@timestamp"]
            suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
            suricata_output["user_data1"] = res
            es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("data_staged_2A5 finished.")
  return True

def remote_file_copy_3A1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Ingress Tool Transfer - T1105"
  query_str = remote_file_copy_3A1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210011"
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("remote_file_copy_3A1 finished.")
  return True

def obfuscated_files_or_information_3A2(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Obfuscated Files or Information - T1027"
  query_str = obfuscated_files_or_information_3A2_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210012"
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("obfuscated_files_or_information_3A2 finished.")
  return True

def component_object_model_hijacking_3B1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Event Triggered Execution: Component Object Model Hijacking - T1546.015"
  query_str = component_object_model_hijacking_3B1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210013"
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("component_object_model_hijacking_3B1 finished.")
  return True

def bypass_user_accounnt_control_3B2(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Abuse Elevation Control Mechanism: Bypass User Access Control - T1548.002"
  query_str = bypass_user_accounnt_control_3B2_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210014"
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("bypass_user_accounnt_control_3B2 finished.")
  return True

def commomly_used_port_3B3(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Commonly Used Port - T1436"
  WINDOWS_COMMON_PORT_LIST = ["20", "21", "22","23", "25", "50", "51", "53", "67", "68", "69", "80", "110", "119", "123", "135", "136", "137", "138", "139", "143", "161", "162", "389", "443", "3389", "5985"]
  query_str = commomly_used_port_3B3_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if res["winlog"]["event_data"]["DestinationPort"] in WINDOWS_COMMON_PORT_LIST:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210015"
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("commomly_used_port_3B3 finished.")
  return True

def standard_application_layer_protocol_3B4(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Application Layer Protocol - T1071"
  query_str = standard_application_layer_protocol_3B4_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210016"
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("standard_application_layer_protocol_3B4 finished.")
  return True

def modify_registry_3C1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Modify Registry - T1112"
  query_str = modify_registry_3C1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      res_scripts = res["winlog"]["event_data"]["ScriptBlockText"]
      if "HKCU:\\" in res_scripts or "HKEY_CURRENT_USER" in res_scripts:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210017"
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("modify_registry_3C1 finished.")
  return True

def remote_file_copy_4A1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Ingress Tool Transfer - T1105"
  query_str = remote_file_copy_4A1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210018"
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("remote_file_copy_4A1 finished.")
  return True

def powershell_4A2(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Command and Scripting Interpreter: PowerShell - T1059.001"
  query_str = powershell_4A2_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210019"
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("powershell_4A2 finished.")
  return True

def decode_files_or_information_4A3(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Deobfuscate/Decode Files or Information - T1140"
  query_str = decode_files_or_information_4A3_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210020"
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("decode_files_or_information_4A3 finished.")
  return True

def process_discovery_4B1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Process Discovery - T1057"
  query_str = process_discovery_4B1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210021"
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("process_discovery_4B1 finished.")
  return True

def file_deletion_4B2(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Indicator Removal on Host: File Deletion - T1070.004"
  query_str = file_deletion_4B2_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "CommandLine" in res["winlog"]["event_data"]:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210022"
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("file_deletion_4B2 finished.")
  return True

def file_deletion_4B3(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Indicator Removal on Host: File Deletion - T1070.004"
  query_str = file_deletion_4B3_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "CommandLine" in res["winlog"]["event_data"]:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210023"
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("file_deletion_4B3 finished.")
  return True

def file_deletion_4B4(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Indicator Removal on Host: File Deletion - T1070.004"
  query_str = file_deletion_4B4_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "CommandLine" in res["winlog"]["event_data"]:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210024"
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("file_deletion_4B4 finished.")
  return True

def file_and_directory_discovery_4C1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "File and Directory Discovery - T1083"
  query_str = file_and_directory_discovery_2A1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210025"
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("file_and_directory_discovery_4C1 finished.")
  return True

def system_owner_or_user_discovery_4C2(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "System Owner/User Discovery - T1033"
  query_str = system_owner_or_user_discovery_4C2_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210026"
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("system_owner_or_user_discovery_4C2 finished.")
  return True

def system_information_discovery_4C3(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "System Information Discovery - T1082"
  query_str = system_information_discovery_4C3_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "$env:COMPUTERNAME" in res["winlog"]["event_data"]["ScriptBlockText"]:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210027"
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("system_information_discovery_4C3 finished.")
  return True

def system_network_configuration_discovery_4C4(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "System Network Configuration Discovery - T1016"
  query_str = system_network_configuration_discovery_4C4_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "$env:USERDOMAIN" in res["winlog"]["event_data"]["ScriptBlockText"]:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210028"
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("system_network_configuration_discovery_4C4 finished.")
  return True

def process_discovery_4C5(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Process Discovery - T1057"
  query_str = process_discovery_4C5_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210029"
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("process_discovery_4C5 finished.")
  return True

def system_information_discovery_4C6(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "System Information Discovery - T1802"
  query_str = system_information_discovery_4C6_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Win32_OperatingSystem" in res["winlog"]["event_data"]["ScriptBlockText"]:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210030"
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("system_information_discovery_4C6 finished.")
  return True

def security_software_discovery_4C7(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Software Discovery: Security Software Discovery - T1518.001"
  query_str = security_software_discovery_4C7_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "AntiVirusProduct" in res["winlog"]["event_data"]["ScriptBlockText"]:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210031"
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("security_software_discovery_4C7 finished.")
  return True

def security_software_discovery_4C8(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Software Discovery: Security Software Discovery - T1518.001"
  query_str = security_software_discovery_4C8_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "FireWallProduct" in res["winlog"]["event_data"]["ScriptBlockText"]:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210032"
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("security_software_discovery_4C8 finished.")
  return True

def permission_groups_discovery_4C9(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Permission Groups Discovery - T1069"
  query_str = permission_groups_discovery_4C9_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Invoke-NetUserGetGroups" in res["winlog"]["event_data"]["ScriptBlockText"]:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210033"
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("permission_groups_discovery_4C9 finished.")
  return True

def execution_through_api_4C10(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Native API - T1106"
  query_str = execution_through_api_4C10_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Netapi32.dll" in res["winlog"]["event_data"]["ScriptBlockText"]:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210034"
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("execution_through_api_4C10 finished.")
  return True

def permission_groups_discovery_4C11(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Permission Groups Discovery - T1069"
  query_str = permission_groups_discovery_4C11_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Invoke-NetUserGetLocalGroups" in res["winlog"]["event_data"]["ScriptBlockText"]:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210035"
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("permission_groups_discovery_4C11 finished.")
  return True

def execution_through_api_4C12(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Native API - T1106"
  query_str = execution_through_api_4C12_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Netapi32.dll" in res["winlog"]["event_data"]["ScriptBlockText"]:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210036"
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("execution_through_api_4C12 finished.")
  return True

def new_service_5A1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Create or Modify System Process: Windows Service - T1543.003"
  query_str = new_service_5A1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "New-Service" in res["winlog"]["event_data"]["ScriptBlockText"]:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210037"
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("new_service_5A1 finished.")
  return True

def registry_run_keys_or_startup_folder_5B1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder - T1547.001"
  query_str = registry_run_keys_or_startup_folder_5B1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp" in res["winlog"]["event_data"]["TargetFilename"]:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210038"
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("registry_run_keys_or_startup_folder_5B1 finished.")
  return True

def private_keys_6B1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Unsecured Credentials: Private Keys - T1552.004"
  query_str = private_keys_6B1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if ".pfx" in res["winlog"]["event_data"]["TargetFilename"]:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210039"
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("private_keys_6B1 finished.")
  return True

def screen_capture_7A1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Screen Capture - T1113"
  query_str = screen_capture_7A1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "CopyFromScreen" in res["winlog"]["event_data"]["ScriptBlockText"]:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210040"
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("screen_capture_7A1 finished.")
  return True

def clipboard_data_7A2(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Clipboard Data - T1115"
  query_str = clipboard_data_7A2_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Get-Clipboard" in res["winlog"]["event_data"]["ScriptBlockText"]:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210041"
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("clipboard_data_7A2 finished.")
  return True

def input_capture_7A3(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Input Capture - T1056"
  query_str = input_capture_7A3_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "GetAsyncKeyState" in res["winlog"]["event_data"]["ScriptBlockText"]:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210042"
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("input_capture_7A3 finished.")
  return True

def data_compressed_7B2(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Archive Collected Data - T1560"
  query_str = data_compressed_7B2_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Compress-7Zip" in res["winlog"]["event_data"]["ScriptBlockText"]:
        if ".7z" in res["winlog"]["event_data"]["ScriptBlockText"]:
          suricata_output = suricata_output_format()
          suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
          suricata_output["alert"]["category"] = TECHNIQUE
          suricata_output["alert"]["signature_id"] = "20210043"
          suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
          suricata_output["log_time"] = res["@timestamp"]
          suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
          suricata_output["user_data1"] = res
          es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("data_compressed_7B2 finished.")
  return True

def data_encrypted_7B3(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Archive Collected Data - T1560"
  query_str = data_encrypted_7B3_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Compress-7Zip" in res["winlog"]["event_data"]["ScriptBlockText"]:
        if "-Password" in res["winlog"]["event_data"]["ScriptBlockText"]:
          suricata_output = suricata_output_format()
          suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
          suricata_output["alert"]["category"] = TECHNIQUE
          suricata_output["alert"]["signature_id"] = "20210044"
          suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
          suricata_output["log_time"] = res["@timestamp"]
          suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
          suricata_output["user_data1"] = res
          es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("data_encrypted_7B3 finished.")
  return True

def remote_system_discovery_8A1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Remote System Discovery - T1018"
  query_str = remote_system_discovery_8A1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210045"
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("remote_system_discovery_8A1 finished.")
  return True

def windows_remote_management_8A2(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Remote Services: Windows Remote Management - T1021.006"
  query_str = windows_remote_management_8A2_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210046"
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("windows_remote_management_8A2 finished.")
  return True

def process_discovery_8A3(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Process Discovery - T1057"
  query_str = process_discovery_8A3_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Get-Process" in res["winlog"]["event_data"]["ScriptBlockText"]:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210047"
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("process_discovery_8A3 finished.")
  return True

def remote_file_copy_8B1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Ingress Tool Transfer - T1105"
  query_str = remote_file_copy_8B1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210048"
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("remote_file_copy_8B1 finished.")
  return True

def valid_accounts_8C1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Valid Accounts - T1078"
  query_str = valid_accounts_8C1_query(es_start_time, es_end_time)
  SYSTEM_DEFAULT_ACCOUNT = ["SYSTEM", "LOCAL SYSTEM", "LOCAL SERVICE", "NETWORK SERVICE", "UMFD-0", "UMFD-1", "DWM-1"]
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      target_user_name = res["winlog"]["event_data"]["TargetUserName"]
      if target_user_name not in SYSTEM_DEFAULT_ACCOUNT:
        if not target_user_name.endswith("$"):
          suricata_output = suricata_output_format()
          suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
          suricata_output["alert"]["category"] = TECHNIQUE
          suricata_output["alert"]["signature_id"] = "20210049"
          suricata_output["_log_type"] = "Microsoft-Windows-Security-Auditing"
          suricata_output["log_time"] = res["@timestamp"]
          suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
          suricata_output["user_data1"] = res
          es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("valid_accounts_8C1 finished.")
  return True

def windows_admin_shares_8C2(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Remote Services: SMB/Windows Admin Shares - T1021.002"
  query_str = windows_admin_shares_8C2_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210050"
      suricata_output["_log_type"] = "Microsoft-Windows-Security-Auditing"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("windows_admin_shares_8C2 finished.")
  return True

def service_execution_8C3(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "System Services: Service Execution - T1569.002"
  query_str = service_execution_8C3_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210051"
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("service_execution_8C3 finished.")
  return True

def remote_file_copy_9A1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Ingress Tool Transfer - T1105"
  query_str = remote_file_copy_9A1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210052"
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("remote_file_copy_9A1 finished.")
  return True

def remote_file_copy_9A2(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Ingress Tool Transfer - T1105"
  query_str = remote_file_copy_9A2_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210053"
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("remote_file_copy_9A2 finished.")
  return True

def powershell_9B1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Command and Scripting Interpreter: PowerShell - T1059.001"
  query_str = powershell_9B1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210054"
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("powershell_9B1 finished.")
  return True

def file_and_directory_discovery_9B2(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "File and Directory Discovery - T1083"
  query_str = file_and_directory_discovery_9B2_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210055"
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("file_and_directory_discovery_9B2 finished.")
  return True

def automated_collection_9B3(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Automated Collection - T1119"
  query_str = automated_collection_9B3_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210056"
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("automated_collection_9B3 finished.")
  return True

def data_from_local_system_9B4(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Data from Local System - T1005"
  query_str = data_from_local_system_9B4_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210057"
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("data_from_local_system_9B4 finished.")
  return True

def data_staged_9B5(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Data Staged - T1074"
  query_str = data_staged_9B5_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Compress-Archive" in res["winlog"]["event_data"]["ScriptBlockText"]:
        if "-DestinationPath" in res["winlog"]["event_data"]["ScriptBlockText"]:
          if ".zip" in res["winlog"]["event_data"]["ScriptBlockText"]:
            suricata_output = suricata_output_format()
            suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
            suricata_output["alert"]["category"] = TECHNIQUE
            suricata_output["alert"]["signature_id"] = "20210058"
            suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
            suricata_output["log_time"] = res["@timestamp"]
            suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
            suricata_output["user_data1"] = res
            es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("data_staged_9B5 finished.")
  return True

def data_encrypted_9B6(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Archive Collected Data - T1560"
  query_str = data_encrypted_9B6_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Rar.exe a" in res["winlog"]["event_data"]["ScriptBlockText"]:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210059"
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("data_encrypted_9B6 finished.")
  return True

def data_compressed_9B7(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Archive Collected Data - T1560"
  query_str = data_compressed_9B7_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Rar.exe" in res["winlog"]["event_data"]["Image"]:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210060"
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("data_compressed_9B7 finished.")
  return True

def file_deletion_9C1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Indicator Removal on Host: File Deletion - T1070.004"
  query_str = file_deletion_9C1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "CommandLine" in res["winlog"]["event_data"]:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210061"
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("file_deletion_9C1 finished.")
  return True

def file_deletion_9C2(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Indicator Removal on Host: File Deletion - T1070.004"
  query_str = file_deletion_9C2_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "CommandLine" in res["winlog"]["event_data"]:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210062"
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("file_deletion_9C2 finished.")
  return True

def file_deletion_9C3(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Indicator Removal on Host: File Deletion - T1070.004"
  query_str = file_deletion_9C3_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "CommandLine" in res["winlog"]["event_data"]:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210063"
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("file_deletion_9C3 finished.")
  return True

# To be determined
def file_deletion_9C4(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "Indicator Removal on Host: File Deletion - T1070.004"
  query_str = file_deletion_9C4_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "CommandLine" in res["winlog"]["event_data"]:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = "20210064"
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        suricata_output["log_time"] = res["@timestamp"]
        suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("file_deletion_9C4 finished.")
  return True

def service_execution_10A1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
  """
  Parameters:
    - es_conn: elasticsearch connection instance
    - ES_INPUT_INDEX: elasticsearch intput index name
    - ES_OUTPUT_INDEX: elasticsearch output index name
    - es_start_time: elasticsearch range query start time
    - ES_OUes_end_timeTPUT_INDEX: elasticsearch range query end time

  Returns:
    True
  """
  TECHNIQUE = "System Services: Service Execution - T1569.002"
  query_str = service_execution_10A1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=1000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = "20210065"
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      suricata_output["log_time"] = res["@timestamp"]
      suricata_output["@timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("service_execution_10A1 finished.")
  return True
