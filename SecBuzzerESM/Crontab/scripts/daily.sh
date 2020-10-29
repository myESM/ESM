#/bin/bash

# Auto remove eve-yyyy-mm-dd.json
rm /suricata_log/eve-`date -d "-7 days" "+%Y-%m-%d"`.json 2>/dev/null
echo "[*] remove eve-`date -d "-7 days" "+%Y-%m-%d"`.json"

# Auto remove ES index
eta_remove_date="$(date -d '-3 month' +%Y-%m)"
curl -X DELETE "elasticsearch:9200/eta-attack-$eta_remove_date"
curl -X DELETE "elasticsearch:9200/eta-malware-$eta_remove_date"

winlog_remove_date="$(date -d '-3 month' +%Y-%m)"
curl -X DELETE "elasticsearch:9200/winlog-$winlog_remove_date"

suricata_remove_date="$(date -d '-6 month' +%Y-%m)"
curl -X DELETE "elasticsearch:9200/suricata-$suricata_remove_date"

cic_remove_date="$(date -d '-7 days' +%Y%m%d)"
curl -X DELETE "elasticsearch:9200/cic-$cic_remove_date"

winlogbeat_remove_date="$(date -d '-7 days' +%Y%m%d)"
curl -X DELETE "elasticsearch:9200/winlogbeat-$winlogbeat_remove_date"
echo "[*] Daily check and remove index"

