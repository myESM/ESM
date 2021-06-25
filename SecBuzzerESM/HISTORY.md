# Release History
# V2.3.4 (2021-06-25)
- 再次更新 winlog模組的es query資料量上限

# V2.3.3 (2021-06-24)
- 更新 winlog模組的es query資料量上限

# V2.3.2 (2021-06-21)
- 更新文件: Winlogbeat設定SSL和CA.md

# V2.3.1 (2021-06-15)
- 移除compose.sh內的AI模組註解
- 新增文件: SecBuzzerESM 連線安裝手冊.md

# V2.3.0 (2021-06-05)
- 修復 servicecheck.py 無法讀取環境變數
- 修正 servicecheck 執行的時間

# V2.2.0 (2021-05-31)
- 修復 Cronjob 不執行問題

# V2.1.1 (2021-05-31)
- 修復 suricata_checker 不執行問題
- 重寫 servicecheck.py
- 修復 CI 版本錯亂
# V2.0.7 (2021-05-27)
- 調整 Crontab 運行 Ｗinlogbeat AI 模組讀取 Index 名稱

# V2.0.6 (2021-05-12)
- EsmEdgeApp.jar的ES連線訊息更新

# V2.0.5 (2021-05-03)
- 更新資產盤點版本 v1.0.3
# V2.0.4 (2021-04-21)
- EsmEdgeApp.jar的ES client連線版本升級到7.6.0

# V2.0.3 (2021-04-19)
- 更新 AI module

# V2.0.2 (2021-04-06)
- 關閉 Suricata_dumper Service

# V2.0.1 (2021-03-25)
- EsmEdgeApp.jar整合資產盤點 (nmap & flowscan)

# V2.0.0 (2021-03-24)
- 整合資產盤點 (nmap & flowscan)
- 更新 ETA-Malware

# V1.7.0 (2021-03-19)
- 新增資產盤點

# V1.6.0 (2021-03-18)
- 使用 tini 優化 Container 關閉速度
- 新增 vnstat Service 
- Container 重啟策略改為 unless-stopped
- 修正 Upgrade_ESM.py 大版本更新時 .env 消失

# V1.5.8 (2021-03-10)
- EsmEdgeApp.jar重新上傳
- EsmEdgeApp.jar update ES attribute client.transport.sniff to be true

# V1.5.7 (2021-03-09)
- 設定 FluentD Tail read_from_head 參數為 True

# V1.5.6 (2021-03-02)
- Fluentd 停用 Syslog 與 CEF Log Parser 功能
- fluent.conf 移除多餘 x 字元

# V1.5.5 (2021-02-26)
- 修改 compose.sh, 不啟動 AI 模組
- 調整 prepare.sh, 避免新版 Docker 無法壓縮離線安裝包 (已測試在 Docker 20.10.3)

# V1.5.4 (2021-02-25)
- Fluentd 啟用 Syslog 與 CEF Log Parser 功能
- 新增 ES Template 指定 lm index timestamp 欄位為 text 格式
- 新增自動刪除半年前 lm index
- 新增壓縮 Syslog 與 CEF Log Raw Log 功能
- 調整 Crontab 與 FluentD 啟動優先順序

# V1.5.3 (2021-01-28)
- 修改 Suricata 啟動方式, 解決啟動失敗問題
- 安裝腳本中新增關閉 swap 
- 安裝腳本中新增 UDP 優化設定檔

# V1.5.2 (2021-01-13)
- 關閉 ETA-Attack AI Module
- 新增 vnstat 安裝包, 在 Tools 目錄下

# V1.5.1 (2021-01-06)
- :tada: Happy New Year! :tada:
- 修正 Packet_Reporter 傳送重複資料

# V1.5.0 (2020-12-18)
- 優化線上安裝&離線安裝腳本
- 修正更新腳本無法重新安裝
- 修正 Packetbeat 輸出資料錯字

# V1.4.3 (2020-12-11)
- 修正部分服務回傳的 org_code 大小寫不同

# V1.4.2 (2020-12-09)
- 修正線上 & 離線安裝時重複執行會安裝失敗

# V1.4.1 (2020-12-07)
- 更新 ES Head 的版本
- 修正離線安裝失敗的問題
- 更新 workflow

# V1.4.0 (2020-12-03)
- 修正 packet_reporter 因各式回傳失敗
- 修正 packet_reporter 噴錯後無法重啟

# V1.3.4 (2020-12-02)
- 更新 EsmEdgeApp.jar update ES attribute client.transport.sniff to be true

# V1.3.3 (2020-12-02)
- 調整 workflow

# V1.3.2 (2020-12-02)
- 調整 Suricata_Stats_Dumper 回傳時間為 15 分鐘

# V1.3.1 (2020-12-02)
- 更新 ETA-Malware

# V1.3.0 (2020-12-01)
- 重構 Suricata_Stats_Dumper, 修正重啟統計問題
- 更新 CICFlowMeter.jar 修正 Log 不移除問題
- 修改 Suricata 輸出 Stats 時間為 30 秒

# V1.2.1 (2020-11-23)
- 更新 EsmEdgeApp.jar 初始時印出環境變數DEV_MODE的內容

# V1.2.0 (2020-11-23)
- 修正 Install.sh 腳本失敗
- 修正 Install.sh 安裝 Docker 邏輯
- 修正 Crontab container 執行時間錯誤
- 更新 ETA Malware 程式

# V1.1.4 (2020-11-18)
- 修正 EdgeApp 掛載及環境變數未設定問題

# V1.1.3 (2020-11-17)
- 更新 EsmEdgeApp.jar 自動判斷是否為 Production
- 新增 EsmEdgeApp.jar 上傳 ESM Edge 版本號

# V1.1.2 (2020-11-13)
- 調整 workflows

# V1.1.1 (2020-11-13)
- 新增 .version 檔案

# V1.1.0 (2020-11-11)
- 更新 Suricata 6.0.0
- 更新 ETA & Winlog AI module
- 新增 DEV_Mode 環境變數
- 調整部分 Docker-compose.yml 設定, 新增預設值

# V1.0.0 (2020-11-2)
- 新增 Packetbeat & Packet_reporter
- Cron 自動移除 Packetbeat Index
- 修正 ETA 模組觸發的 Index
- 調整 diskcheck.py、es_setter.py 輸出 Log 會顯示 Service name
- 重構 es_setter 架構
- Upgrade_ESM 新增防呆、檢查機制判斷更新失敗
- 調整 Install.sh、Offlin_Intall.sh 使 exit code 正常輸出

# V0.8.2 (2020-11-05)
- Fix RabbitMQ傳輸的中文資訊不為亂碼

# V0.8.1 (2020-10-29)
- Fix ETA path

# V0.8.0 (2020-10-28)
- 修正無移除 winlogbeat Index 
- 修正 Cron 執行腳本沒輸出 Log
- 修正 Suricata_Checker 誤判問題
- 新增 packetbeat
- 新增 ES pipline for packetbeat
- 新增每月移除 Sricata_checker Logs

# V0.7.3 (2020-10-26)
- 更新 ETA Training

# V0.7.2 (2020-10-26)
- 更新 PacketAnalyze jar 檔

# V0.7.1 (2020-10-26)
- 新增 Suricata_stats_dumper
- 獨立 Suricata_Checker (tcpreplay) & 優化 Image 大小
- 移除舊版 Suricata_checker
- 新增輸出 suricata stats.log 到 /opt/Logs/Suricata/stats.log
- Crontab 新增每週移除 stats.log

# V0.7.0 (2020-10-14)
- 調整清除 Cron Log 時間為每月一次
- 新增 Suricata Checker
- 優化 Crontab container 大小

# V0.6.1 (2020-10-15)
- fluen.conf 新增 pipeline 設置

# V0.6.0 (2020-10-13)
- 新增每日測試 Suricata rule
- 修正 Daily.sh 無法移除 malware & winlog

# V0.5.9 (2020-09-28)
- 更新 PacketAnalyze jar 檔
- 修正 PacketAnalyze log4j 噴錯
- 修正呼叫 winlog 沒帶時區
- 修正呼叫 ETA API 的參數錯誤
- 移除 FluentdCron
- 暫時移除 Fluentd 收 Log 功能

# V0.5.8 (2020-09-28)
- 修正 prepare.sh 噴錯
- 修正 winlogbeat index 不移除問題

# V0.5.7 (2020-09-22)
- 修正 winlog 模組呼叫失敗
- 優化 prepare.sh 路徑問題

# V0.5.6 (2020-09-17)
- 修正EsmEdgeApp.jar內runCheckDataForDay的重送資料

# V0.5.5 (2020-09-16)
- 修正使用 Upgrade_ESM.py 時同版本時跳出錯誤
- 優化 Upgrade_ESM.py 邏輯, 更新失敗時不會蓋掉版本號
- 優化 Docker 更新過程, 清除環境變數帶來的 WARNING
- 優化 Install.sh, 清除環境變數帶來的 WARNING

# V0.5.4 (2020-09-15)
- 修正 Upgrade_ESM.py 預設的讀取路徑

# V0.5.3 (2020-09-15)
- 更新WEB/docker-compose.yml
- 指定時區為台北時間

# V0.5.2 (2020-09-11)
- 更新EsmEdgeApp.jar

# V0.5.1 (2020-09-11)
- 修正 Upgrade_ESM.py 版本判斷
- 增加對版本的防呆機制、若無法讀取版本則提示完整更新

# V0.5.0 (2020-09-10)
- 重新調整 ETA 在 EMS 的架構 (ETA ATTACK、MALWARE 放在 ETA 目錄且共用 Image)
- 重寫 Dockerfile (移除 ADD、pip install requirement)
- 修正新版 Dockerfile 在 ETA 中路徑壞掉 error
- 重新調整套件版本, 加快 Build 時間 (原本需要20-40分鐘)

# V0.4.0 (2020-09-08)
- 新增 Upgrade_ESM.py
- 修改為讀取線上更新的 classification
- 更新 ETA-Attack 並啟用
- 更新 PacketAnalyze
- Install.sh & Update_Suricata_rules.sh 加上 API Key 防呆, 避免噴錯

# V0.3.22 (2020-08-28)
- 修正 Suricata Updater 無法輸出 Log

# V0.3.21 (2020-08-27)
- 調整 Dickcheck.py 邏輯
- 新增每日自動檢查並移除 es index
- 調整 SuricataUpdater 輸出 log
- 新增每日自動移除 Cron 產生的 Log

# V0.3.20 (2020-08-27)
- 修改 SuricataUpdater API
- 修改 Update_Suricata_rules API
- 修改 Install.sh 更新 Rules API

# V0.3.19 (2020-08-26)
- 修正 SuricataUpdater 無法下載 Rule 時重試失敗

# V0.3.18 (2020-08-25)
- 修正 SuricataUpdater 套件沒引用導致的錯誤

# V0.3.17 (2020-08-21)
- 更新 Suricata updater, 輸出更詳細的內容!
- 更新 Suricata updater, 增加隨機 Sleep

# V0.3.16 (2020-08-21)
- 換上 python 版本的 Suricata updater
- 修改 fluentd syslog host 欄位名稱為 hostname 

# V0.3.15 (2020-08-20)
- 更新 classification.config (新增快篩規則中定義的類別)

# V0.3.14 (2020-08-20)
- 補上缺少的 classification.config

# V0.3.13 (2020-08-20)
- 掛載 Suricata classification、iprep

# V0.3.12 (2020-08-19)
- 修改 es replica, 解決 ES 不健康

# V0.3.11
- 更新ESM的「連線」與「離線」安裝文件

# V0.3.10
- Update_Suricata_rules.sh 修改為使用 env 內的 key
- 更新 Winlog AI module 版本

# V0.3.9
- 隱藏重複創建 docker network 噴出的 error

# V0.3.8
- 修正 Suricata 無法送資料到ES

## V0.3.7
- cron 補上 pipe line 
- 移除 ES ILM相關設定

## V0.3.6
- 移除 ETA1 AI module
- 將 Suricata 規則更新改為每十分鐘觸發

## V0.3.5
- 將 AI 模組 PacketAnalyze 恢復
- 將 AI 模組 Winlog 恢復
- 將 AI 模組 ETA1 恢復
- Install.sh 加上更新規則

## V0.3.4
- Suricata 同步更新 rules

## V0.3.4
- 增加 Suricata Updater 延時

## V0.3.3
- ES 改為 OSS 版
- ES 改為單節點
- 暫時移除 AI 模組

## V0.3.2
- :tada: repush to Github :sparkler:

## V0.3.1
- 修正 Suricata updater 無法更新

## V0.3.0
- 新增 esm network
- 新增 ETA1 AI module
- 新增自動更新 suricata rules

## V0.2.24
- 修改 CEF Log Parser 處理欄位內容夾帶 "|" 符號狀況

## V0.2.23
- 更新 Update_Suricata_rulues.sh 
- 調整 suricata.yml 為讀取所有 rule

## V0.2.22
- 修正 AI docker-compose 格式錯誤

## V0.2.21
- 將 Winlog 觸發時間改為一小時一次
- 關閉 OMP module 
- 關閉 AI 用 mysql & 管理工具
- 增加 compose.sh 啟動 AI module

## V0.2.20
- 新增 Winlog 模組
- 新增 Cronjob 定時觸發 Winlog 模組
- 新增自動移除 eve.json

## V0.2.19
- 新增 PacketAnalyze 模組

## V0.2.18
- 新增 Suricata 資料打入 ES 時間欄位

## V0.2.17
- 修正suricata.yaml檔 - eve檔案輸出格式錯誤

## V0.2.16
- 調整 Update_Suricata_rules.sh 檔案路徑

## V0.2.15
- Suricata 資料新增 ticket 欄位

## V0.2.14
- 修正 Suricata rules 檔重複 sid

## V0.2.13
- 修正 Update_Suricata_rules.sh 檔案路徑

## V0.2.12
- Suricata 資料新增 dump_status 欄位

## V0.2.11
- 上傳初版 Suricata 更新腳本

## V0.2.10
- 修改 eve.json rotate 的區間
 
## V0.2.9
- 修正 Suricata 讀取不到網卡

## V0.2.8
- 修正 Fluentd 沒將規則送到 ES
- 修正 Cron 腳本不會自動重啟

## V0.2.7
- 新增離線安裝腳本 & 打包腳本

## V0.2.6
- 修正 Top Suricata Rules 因檔案名稱相同覆蓋狀況

## V0.2.5
- 修改 Suricata 設定檔, 避免 Windows 無法存取 Log
- 將 Suricata Image 上傳到 Docker hub

## V0.2.4
- 將 MiniSOC 改為 SecBuzzerESM

## V0.2.3
- 修改 Suricata docker-compose.yml, 修正 Build 後讀不到網卡

## V0.2.2
- 更新 Top Suricata Rules (20200721)

## V0.2.1
- 將 WEB 需要的 API KEY 加入到 MiniSOC.env
- 移除 POC 用不到的檔案 (Fluentd cron 備份 raw log)
- 
## V0.2.0
- 調整 sucicata, 不會輸出 fast.log, suricata.log
- 移除 POC 用不到的檔案

## V0.1.0
- Init, Base on MiniSOC 1.0.8
- Install.sh 腳本加上防呆
- 移除 Fluentd raw log 輸出
- 移除 prepare.sh & 舊版 install.sh
- 將 WEB 服務讀取的網卡加MiniSOC.env
