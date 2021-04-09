#/bin/bash

# Auto remove eve-yyyy-mm-dd.json
rm /suricata_log/eve-`date -d "-7 days" "+%Y-%m-%d"`.json 2>/dev/null
echo "[*] remove eve-`date -d "-7 days" "+%Y-%m-%d"`.json"

# Auto remove ES index
eta_remove_date="$(date -d '-3 month' +%Y-%m)"
# curl -X DELETE "elasticsearch:9200/eta-attack-$eta_remove_date"
curl -X DELETE "elasticsearch:9200/eta-malware-$eta_remove_date"

winlog_remove_date="$(date -d '-3 month' +%Y-%m)"
curl -X DELETE "elasticsearch:9200/winlog-$winlog_remove_date"

suricata_remove_date="$(date -d '-6 month' +%Y-%m)"
curl -X DELETE "elasticsearch:9200/suricata-$suricata_remove_date"

cic_remove_date="$(date -d '-7 days' +%Y%m%d)"
curl -X DELETE "elasticsearch:9200/cic-$cic_remove_date"

winlogbeat_remove_date="$(date -d '-7 days' +%Y%m%d)"
curl -X DELETE "elasticsearch:9200/winlogbeat-$winlogbeat_remove_date"

packetbeat_remove_date="$(date -d '-7 days' +%Y.%m.%d)"
curl -X DELETE "elasticsearch:9200/packetbeat-$packetbeat_remove_date"

flowscan_remove_date="$(date -d '-6 month' +%Y-%m)"
curl -X DELETE "elasticsearch:9200/flowscan-$flowscan_remove_date"

nmapscan_remove_date="$(date -d '-6 month' +%Y-%m)"
curl -X DELETE "elasticsearch:9200/nmap-$nmapscan_remove_date"
echo "[*] Daily check and remove index"

lm_remove_date="$(date -d '-184 day' +%Y-%m-%d)"
curl -X DELETE "elasticsearch:9200/lm-$lm_remove_date"

find /Logs/ -type f -ctime +3 | xargs tar zcvf `date +'%Y-%m-%d'`.tgz --remove-files
find /Logs/ -type d -empty -delete
mv `date +'%Y-%m-%d'`.tgz /LogsCompress

chgrp 1000 /LogsCompress/*
chown 1000 /LogsCompress/*

#rm -f /LogsCompress/`date +'%Y-%m-%d' -d '-397 days'`.tgz

echo [*] `date +'%Y-%m-%d'` exec RAW log compress >> /var/log/cron.log
#echo [*] `date +'%Y-%m-%d'` Delete `date +'%Y-%m-%d' -d '-397 days'`.tgz  >> /var/log/cron.loga