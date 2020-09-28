引言：本文章介紹如何透過現有開源工具，於windows平台上進行log收集，以利網管人員管理及監控。文章以WinlogBeat及sysmon兩套開源工具為主進行說明。

<font color="blue"><b> ＊＊＊以下的操作以windows 10平台為主進行示範＊＊＊ </b></font>


# 1. Winlogbeat的由來  

[Winlogbeat下載點](https://myspace.iii.org.tw/d/f/578606223698474547) 首先進行Winlogbeat的下載，因為整個操作需要做較多的設定，故可在此下載本篇文章的範例 。


簡介：Winlogbeat為ELK開源家族的其中一個工具，其功能為擷取windows上的eventlog，並透過設定winlogbeat.yml檔案，達到收集該主機的log資料，並即時輸出至logstash或是elasticsearch或是其他接收端的目的。


下載後為一zip檔案，須先用解壓縮軟體解開，可在解壓後的檔案目錄中看到winlogbeat.exe和winlogbeat.yml等相關檔案，透過在終端機介面中移動到解壓縮後的檔案目錄，然後輸入  
<font color="red"><b>  winlogbeat.exe -c -e winlogbeat.yml  </b></font>
指令，系統即開始作動。


## 1-1. Winlogbeat的輸出入設定


本文章列出三個較常受到關注的channel進行實際操演：

1. 	Security
2.	Microsoft-Windows-Sysmon%4Operational
3.	Microsoft-Windows-PowerShell%4Operational


進入Winlogbeat目錄後，首先編修winlogbeat.yml，編輯後如下 <b>（此範例收錄在上述載點中，也可以根據實際請況進行變更）</b>

	winlogbeat.event_logs:
	  - name: Security

	  - name: Microsoft-Windows-Sysmon/Operational

	  - name: Microsoft-Windows-PowerShell/Operational
	
	
	output.elasticsearch:
	
	  hosts: ["hostname:9200"]
	  index: "winlogbeat-%{+yyyyMMdd}"
	
	setup.template.name: "winlogbeat-%{+yyyyMMdd}"
	setup.template.pattern: "winlogbeat-%{+yyyyMMdd}"
	setup.ilm.enabled: false


說明：

* hosts: ["hostname:9200"]：為輸出的ES的位置

* index: "winlogbeat-%{+yyyyMMdd}"：index 的名稱，%{+yyyyMMdd}為以“日期”為變數，當成索引的產出，產出的索引名稱如“winlogbeat-20200901”

* setup.template.name: "winlogbeat-%{+yyyyMMdd}"   <font color="red">(如果不是利用預設index名稱，則需設定)</font>

* setup.template.pattern: "winlogbeat-%{+yyyyMMdd}" <font color="red">(如果不是利用預設index名稱，則需設定) </font>

* setup.ilm.enabled: false   <font color="red"> (如果不是利用預設index名稱，則需設定) </font>



## 1-2. 註冊Winlogbeat為系統服務，使其開機後可自動執行

上述1-1的操作，在我們將終端機關掉時，winlogbeat.exe就會結束。而在真實的情況中，我們會希望安裝完Winlogbeat後，其可以在背景默默的工作，此時就需要透過以下的步驟進行：

“以系統管理員身份”開啟Windows PowerShell。切換到解壓縮的Winlogbeat目錄中，確認有install-service-winlogbeat.ps1，接著在PowerShell中輸入以下指令：

1. 	<b> set-executionpolicy remotesigned </b> --> 打開PowerShell執行指令碼的權限
2.	<b> .\install-service-winlogbeat.ps1 </b> --> 將Winlogbeat註冊成“服務”，此時應可以在 “工作管理員“中的”服務“看到Winlogbeat，但是其 “狀態”預設是 “已停止”
3.	<b>在 “工作管理員“中的”服務“中，“啟動”Winlogbeat </b>

這時，差不多已經完成80%的步驟了，但是因為每次重開機後，Winlogbeat又會默默的回到 “已停止”的狀態，實在是不聰明。這時候，可以透過撰寫一個bat檔案來執行“重開機後自動啟動”的功能 。如下：

1. 	開啟文字編輯器，裡面的內容只需一行  <font color="red"><b> sc start winlogbeat </b></font>
2.	將此檔案儲存成 Winlogbeat.bat (這邊要注意，不要存成.txt 或是其他副檔名)
3.	將上述的檔案<font color="red"><b>放置windows的啟動目錄</b></font>中，即完成


<font color="red"><b>＊＊＊Winlogbeat.bat已經置於上述載點中 ＊＊＊</b></font>

這邊要注意：因為windows的版本差異，路徑和系統程式也不盡相同。本文範例啟動目錄如下：


	Win10:  C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

	



# 2. Sysmon安裝 

[Sysmon下載點](https://myspace.iii.org.tw/d/f/578608233711713089)


簡介：Sysmon.exe是一個Microsoft提供的log紀錄工具，其功能為根據”規則”生成windows上的log。此工具可於官網下載，下載後為一個zip檔，於解壓縮後會看到Sysmon.exe，Sysmon64.exe兩隻程式，接著利用terminal(以系統管理員身分執行)執行如下指令：

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

