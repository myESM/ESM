引言：本文章介紹如何透過現有開源工具，於windows平台上進行log收集的動作以利網管人員管理及監控。文章以WinlogBeat及sysmon兩套開源工具為主進行說明。

# 1. Winlogbeat的設定  
[Winlogbeat下載點](https://www.elastic.co/downloads/beats/winlogbeat)

簡介：Winlogbeat為ELK開源家族的其中一個工具，其功能為擷取windows上的eventlog，並透過設定winlogbeat.yml檔案，達到將log資料即時輸出至logstash或是elasticsearch或是其他接收端的目的。在設定winlogbeat.yml時，可以根據需求，選擇隨意地一個具有evtx的路徑當成Winlogbeat.exe的輸入，也可以以windows預設的路徑(C:\Windows\System32\winevt)進行即時的監控。本文章介紹以較常受到關注的三個channel為主進行實際操演．列出如下：

1. 	Microsoft-Windows-Sysmon%4Operational
2.	Microsoft-Windows-PowerShell%4Operational
3.	Security



## 1-1. 即時監控evtx的channel

進入Winlogbeat目錄後，首先編修winlogbeat.yml，編輯後如下

	winlogbeat.event_logs:
	  - name: Security
	    processors:
	      - script:
	          lang: javascript
	          id: security
	          file: ${path.home}/module/security/config/winlogbeat-security.js
	
	  - name: Microsoft-Windows-Sysmon/Operational
	    processors:
	      - script:
	          lang: javascript
	          id: sysmon
	          file: ${path.home}/module/sysmon/config/winlogbeat-sysmon.js
	
	  - name: Microsoft-Windows-PowerShell/Operational
	
	winlogbeat.shutdown_timeout: 30s 
	winlogbeat.registry_file: evtx-registry.yml 
	
	output.elasticsearch.hosts: ['http://localhost:9200']

說明：
output.elasticsearch.hosts: ['http://localhost:9200']：'http://localhost:9200' 為輸出的es的位置 （本文的輸出以es為主，可於官網中進行下載）[es官方載點](https://www.elastic.co/downloads/elasticsearch)

winlogbeat.yml 中的name：可以利用windows內附的”事件檢視器”取得想要監聽的channel，此”全名”就會對應到yml中的name。例如要取得 Security，那可以如下圖操作，其他的channel取得也是一樣的方式。

接著即可以至 es head 觀察資料是否已經正確輸入 

[官網參考資料連結](https://www.elastic.co/guide/en/beats/winlogbeat/current/reading-from-evtx.html)

### <font color="red">事件檢視器操作示意圖</font>
![](https://github.com/shwang362000/ESM/blob/master/Document/ESM_Install/images/%E4%BA%8B%E4%BB%B6%E6%AA%A2%E8%A6%96%E5%99%A8%E6%93%8D%E4%BD%9C%E7%A4%BA%E6%84%8F%E5%9C%96.png)


## 1-2. ectx輸出到指定的es index
小編於本次演練中，因為需要將多台主機的evtx log打到不同的es index中，參考了官方的文件，始終無法順利解決，後來發現必須在winlogbeat.yaml 做細部的設定，即可以達到該功能，將winlogbeat.yaml 分享如下：

	winlogbeat.event_logs:
	  - name: ${EVTX_FILE} 
	    no_more_events: stop 
	
	winlogbeat.shutdown_timeout: 30s 
	winlogbeat.registry_file: evtx-registry.yml 
	
	output.elasticsearch:
	
	  hosts: ["hostname:9200"]
	  index: "winlogbeat-%{+yyyyMMdd}"
	
	setup.template.name: "winlogbeat-%{+yyyyMMdd}"
	setup.template.pattern: "winlogbeat-%{+yyyyMMdd}"
	setup.ilm.enabled: false

說明：

* index: "winlogbeat-%{+yyyyMMdd}"：index 的名稱，%{+yyyyMMdd}為以“日期”為變數，當成索引的產出，產出的索引名稱如“winlogbeat-20200901”

* setup.template.name: "winlogbeat-%{+yyyyMMdd}" <font color="red">如果不是利用預設名稱，則強迫要設定這個項目</font>

* setup.template.pattern: "winlogbeat-%{+yyyyMMdd}" <font color="red">如果不是利用預設名稱，則強迫要設定這個項目</font>

* setup.ilm.enabled: false  <font color="red">如果不是利用預設名稱，則強迫要設定這個項目</font>
	
# 2. Sysmon安裝 

[Sysmon程式下載點](https://download.sysinternals.com/files/Sysmon.zip)

[Sysmon規則下載點](https://github.com/SwiftOnSecurity/sysmon-config)

簡介：Sysmon.exe是一個Microsoft提供的log紀錄工具，其功能為根據”規則”生成windows上的log。此工具可於官網下載，下載後為一個zip檔，於解壓縮後會看到Sysmon.exe，Sysmon64.exe兩隻程式。

接著下載sysmon規則，並將此規則 “sysmonconfig-export.xml” 與 Sysmon64.exe放置於同一資料夾下，接著利用terminal(以系統管理員身分執行)執行如下指令：

sysmon64 -i sysmonconfig-export.xml 

如果順利，按下Ctrl+Alt+Del 應該可以在“工作管理員”內看到如下畫面，如此即代表安裝完成並已經啟動該服務（僅需安裝一次，重開機後該服務會自動啟動免煩惱）。

[官網參考資料連結](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)



### <font color="red">檢查sysmon執行成功示意圖</font>
![](https://github.com/shwang362000/ESM/blob/master/Document/ESM_Install/images/%E6%AA%A2%E6%9F%A5sysmon%E5%9F%B7%E8%A1%8C%E6%88%90%E5%8A%9F%E7%A4%BA%E6%84%8F%E5%9C%96.png
)




# 3. 其他細部設定

本次演練中有一個channel為監聽PowerShell所產出的相關軌跡，故可以做一些進階設定，如下所述。於 Windows中執行”本機群組原則編輯器”，開啟後做如下的設定。


### <font color="red">群組原則編輯器操作示意圖</font>
![](https://github.com/shwang362000/ESM/blob/master/Document/ESM_Install/images/%E7%BE%A4%E7%B5%84%E5%8E%9F%E5%89%87%E7%B7%A8%E8%BC%AF%E5%99%A8%E6%93%8D%E4%BD%9C%E7%A4%BA%E6%84%8F%E5%9C%96.png)


## 3-1. 確認設定是否成功 

經過一連串的設定，最後總是要確認以上的設定都正確無誤，且該被監聽的動作已經被如實紀錄，可以利用以下方式來做檢查。開啟PowerShell，隨意輸入指令，如” Get-ChildItem”，接著進入事件檢視器，看看是否有正確紀錄輸入軌跡紀錄。檢視方式如下圖紅框，開啟”事件內容”即可做細部確認。

### <font color="red">確認設定正確操作示意圖</font>
![](https://github.com/shwang362000/ESM/blob/master/Document/ESM_Install/images/%E7%A2%BA%E8%AA%8D%E8%A8%AD%E5%AE%9A%E6%AD%A3%E7%A2%BA%E6%93%8D%E4%BD%9C%E7%A4%BA%E6%84%8F%E5%9C%96.png)

