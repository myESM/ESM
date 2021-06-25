# -*- coding: utf-8 -*-
import json
import logging
from datetime import datetime

import pytz
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
from src.main.windows_rules_setting import virtualization_evasion_11A3_query
from src.main.windows_rules_setting import system_information_discovery_11A4_query
from src.main.windows_rules_setting import peripheral_device_discovery_11A5_query
from src.main.windows_rules_setting import system_owner_user_discovery_11A6_query
from src.main.windows_rules_setting import system_network_configuration_discovery_11A7_query
from src.main.windows_rules_setting import process_discovery_11A8_query
from src.main.windows_rules_setting import file_and_directory_discovery_11A9_query
from src.main.windows_rules_setting import decode_files_or_information_11A10_query
from src.main.windows_rules_setting import powershell_11A12_query
from src.main.windows_rules_setting import commomly_used_port_11A13_query
from src.main.windows_rules_setting import standard_application_layer_protocol_11A14_query
from src.main.windows_rules_setting import file_and_directory_discovery_12A1_query
from src.main.windows_rules_setting import security_software_discovery_12B1_query
from src.main.windows_rules_setting import system_information_discovery_13A1_query
from src.main.windows_rules_setting import system_network_configuration_discovery_13B1_query
from src.main.windows_rules_setting import system_owner_user_discovery_13C1_query
from src.main.windows_rules_setting import process_discovery_13D1_query
from src.main.windows_rules_setting import component_object_model_hijacking_14A1_query
from src.main.windows_rules_setting import bypass_user_accounnt_control_14A2_query
from src.main.windows_rules_setting import modify_registry_14A3_query
from src.main.windows_rules_setting import process_discovery_14B2_query
from src.main.windows_rules_setting import system_owner_user_discovery_15A1_query
from src.main.windows_rules_setting import remote_system_discovery_16A1_query
from src.main.windows_rules_setting import execution_through_api_16B2_query
from src.main.windows_rules_setting import windows_remote_management_16C1_query
from src.main.windows_rules_setting import valid_accounts_16C2_query
from src.main.windows_rules_setting import email_collection_17A1_query
from src.main.windows_rules_setting import data_staged_17B2_query
from src.main.windows_rules_setting import data_compressed_17C1_query
from src.main.windows_rules_setting import web_service_18A1_query
from src.main.windows_rules_setting import rundll32_20A1_query
from src.main.windows_rules_setting import windows_management_instrumentation_event_subscription_20A2_query
from src.main.windows_rules_setting import pass_the_ticket_20A2_query
from src.main.windows_rules_setting import windows_remote_management_20B2_query
from src.main.windows_rules_setting import create_account_20B3_query

taiwan_tz = pytz.timezone("Asia/Taipei")

def tz_convert(ts, tz_new="Asia/Taipei", tz_old="UTC"):
	tz_old = pytz.timezone(tz_old)
	tz_new = pytz.timezone(tz_new)
	ts = datetime.fromtimestamp(float(ts))
	return tz_old.localize(ts).astimezone(tz_new).isoformat()

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
  suricata_fields["src_port"] = 0
  suricata_fields["dest_ip"] = ""
  suricata_fields["dest_port"] = 0
  suricata_fields["proto"] = ""
  suricata_fields["metadata"] = {"flowbits" : []}
  suricata_fields["tx_id"] = ""
  suricata_fields["alert"] = {
                              "action" : "",
                              "gid" : 0,
                              "signature_id" : "",
                              "rev" : "",
                              "signature" : "",
                              "category" : "",
                              "severity" : 2,
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
  suricata_fields["module"] = "Winlog"
  suricata_fields["dump_status"] = "0"
  suricata_fields["ingest_timestamp"] = ""
  suricata_fields["ticket"] = "0"
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
    result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
    result_length = result["hits"]["total"]["value"]
    if result_length > 0:
      for res in result["hits"]["hits"]:
        res = res["_source"]
        # res_hashes = res["winlog"]["event_data"]["Hashes"]
        # # ToDo: virustotal API
        # res_md5 = res_hashes.split(",")[0].split("=")[1]
        # res_sha256 = res_hashes.split(",")[1].split("=")[1]
        # res_imphash = res_hashes.split(",")[2].split("=")[1]

        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210001)
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
    result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
    result_length = result["hits"]["total"]["value"]
    if result_length > 0:
      for res in result["hits"]["hits"]:
        res = res["_source"]
        if "\u202e" in res.get("winlog", "").get("event_data", "").get("Image", ""):
          suricata_output = suricata_output_format()
          suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
          suricata_output["alert"]["category"] = TECHNIQUE
          suricata_output["alert"]["signature_id"] = int(20210002)
          suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
          res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
          res_time_timestamp = datetime.timestamp(res_time)
          suricata_output["log_time"] = tz_convert(res_time_timestamp)
          suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if res.get("winlog", "").get("event_data", "").get("DestinationPort", "") not in WINDOWS_COMMON_PORT_LIST:
      # if res["winlog"]["event_data"]["DestinationPort"] not in WINDOWS_COMMON_PORT_LIST:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210003)
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210004)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210005)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210006)
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210007)
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210008)
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210009)
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Compress-Archive" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        if "-DestinationPath" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
          if ".zip" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
            suricata_output = suricata_output_format()
            suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
            suricata_output["alert"]["category"] = TECHNIQUE
            suricata_output["alert"]["signature_id"] = int(20210010)
            suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
            res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
            res_time_timestamp = datetime.timestamp(res_time)
            suricata_output["log_time"] = tz_convert(res_time_timestamp)
            suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210011)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210012)
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210013)
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210014)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if res.get("winlog", "").get("event_data", "").get("DestinationPort", "") in WINDOWS_COMMON_PORT_LIST:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210015)
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210016)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      res_scripts = res.get("winlog", "").get("event_data", "").get("ScriptBlockText", "")
      if "HKCU:\\" in res_scripts or "HKEY_CURRENT_USER" in res_scripts:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210017)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210018)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210019)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210020)
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210021)
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "CommandLine" in res.get("winlog", "").get("event_data", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210022)
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "CommandLine" in res.get("winlog", "").get("event_data", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210023)
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "CommandLine" in res.get("winlog", "").get("event_data", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210024)
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210025)
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210026)
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "$env:COMPUTERNAME" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210027)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "$env:USERDOMAIN" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210028)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210029)
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Win32_OperatingSystem" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210030)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "AntiVirusProduct" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210031)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "FireWallProduct" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210032)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Invoke-NetUserGetGroups" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210033)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Netapi32.dll" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210034)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Invoke-NetUserGetLocalGroups" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210035)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Netapi32.dll" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210036)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "New-Service" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210037)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp" in res.get("winlog", "").get("event_data", "").get("TargetFilename", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210038)
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if ".pfx" in res.get("winlog", "").get("event_data", "").get("TargetFilename", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210039)
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "CopyFromScreen" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210040)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Get-Clipboard" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210041)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "GetAsyncKeyState" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210042)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Compress-7Zip" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        if ".7z" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
          suricata_output = suricata_output_format()
          suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
          suricata_output["alert"]["category"] = TECHNIQUE
          suricata_output["alert"]["signature_id"] = int(20210043)
          suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
          res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
          res_time_timestamp = datetime.timestamp(res_time)
          suricata_output["log_time"] = tz_convert(res_time_timestamp)
          suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Compress-7Zip" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        if "-Password" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
          suricata_output = suricata_output_format()
          suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
          suricata_output["alert"]["category"] = TECHNIQUE
          suricata_output["alert"]["signature_id"] = int(20210044)
          suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
          res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
          res_time_timestamp = datetime.timestamp(res_time)
          suricata_output["log_time"] = tz_convert(res_time_timestamp)
          suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210045)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210046)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Get-Process" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210047)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210048)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      target_user_name = res.get("winlog", "").get("event_data", "").get("TargetUserName", "")
      if target_user_name not in SYSTEM_DEFAULT_ACCOUNT:
        if not target_user_name.endswith("$"):
          suricata_output = suricata_output_format()
          suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
          suricata_output["alert"]["category"] = TECHNIQUE
          suricata_output["alert"]["signature_id"] = int(20210049)
          suricata_output["_log_type"] = "Microsoft-Windows-Security-Auditing"
          res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
          res_time_timestamp = datetime.timestamp(res_time)
          suricata_output["log_time"] = tz_convert(res_time_timestamp)
          suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210050)
      suricata_output["_log_type"] = "Microsoft-Windows-Security-Auditing"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210051)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210052)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210053)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210054)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210055)
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210056)
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210057)
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Compress-Archive" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        if "-DestinationPath" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
          if ".zip" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
            suricata_output = suricata_output_format()
            suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
            suricata_output["alert"]["category"] = TECHNIQUE
            suricata_output["alert"]["signature_id"] = int(20210058)
            suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
            res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
            res_time_timestamp = datetime.timestamp(res_time)
            suricata_output["log_time"] = tz_convert(res_time_timestamp)
            suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Rar.exe a" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210059)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Rar.exe" in res.get("winlog", "").get("event_data", "").get("Image", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210060)
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "CommandLine" in res.get("winlog", "").get("event_data", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210061)
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "CommandLine" in res.get("winlog", "").get("event_data", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210062)
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "CommandLine" in res.get("winlog", "").get("event_data", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210063)
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "CommandLine" in res.get("winlog", "").get("event_data", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210064)
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
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
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210065)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("service_execution_10A1 finished.")
  return True

def virtualization_evasion_11A3(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  TECHNIQUE = "Virtualization/Sandbox Evasion - T1497"
  query_str = virtualization_evasion_11A3_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210101)
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("virtualization_evasion_11A3 finished.")
  return True

def system_information_discovery_11A4(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = system_information_discovery_11A4_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Win32_ComputerSystem" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210102)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("system_information_discovery_11A4 finished.")
  return True

def peripheral_device_discovery_11A5(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  TECHNIQUE = "Peripheral Device Discovery - T1120"
  query_str = peripheral_device_discovery_11A5_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210103)
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("peripheral_device_discovery_11A5 finished.")
  return True

def system_owner_user_discovery_11A6(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = system_owner_user_discovery_11A6_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Win32_ComputerSystem" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210104)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("system_owner_user_discovery_11A6 finished.")
  return True

def system_network_configuration_discovery_11A7(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = system_network_configuration_discovery_11A7_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Win32_ComputerSystem" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210105)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("system_network_configuration_discovery_11A7 finished.")
  return True

def process_discovery_11A8(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = process_discovery_11A8_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210106)
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("process_discovery_11A8 finished.")
  return True

def file_and_directory_discovery_11A9(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = file_and_directory_discovery_11A9_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210107)
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("file_and_directory_discovery_11A9 finished.")
  return True

def decode_files_or_information_11A10(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = decode_files_or_information_11A10_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210108)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("decode_files_or_information_11A10 finished.")
  return True

def powershell_11A12(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = powershell_11A12_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210109)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("powershell_11A12 finished.")
  return True

def commomly_used_port_11A13(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  WINDOWS_COMMON_PORT_LIST = ["443"]
  query_str = commomly_used_port_11A13_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if res.get("winlog", "").get("event_data", "").get("DestinationPort", "") in WINDOWS_COMMON_PORT_LIST:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210110)
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("commomly_used_port_11A13 finished.")
  return True

def standard_application_layer_protocol_11A14(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = standard_application_layer_protocol_11A14_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210111)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("standard_application_layer_protocol_11A14 finished.")
  return True

def file_and_directory_discovery_12A1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = file_and_directory_discovery_12A1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210112)
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("file_and_directory_discovery_12A1 finished.")
  return True

def security_software_discovery_12B1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = security_software_discovery_12B1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210113)
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("security_software_discovery_12B1 finished.")
  return True

def system_information_discovery_13A1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = system_information_discovery_13A1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "GetComputerNameEx" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210114)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("system_information_discovery_13A1 finished.")
  return True

def system_network_configuration_discovery_13B1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = system_network_configuration_discovery_13B1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "NetWkstaGetInfo" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210115)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("system_network_configuration_discovery_13B1 finished.")
  return True

def system_owner_user_discovery_13C1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = system_owner_user_discovery_13C1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "GetUserNameEx" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210116)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("system_owner_user_discovery_13C1 finished.")
  return True

def process_discovery_13D1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = process_discovery_13D1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "CreateToolhelp32Snapshot" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210117)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("process_discovery_13D1 finished.")
  return True

def component_object_model_hijacking_14A1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = component_object_model_hijacking_14A1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "DelegateExecute" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210118)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("component_object_model_hijacking_14A1 finished.")
  return True

def bypass_user_accounnt_control_14A2(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = bypass_user_accounnt_control_14A2_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210119)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("bypass_user_accounnt_control_14A2 finished.")
  return True

def modify_registry_14A3(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = modify_registry_14A3_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      res_scripts = res.get("winlog", "").get("event_data", "").get("ScriptBlockText", "")
      if "HKCU:\\" in res_scripts or "HKEY_CURRENT_USER" in res_scripts:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210120)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("modify_registry_14A3 finished.")
  return True

def process_discovery_14B2(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = process_discovery_14B2_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Get-Process" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210121)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("process_discovery_14B2 finished.")
  return True

def system_owner_user_discovery_15A1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = system_owner_user_discovery_15A1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "$env:username" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210123)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("system_owner_user_discovery_15A1 finished.")
  return True

def remote_system_discovery_16A1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = remote_system_discovery_16A1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210124)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("remote_system_discovery_16A1 finished.")
  return True

def execution_through_api_16B2(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = execution_through_api_16B2_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "Advapi32.dll" in res.get("winlog", "").get("event_data", "").get("ScriptBlockText", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210125)
        suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("execution_through_api_16B2 finished.")
  return True

def windows_remote_management_16C1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = windows_remote_management_16C1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210126)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("windows_remote_management_16C1 finished.")
  return True

def valid_accounts_16C2(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = valid_accounts_16C2_query(es_start_time, es_end_time)
  SYSTEM_DEFAULT_ACCOUNT = ["SYSTEM", "LOCAL SYSTEM", "LOCAL SERVICE", "NETWORK SERVICE", "UMFD-0", "UMFD-1", "DWM-1"]
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      target_user_name = res.get("winlog", "").get("event_data", "").get("TargetUserName", "")
      if target_user_name not in SYSTEM_DEFAULT_ACCOUNT:
        if not target_user_name.endswith("$"):
          suricata_output = suricata_output_format()
          suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
          suricata_output["alert"]["category"] = TECHNIQUE
          suricata_output["alert"]["signature_id"] = int(20210127)
          suricata_output["_log_type"] = "Microsoft-Windows-Security-Auditing"
          res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
          res_time_timestamp = datetime.timestamp(res_time)
          suricata_output["log_time"] = tz_convert(res_time_timestamp)
          suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
          suricata_output["user_data1"] = res
          es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("valid_accounts_16C2 finished.")
  return True

def email_collection_17A1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  TECHNIQUE = "Email Collection - T1114"
  query_str = email_collection_17A1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      parent_image = res.get("winlog", "").get("event_data", "").get("ParentImage", "")
      if "powershell" in parent_image or "svchost" in parent_image:
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210128)
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("email_collection_17A1 finished.")
  return True

def data_staged_17B2(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = data_staged_17B2_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210129)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("data_staged_17B2 finished.")
  return True

def data_compressed_17C1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = data_compressed_17C1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210130)
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("data_compressed_17C1 finished.")
  return True

def web_service_18A1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  TECHNIQUE = "Web Service - T1102"
  query_str = web_service_18A1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210131)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("web_service_18A1 finished.")
  return True

def rundll32_20A1(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  TECHNIQUE = "Signed Binary Proxy Execution: Rundll32 - T1218.011"
  query_str = rundll32_20A1_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210132)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("rundll32_20A1 finished.")
  return True

def windows_management_instrumentation_event_subscription_20A2(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  TECHNIQUE = "Event Triggered Execution: Windows Management Instrumentation Event Subscription - T1546.003"
  query_str = windows_management_instrumentation_event_subscription_20A2_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210133)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("windows_management_instrumentation_event_subscription_20A2 finished.")
  return True

def pass_the_ticket_20A2(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  TECHNIQUE = "Use Alternate Authentication Material: Pass the Ticket - T1550.003"
  query_str = pass_the_ticket_20A2_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210134)
      suricata_output["_log_type"] = "Microsoft-Windows-PowerShell"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("pass_the_ticket_20A2 finished.")
  return True

def windows_remote_management_20B2(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  query_str = windows_remote_management_20B2_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      suricata_output = suricata_output_format()
      suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["alert"]["category"] = TECHNIQUE
      suricata_output["alert"]["signature_id"] = int(20210135)
      suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
      res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
      res_time_timestamp = datetime.timestamp(res_time)
      suricata_output["log_time"] = tz_convert(res_time_timestamp)
      suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
      suricata_output["user_data1"] = res
      es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("windows_remote_management_20B2 finished.")
  return True

def create_account_20B3(es_conn, ES_INPUT_INDEX, ES_OUTPUT_INDEX, es_start_time, es_end_time):
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
  TECHNIQUE = "Create Account - T1136"
  query_str = create_account_20B3_query(es_start_time, es_end_time)
  result = es_conn.es.search(index=ES_INPUT_INDEX, body=query_str, from_=0, size=20000)
  result_length = result["hits"]["total"]["value"]
  if result_length > 0:
    for res in result["hits"]["hits"]:
      res = res["_source"]
      if "/user" in res.get("winlog", "").get("event_data", "").get("CommandLine", ""):
        suricata_output = suricata_output_format()
        suricata_output["timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["alert"]["category"] = TECHNIQUE
        suricata_output["alert"]["signature_id"] = int(20210136)
        suricata_output["_log_type"] = "Microsoft-Windows-Sysmon"
        res_time = datetime.strptime(res["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        res_time_timestamp = datetime.timestamp(res_time)
        suricata_output["log_time"] = tz_convert(res_time_timestamp)
        suricata_output["@timestamp"] = datetime.now(tz=taiwan_tz).isoformat()
        suricata_output["user_data1"] = res
        es_conn.insert_result(ES_OUTPUT_INDEX, suricata_output)
  logging.info("create_account_20B3 finished.")
  return True
