# -*- coding: utf-8 -*-
def user_execution_1A1_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 1.A.1, User Execution, T1204
  https://attack.mitre.org/techniques/T1204/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string list.
  """
  event_id = "1"
  event_provider = "Microsoft-Windows-Sysmon"
  common_file_extensions = ["*.doc", "*.pdf", "*.xls", "*.rtf", "*.scr", "*.exe", "*.lnk", "*.pif", "*.cpl"]
  user_extension_query_list = []
  for ext in common_file_extensions:
    user_extension_query_str = {
      "query": {
        "bool": {
          "must": [{
            "match": {
              "winlog.event_id": event_id
            }
          },
          {
            "match": {
              "winlog.provider_name": event_provider
            }
          },
          {
            "wildcard": {
              "winlog.event_data.Image": ext
            }
          },
          {
            "range": {
              "@timestamp": {
                "gte": es_start_time,
                "lte": es_end_time
              }
            }
          }]
        }
      }
    }
    user_extension_query_list.append(user_extension_query_str)
  return user_extension_query_list

def masquerading_1A2_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 1.A.2, Masquerading, T1036
  https://attack.mitre.org/techniques/T1036/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string list.
  """
  event_id = "1"
  event_provider = "Microsoft-Windows-Sysmon"
  common_file_extensions = ["*.doc", "*.pdf", "*.xls", "*.rtf", "*.scr", "*.exe", "*.lnk", "*.pif", "*.cpl"]
  masquerading_query_list = []
  for ext in common_file_extensions:
    masquerading_query_str = {
      "query": {
        "bool": {
          "must": [{
            "match": {
              "winlog.event_id": event_id
            }
          },
          {
            "match": {
              "winlog.provider_name": event_provider
            }
          },
          {
            "wildcard": {
              "winlog.event_data.Image": ext
            }
          },
          {
            "range": {
              "@timestamp": {
                "gte": es_start_time,
                "lte": es_end_time
              }
            }
          }]
        }
      }
    }
    masquerading_query_list.append(masquerading_query_str)
  return masquerading_query_list

def non_standard_port_1A3_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 1.A.3, Non-Standard Port, T1571
  https://attack.mitre.org/techniques/T1571/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "3"
  event_provider = "Microsoft-Windows-Sysmon"
  non_standard_port_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return non_standard_port_str

def command_line_interface_1B1_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 1.B.1, Command and Scripting Interpreter: Windows Command Shell, T1059.003
  https://attack.mitre.org/techniques/T1059/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "1"
  event_provider = "Microsoft-Windows-Sysmon"
  command_line_interface_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.Image": "*cmd.exe*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return command_line_interface_str

def powershell_1B2_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 1.B.2, Command and Scripting Interpreter: PowerShell, T1059.001
  https://attack.mitre.org/techniques/T1059/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "1"
  event_provider = "Microsoft-Windows-Sysmon"
  powershell_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.Image": "*powershell.exe"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return powershell_str

def file_and_directory_discovery_2A1_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 2.A.1, File and Directory Discovery, T1083
  https://attack.mitre.org/techniques/T1083/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  file_and_directory_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ScriptBlockText": "*ChildItem*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return file_and_directory_discovery_str

def automated_collection_2A2_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 2.A.2, Automated Collection, T1119
  https://attack.mitre.org/techniques/T1119/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  automated_collection_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ScriptBlockText": "*ChildItem*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return automated_collection_str

def data_from_local_system_2A3_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 2.A.3, Data from Local System, T1005
  https://attack.mitre.org/techniques/T1005/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  data_from_local_system_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ScriptBlockText": "*$env:USERPROFILE*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return data_from_local_system_str

def data_compressed_2A4_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 2.A.4, Archive Collected Data, T1560
  https://attack.mitre.org/techniques/T1560/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  data_compressed_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ScriptBlockText": "*Compress-Archive*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return data_compressed_str

def data_staged_2A5_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 2.A.5, Data Staged, T1074
  https://attack.mitre.org/techniques/T1074/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  data_staged_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return data_staged_str

def remote_file_copy_3A1_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 3.A.1, Ingress Tool Transfer, T1105
  https://attack.mitre.org/techniques/T1105/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "11"
  rule_name = "Downloads"
  event_provider = "Microsoft-Windows-Sysmon"
  remote_file_copy_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "match": {
            "winlog.event_data.RuleName": rule_name
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return remote_file_copy_str

def obfuscated_files_or_information_3A2_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 3.A.2, Obfuscated Files or Information, T1027
  https://attack.mitre.org/techniques/T1027/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  obfuscated_files_or_information_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ScriptBlockText": "*GetPixel*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }],
        "should": [{
          "wildcard": {
            "winlog.event_data.ScriptBlockText": "*for*"
          }
        }]
      }
    }
  }
  return obfuscated_files_or_information_str

def component_object_model_hijacking_3B1_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 3.B.1, Event Triggered Execution: Component Object Model Hijacking, T1546.015
  https://attack.mitre.org/techniques/T1546/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  component_object_model_hijacking_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ScriptBlockText": "*DelegateExecute*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return component_object_model_hijacking_str

def bypass_user_accounnt_control_3B2_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 3.B.1, Abuse Elevation Control Mechanism: Bypass User Access Control, T1548.002
  https://attack.mitre.org/techniques/T1548/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "1"
  event_provider = "Microsoft-Windows-Sysmon"
  bypass_user_accounnt_control_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.Image": "*sdclt.exe*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return bypass_user_accounnt_control_str

def commomly_used_port_3B3_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 3.B.3, Commonly Used Port, T1436
  https://attack.mitre.org/techniques/T1436/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "3"
  event_provider = "Microsoft-Windows-Sysmon"
  commomly_used_port_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return commomly_used_port_str

def standard_application_layer_protocol_3B4_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 3.B.4, Application Layer Protocol, T1071
  https://attack.mitre.org/techniques/T1071/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "3"
  event_provider = "Microsoft-Windows-Sysmon"
  standard_application_layer_protocol_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "match": {
            "winlog.event_data.DestinationPortName": "https"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return standard_application_layer_protocol_str

def modify_registry_3C1_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 3.C.1, Modify Registry, T1112
  https://attack.mitre.org/techniques/T1112/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  modify_registry_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ScriptBlockText": "*Remove-Item*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return modify_registry_str

def remote_file_copy_4A1_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 4.A.1, Ingress Tool Transfer, T1105
  https://attack.mitre.org/techniques/T1105/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "11"
  rule_name = "Downloads"
  event_provider = "Microsoft-Windows-Sysmon"
  remote_file_copy_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "match": {
            "winlog.event_data.RuleName": rule_name
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return remote_file_copy_str

def powershell_4A2_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 4.A.2, Command and Scripting Interpreter: PowerShell, T1059.001
  https://attack.mitre.org/techniques/T1059/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "1"
  event_provider = "Microsoft-Windows-Sysmon"
  powershell_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.Image": "*powershell.exe"
          }
        },
        {
          "wildcard": {
            "winlog.event_data.Image": "*powershell.exe"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return powershell_str

def decode_files_or_information_4A3_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 4.A.3, Deobfuscate/Decode Files or Information, T1140
  https://attack.mitre.org/techniques/T1140/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  decode_files_or_information_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ScriptBlockText": "*Expand-Archive*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return decode_files_or_information_str

def process_discovery_4B1_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 4.B.1, Process Discovery, T1057
  https://attack.mitre.org/techniques/T1057/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  process_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ScriptBlockText": "*Get-Process*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return process_discovery_str

def file_deletion_4B2_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 4.B.2, Indicator Removal on Host: File Deletion, T1070.004
  https://attack.mitre.org/techniques/T1070/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "1"
  event_provider = "Microsoft-Windows-Sysmon"
  file_deletion_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.Image": "*sdelete64.exe*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return file_deletion_str

def file_deletion_4B3_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 4.B.3, Indicator Removal on Host: File Deletion, T1070.004
  https://attack.mitre.org/techniques/T1070/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "1"
  event_provider = "Microsoft-Windows-Sysmon"
  file_deletion_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.Image": "*sdelete64.exe*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return file_deletion_str

def file_deletion_4B4_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 4.B.4, Indicator Removal on Host: File Deletion, T1070.004
  https://attack.mitre.org/techniques/T1070/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "1"
  event_provider = "Microsoft-Windows-Sysmon"
  file_deletion_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.Image": "*sdelete64.exe*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return file_deletion_str

def file_and_directory_discovery_4C1_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 4.C.1, File and Directory Discovery, T1083
  https://attack.mitre.org/techniques/T1083/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  file_and_directory_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ScriptBlockText": "*$env:TEMP*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return file_and_directory_discovery_str

def system_owner_or_user_discovery_4C2_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 4.C.2, System Owner/User Discovery, T1033
  https://attack.mitre.org/techniques/T1033/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  system_owner_or_user_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ScriptBlockText": "*$env:USERNAME*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return system_owner_or_user_discovery_str

def system_information_discovery_4C3_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 4.C.3, System Information Discovery, T1082
  https://attack.mitre.org/techniques/T1082/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  system_information_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return system_information_discovery_str

def system_network_configuration_discovery_4C4_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 4.C.4, System Network Configuration Discovery, T1016
  https://attack.mitre.org/techniques/T1016/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  system_network_configuration_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return system_network_configuration_discovery_str

def process_discovery_4C5_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 4.C.5, Process Discovery, T1057
  https://attack.mitre.org/techniques/T1057/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  process_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ScriptBlockText": "*$PID*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return process_discovery_str

def system_information_discovery_4C6_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 4.C.6, System Information Discovery, T1082
  https://attack.mitre.org/techniques/T1082/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  system_information_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return system_information_discovery_str

def security_software_discovery_4C7_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 4.C.7, Software Discovery: Security Software Discovery, T1518.001
  https://attack.mitre.org/techniques/T1518/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  security_software_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return security_software_discovery_str

def security_software_discovery_4C8_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 4.C.8, Software Discovery: Security Software Discovery, T1518.001
  https://attack.mitre.org/techniques/T1518/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  security_software_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return security_software_discovery_str

def permission_groups_discovery_4C9_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 4.C.9, Permission Groups Discovery, T1069
  https://attack.mitre.org/techniques/T1069/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  permission_groups_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return permission_groups_discovery_str

def execution_through_api_4C10_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 4.C.10, Native API, T1106
  https://attack.mitre.org/techniques/T1106/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  execution_through_api_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return execution_through_api_str

def permission_groups_discovery_4C11_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 4.C.11, Permission Groups Discovery, T1069
  https://attack.mitre.org/techniques/T1069/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  permission_groups_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return permission_groups_discovery_str

def execution_through_api_4C12_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 4.C.12, Native API, T1106
  https://attack.mitre.org/techniques/T1106/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  execution_through_api_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return execution_through_api_str

def new_service_5A1_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 5.A.1, Create or Modify System Process: Windows Service, T1543.003
  https://attack.mitre.org/techniques/T1543/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  new_service_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return new_service_str

def registry_run_keys_or_startup_folder_5B1_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 5.B.1, Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder, T1547.001
  https://attack.mitre.org/techniques/T1547/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "11"
  event_provider = "Microsoft-Windows-Sysmon"
  registry_run_keys_or_startup_folder_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return registry_run_keys_or_startup_folder_str

def private_keys_6B1_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 6.B.1, Unsecured Credentials: Private Keys, T1552.004
  https://attack.mitre.org/techniques/T1552/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "11"
  event_provider = "Microsoft-Windows-Sysmon"
  private_keys_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return private_keys_str

def screen_capture_7A1_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 7.A.1, Screen Capture, T1113
  https://attack.mitre.org/techniques/T1113/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  screen_capture_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return screen_capture_str

def clipboard_data_7A2_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 7.A.2, Clipboard Data, T1115
  https://attack.mitre.org/techniques/T1115/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  clipboard_data_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return clipboard_data_str

def input_capture_7A3_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 7.A.3, Input Capture, T1056
  https://attack.mitre.org/techniques/T1056/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  input_capture_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return input_capture_str

def data_compressed_7B2_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 7.B.2, Archive Collected Data, T1560
  https://attack.mitre.org/techniques/T1560/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  data_compressed_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return data_compressed_str

def data_encrypted_7B3_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 7.B.3, Archive Collected Data, T1560
  https://attack.mitre.org/techniques/T1560/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  data_encrypted_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return data_encrypted_str

def remote_system_discovery_8A1_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 8.A.1, Remote System Discovery, T1018
  https://attack.mitre.org/techniques/T1018/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "3"
  event_provider = "Microsoft-Windows-Sysmon"
  remote_system_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "match": {
            "winlog.event_data.DestinationPort": "389"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return remote_system_discovery_str

def windows_remote_management_8A2_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 8.A.2, Remote Services: Windows Remote Management, T1021.006
  https://attack.mitre.org/techniques/T1021/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "3"
  event_provider = "Microsoft-Windows-Sysmon"
  windows_remote_management_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "match": {
            "winlog.event_data.DestinationPort": "5985"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return windows_remote_management_str

def process_discovery_8A3_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 8.A.3, Process Discovery, T1057
  https://attack.mitre.org/techniques/T1057/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  process_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return process_discovery_str

def remote_file_copy_8B1_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 8.B.1, Ingress Tool Transfer, T1105
  https://attack.mitre.org/techniques/T1105/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "11"
  rule_name = "EXE"
  event_provider = "Microsoft-Windows-Sysmon"
  remote_file_copy_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "match": {
            "winlog.event_data.RuleName": rule_name
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return remote_file_copy_str

def valid_accounts_8C1_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 8.C.1, Valid Accounts, T1078
  https://attack.mitre.org/techniques/T1078/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4624"
  event_provider = "Microsoft-Windows-Security-Auditing"
  valid_accounts_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return valid_accounts_str

def windows_admin_shares_8C2_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 8.C.2, Remote Services: SMB/Windows Admin Shares, T1021.002
  https://attack.mitre.org/techniques/T1021/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4648"
  event_provider = "Microsoft-Windows-Security-Auditing"
  windows_admin_shares_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "match": {
            "winlog.event_data.IpPort": "445"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return windows_admin_shares_str

def service_execution_8C3_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 8.C.3, System Services: Service Execution, T1569.002
  https://attack.mitre.org/techniques/T11569/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "1"
  event_provider = "Microsoft-Windows-Sysmon"
  service_execution_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ParentImage": "*PSEXESVC.exe*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return service_execution_str

def remote_file_copy_9A1_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 9.A.1, Ingress Tool Transfer, T1105
  https://attack.mitre.org/techniques/T1105/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "11"
  rule_name = "EXE"
  event_provider = "Microsoft-Windows-Sysmon"
  remote_file_copy_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "match": {
            "winlog.event_data.RuleName": rule_name
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return remote_file_copy_str

def remote_file_copy_9A2_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 9.A.2, Ingress Tool Transfer, T1105
  https://attack.mitre.org/techniques/T1105/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "11"
  rule_name = "EXE"
  event_provider = "Microsoft-Windows-Sysmon"
  remote_file_copy_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "match": {
            "winlog.event_data.RuleName": rule_name
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return remote_file_copy_str

def powershell_9B1_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 9.B.1, Command and Scripting Interpreter: PowerShell, T1059.001
  https://attack.mitre.org/techniques/T1059/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "1"
  event_provider = "Microsoft-Windows-Sysmon"
  powershell_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.Image": "*powershell.exe*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return powershell_str

def file_and_directory_discovery_9B2_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 9.B.2, File and Directory Discovery, T1083
  https://attack.mitre.org/techniques/T1083/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  file_and_directory_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ScriptBlockText": "*ChildItem*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return file_and_directory_discovery_str

def automated_collection_9B3_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 9.B.3, Automated Collection, T1119
  https://attack.mitre.org/techniques/T1119/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  automated_collection_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ScriptBlockText": "*ChildItem*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return automated_collection_str

def data_from_local_system_9B4_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 9.B.4, Data from Local System, T1005
  https://attack.mitre.org/techniques/T1005/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  data_from_local_system_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ScriptBlockText": "*$env:USERPROFILE*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return data_from_local_system_str

def data_staged_9B5_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 9.B.5, Data Staged, T1074
  https://attack.mitre.org/techniques/T1074/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  data_staged_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return data_staged_str

def data_encrypted_9B6_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 9.B.6, Archive Collected Data, T1560
  https://attack.mitre.org/techniques/T1560/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  data_encrypted_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return data_encrypted_str

def data_compressed_9B7_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 9.B.7, Archive Collected Data, T1560
  https://attack.mitre.org/techniques/T1560/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "1"
  event_provider = "Microsoft-Windows-Sysmon"
  data_compressed_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return data_compressed_str

def file_deletion_9C1_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 9.C.1, Indicator Removal on Host: File Deletion, T1070.004
  https://attack.mitre.org/techniques/T1070/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "1"
  event_provider = "Microsoft-Windows-Sysmon"
  file_deletion_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.Image": "*sdelete64.exe*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return file_deletion_str

def file_deletion_9C2_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 9.C.2, Indicator Removal on Host: File Deletion, T1070.004
  https://attack.mitre.org/techniques/T1070/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "1"
  event_provider = "Microsoft-Windows-Sysmon"
  file_deletion_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.Image": "*sdelete64.exe*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return file_deletion_str

def file_deletion_9C3_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 9.C.3, Indicator Removal on Host: File Deletion, T1070.004
  https://attack.mitre.org/techniques/T1070/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "1"
  event_provider = "Microsoft-Windows-Sysmon"
  file_deletion_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.Image": "*sdelete64.exe*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return file_deletion_str

def file_deletion_9C4_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 9.C.4, Indicator Removal on Host: File Deletion, T1070.004
  https://attack.mitre.org/techniques/T1070/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "1"
  event_provider = "Microsoft-Windows-Sysmon"
  file_deletion_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.Image": "*cmd.exe*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return file_deletion_str

def service_execution_10A1_query(es_start_time, es_end_time):
  """
  APT29, First Scenario, 10.A.1, System Services: Service Execution, T1569.002
  https://attack.mitre.org/techniques/T1569/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "1"
  event_provider = "Microsoft-Windows-Sysmon"
  service_execution_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ParentImage": "*services.exe*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return service_execution_str

def virtualization_evasion_11A3_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 11.A.3, Virtualization/Sandbox Evasion, T1497
  https://attack.mitre.org/techniques/T1497/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  virtualization_evasion_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ScriptBlockText": "*Win32_BIOS*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return virtualization_evasion_str

def system_information_discovery_11A4_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 11.A.4, System Information Discovery, T1082
  https://attack.mitre.org/techniques/T1082/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  system_information_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return system_information_discovery_str

def peripheral_device_discovery_11A5_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 11.A.5, Peripheral Device Discovery, T1120
  https://attack.mitre.org/techniques/T1120/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  peripheral_device_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ScriptBlockText": "*Win32_PnPEntity*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return peripheral_device_discovery_str

def system_owner_user_discovery_11A6_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 11.A.6, System Owner/User Discovery, T1033
  https://attack.mitre.org/techniques/T1033/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  system_owner_user_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return system_owner_user_discovery_str

def system_network_configuration_discovery_11A7_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 11.A.7, System Network Configuration Discovery, T1016
  https://attack.mitre.org/techniques/T1016/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  system_network_configuration_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return system_network_configuration_discovery_str

def process_discovery_11A8_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 11.A.8, Process Discovery, T1057
  https://attack.mitre.org/techniques/T1057/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  process_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ScriptBlockText": "*Win32_Process*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return process_discovery_str

def file_and_directory_discovery_11A9_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 11.A.9, File and Directory Discovery, T1083
  https://attack.mitre.org/techniques/T1083/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  file_and_directory_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ScriptBlockText": "*Get-Item*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return file_and_directory_discovery_str

def decode_files_or_information_11A10_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 11.A.10, Deobfuscate/Decode Files or Information, T1140
  https://attack.mitre.org/techniques/T1140/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "1"
  event_provider = "Microsoft-Windows-Sysmon"
  decode_files_or_information_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.Image": "*certutil.exe*"
          }
        },
        {
          "wildcard":{
            "winlog.event_data.CommandLine": "*-decode*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return decode_files_or_information_str

def powershell_11A12_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 11.A.12, Command and Scripting Interpreter: PowerShell, T1059.001
  https://attack.mitre.org/techniques/T1059/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "1"
  event_provider = "Microsoft-Windows-Sysmon"
  powershell_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.Image": "*powershell.exe*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return powershell_str

def commomly_used_port_11A13_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 11.A.13, Commonly Used Port, T1436
  https://attack.mitre.org/techniques/T1436/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "3"
  event_provider = "Microsoft-Windows-Sysmon"
  commomly_used_port_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return commomly_used_port_str

def standard_application_layer_protocol_11A14_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 11.A.4, Application Layer Protocol, T1071
  https://attack.mitre.org/techniques/T1071/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "3"
  event_provider = "Microsoft-Windows-Sysmon"
  standard_application_layer_protocol_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "match": {
            "winlog.event_data.DestinationPortName": "https"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return standard_application_layer_protocol_str

def file_and_directory_discovery_12A1_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 12.A.1, File and Directory Discovery, T1083
  https://attack.mitre.org/techniques/T1083/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  file_and_directory_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ScriptBlockText": "*env:windir*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return file_and_directory_discovery_str

def security_software_discovery_12B1_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 12.B.1, Software Discovery: Security Software Discovery, T1518.001
  https://attack.mitre.org/techniques/T1518/001/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  security_software_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ScriptBlockText": "*AntiVirusProduct*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return security_software_discovery_str

def system_information_discovery_13A1_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 13.A.1, System Information Discovery, T1082
  https://attack.mitre.org/techniques/T1082/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  system_information_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return system_information_discovery_str

def system_network_configuration_discovery_13B1_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 13.B.1, System Network Configuration Discovery, T1016
  https://attack.mitre.org/techniques/T1016/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  system_network_configuration_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return system_network_configuration_discovery_str

def system_owner_user_discovery_13C1_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 13.C.1, System Owner/User Discovery, T1033
  https://attack.mitre.org/techniques/T1033/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  system_owner_user_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return system_owner_user_discovery_str

def process_discovery_13D1_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 13.D.1, Process Discovery, T1057
  https://attack.mitre.org/techniques/T1057/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  process_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return process_discovery_str

def component_object_model_hijacking_14A1_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 14.A.1, Event Triggered Execution: Component Object Model Hijacking, T1546.015
  https://attack.mitre.org/techniques/T1546/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  component_object_model_hijacking_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return component_object_model_hijacking_str

def bypass_user_accounnt_control_14A2_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 14.A.2, Abuse Elevation Control Mechanism: Bypass User Access Control, T1548.002
  https://attack.mitre.org/techniques/T1548/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "1"
  event_provider = "Microsoft-Windows-Sysmon"
  bypass_user_accounnt_control_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.Image": "*sdclt.exe*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return bypass_user_accounnt_control_str

def modify_registry_14A3_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 14.A.3, Modify Registry, T1112
  https://attack.mitre.org/techniques/T1112/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  modify_registry_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ScriptBlockText": "*Remove-Item*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return modify_registry_str

def process_discovery_14B2_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 14.B.2, Process Discovery, T1057
  https://attack.mitre.org/techniques/T1057/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  process_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return process_discovery_str

def system_owner_user_discovery_15A1_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 15.A.1, System Owner/User Discovery, T1033
  https://attack.mitre.org/techniques/T1033/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  system_owner_user_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return system_owner_user_discovery_str


def remote_system_discovery_16A1_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 16.A.1, Remote System Discovery, T1018
  https://attack.mitre.org/techniques/T1018/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "3"
  event_provider = "Microsoft-Windows-Sysmon"
  remote_system_discovery_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.Image": "*powershell.exe*"
          }
        },
        {
          "match": {
            "winlog.event_data.DestinationPort": "389"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return remote_system_discovery_str

def execution_through_api_16B2_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 16.B.2, Native API, T1106
  https://attack.mitre.org/techniques/T1106/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  execution_through_api_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return execution_through_api_str

def windows_remote_management_16C1_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 16.C.1, Remote Services: Windows Remote Management, T1021.006
  https://attack.mitre.org/techniques/T1021/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "3"
  event_provider = "Microsoft-Windows-Sysmon"
  windows_remote_management_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.Image": "*powershell.exe*"
          }
        },
        {
          "match": {
            "winlog.event_data.DestinationPort": "5985"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return windows_remote_management_str


def valid_accounts_16C2_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 16.C.2, Valid Accounts, T1078
  https://attack.mitre.org/techniques/T1078/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4624"
  event_provider = "Microsoft-Windows-Security-Auditing"
  valid_accounts_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return valid_accounts_str

def email_collection_17A1_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 16.C.2, Email Collection, T1114
  https://attack.mitre.org/techniques/T1114/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "1"
  event_provider = "Microsoft-Windows-Sysmon"
  email_collection_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.Image": "*OUTLOOK*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return email_collection_str

def data_staged_17B2_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 17.B.2, Data Staged, T1074
  https://attack.mitre.org/techniques/T1074/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "11"
  event_provider = "Microsoft-Windows-Sysmon"
  data_staged_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.Image": "*powershell.exe*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }],
        "should": [{
          "wildcard": {
            "winlog.event_data.Image": "*PowerShell.exe*"
          }
        }]
      }
    }
  }
  return data_staged_str

def data_compressed_17C1_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 17.C.1, Archive Collected Data, T1560
  https://attack.mitre.org/techniques/T1560/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  data_compressed_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ScriptBlockText": "*System.IO.Compression.ZipFile*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return data_compressed_str

def web_service_18A1_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 18.A.1, Web Service, T1102
  https://attack.mitre.org/techniques/T1102/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "1"
  event_provider = "Microsoft-Windows-Sysmon"
  web_service_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.Image": "*net.exe*"
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ParentImage": "*powershell.exe*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return web_service_str

def rundll32_20A1_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 20.A.1, Signed Binary Proxy Execution: Rundll32, T1218.011
  https://attack.mitre.org/techniques/T1218/011/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "1"
  event_provider = "Microsoft-Windows-Sysmon"
  rundll32_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.Image": "*rundll32.exe*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return rundll32_str

def windows_management_instrumentation_event_subscription_20A2_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 20.A.2, Event Triggered Execution: Windows Management Instrumentation Event Subscription, T1546.003
  https://attack.mitre.org/techniques/T1546/003/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "1"
  event_provider = "Microsoft-Windows-Sysmon"
  windows_management_instrumentation_event_subscription_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.Image": "*powershell.exe*"
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ParentImage": "*WmiPrvSE*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return windows_management_instrumentation_event_subscription_str

def pass_the_ticket_20A2_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 20.A.2, Use Alternate Authentication Material: Pass the Ticket, T1550.003
  https://attack.mitre.org/techniques/T1550/003/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "4104"
  event_provider = "Microsoft-Windows-PowerShell"
  pass_the_ticket_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.ScriptBlockText": "*kerberos::golden*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return pass_the_ticket_str

def windows_remote_management_20B2_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 20.B.2, Remote Services: Windows Remote Management, T1021.006
  https://attack.mitre.org/techniques/T1021/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "3"
  event_provider = "Microsoft-Windows-Sysmon"
  windows_remote_management_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "match": {
            "winlog.event_data.DestinationPort": "5985"
          }
        },
        {
          "wildcard": {
            "winlog.event_data.Image": "*powershell.exe*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return windows_remote_management_str

def create_account_20B3_query(es_start_time, es_end_time):
  """
  APT29, Second Scenario, 20.B.3, Create Account, T1136
  https://attack.mitre.org/techniques/T1136/

  Parameters:
    - es_start_time: elasticsearch range query start time
    - es_end_time: elasticsearch range query end time

  Returns:
    The query string.
  """
  event_id = "1"
  event_provider = "Microsoft-Windows-Sysmon"
  create_account_str = {
    "query": {
      "bool": {
        "must": [{
          "match": {
            "winlog.event_id": event_id
          }
        },
        {
          "match": {
            "winlog.provider_name": event_provider
          }
        },
        {
          "wildcard": {
            "winlog.event_data.Image": "*net.exe*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": es_start_time,
              "lte": es_end_time
            }
          }
        }]
      }
    }
  }
  return create_account_str
