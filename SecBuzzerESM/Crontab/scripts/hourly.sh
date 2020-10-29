#/bin/bash

# Call the Winlog AI module
WinlogIndex=winlogbeat-`date "+%Y%m%d"`
hourtime=`date -d "-1 hour" +"%Y-%m-%dT%H"`
winlog_hourtime=`date -d "-9 hour" +"%Y-%m-%dT%H"`
curl -i "http://winlog:5000/winlog/api/v1.0?index=$WinlogIndex&start_time="$winlog_hourtime":00:00&end_time="$winlog_hourtime":59:59"
echo "[*] `date +"%Y-%m-%d %H:%M"` Exec Winlog AI module"

# Call the ETA AI module
CIC_Index=cic_`date "+%Y%m%d"`
curl -i "http://eta_attack:5000/eta_attack/api/v1.0?index=$CIC_Index&start_time="$hourtime":00:00.000000%2B08:00&end_time="$hourtime":59:59.999999%2B08:00"
echo "[*] `date +"%Y-%m-%d %H:%M"` Exec ETA_Attack AI module"
curl -i "http://eta_malware:5000/eta_malware/api/pred?index=$CIC_Index&start_time="$hourtime":00:00.000000%2B08:00&end_time="$hourtime":59:59.999999%2B08:00"
echo "[*] `date +"%Y-%m-%d %H:%M"` Exec ETA_Malware AI module"
