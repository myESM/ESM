引言：本文章介紹如何透過現有開源工具，於windows平台上進行log收集，以利網管人員管理及監控。文章以WinlogBeat及sysmon兩套開源工具為主進行說明。
Introduction: This article introduces how to use existing open source tools to collect logs on the windows platform to facilitate the management and monitoring of network. The article focuses on two open source tools, WinlogBeat and sysmon.

<font color="blue"><b> ＊＊＊以下的操作以windows 10平台為主進行示範 The following operations are based on the windows 10 platform for demonstration＊＊＊ </b></font>


# 1. Winlogbeat的由來  The origin of Winlogbeat

[Winlogbeat下載點 Winlogbeat Download](https://myspace.iii.org.tw/d/f/578606223698474547) 首先進行Winlogbeat的下載，因為整個操作需要做較多的設定，故可在此下載本篇文章的範例 。
First, download Winlogbeat. Because the entire operation requires more settings, so you can download the example of this article here.


簡介：Winlogbeat為ELK開源家族的其中一個工具，其功能為擷取windows上的eventlog，並透過設定winlogbeat.yml檔案，達到收集該主機的log資料，並即時輸出至logstash或是elasticsearch或是其他接收端的目的。
Introduction: Winlogbeat is one of the tools in the ELK open source family. Its function is to retrieve eventlog on windows, and by setting the winlogbeat.yml file, it can collect the log data of the host and output it to logstash or elasticsearch or other receivers in real time. 


下載後為一zip檔案，須先用解壓縮軟體解開，可在解壓後的檔案目錄中看到winlogbeat.exe和winlogbeat.yml等相關檔案，透過在終端機介面中移動到解壓縮後的檔案目錄，然後輸入  
<font color="red"><b>  .\winlogbeat.exe -e -c winlogbeat.yml  </b></font>
指令，系統即開始作動。
After downloading, it is a zip file, which must be unzipped with decompression software first. You can see winlogbeat.exe and winlogbeat.yml in the unzipped file directory, and move to the unzipped file in the terminal interface Directory and enter
<font color="red"><b> .\winlogbeat.exe -e -c winlogbeat.yml </b></font>
Command, and the system will start to execute.


## 1-1. Winlogbeat的輸出入設定 The Setting of  Winlogbeat's input and output 


本文章列出三個較常受到關注的channel進行實際操演：
This article lists three channels which have received more attention for actual performance:

1. 	Security
2.	Microsoft-Windows-Sysmon%4Operational
3.	Microsoft-Windows-PowerShell%4Operational


進入Winlogbeat目錄後，首先編修winlogbeat.yml，編輯後如下 After entering the Winlogbeat directory, first, edit winlogbeat.yml, and edit it as follows  <b>（此範例收錄在上述載點中，也可以根據實際請況進行變更 This example is included in the above loading point, and it can also be changed according to actual conditions.）</b>

	winlogbeat.registry_file: evtx-registry.yml 

	winlogbeat.event_logs:
	  - name: Security
    	ignore_older: 168h
	  - name: Microsoft-Windows-Sysmon/Operational
    	ignore_older: 168h
	  - name: Microsoft-Windows-PowerShell/Operational
    	ignore_older: 168h


	output.elasticsearch:
	
	  hosts: ["hostname:9200"]
	  index: "winlogbeat-%{+yyyyMMdd}"
	
	setup.template.name: "winlogbeat-%{+yyyyMMdd}"
	setup.template.pattern: "winlogbeat-%{+yyyyMMdd}"
	setup.ilm.enabled: false

	processors:
	  - add_locale: ~


說明 Description：

* winlogbeat.registry_file：紀錄傳送成功的channel的索引位置 The index position of the channel that records the successful transmission.

* ignore_older：僅傳送多少時間內的資料 The data that sent in the specific period. 

* hosts: ["hostname:9200"]：為輸出的ES的位置 The location of the ES output 

* index: "winlogbeat-%{+yyyyMMdd}"：index 的名稱，%{+yyyyMMdd}為以“日期”為變數，當成索引的產出，產出的索引名稱如“winlogbeat-20200901”
The name of the index, %{+yyyyMMdd} is the output of the index with "date" as the variable, and the index name of the output is such as "winlogbeat-20200901."

* setup.template.name: "winlogbeat-%{+yyyyMMdd}"   <font color="red">(如果不是利用預設index名稱，則需設定 If you are not using the default index name, you need to set up one)</font>

* setup.template.pattern: "winlogbeat-%{+yyyyMMdd}" <font color="red">(如果不是利用預設index名稱，則需設定 If you are not using the default index name, you need to set up one) </font>

* setup.ilm.enabled: false   <font color="red"> (如果不是利用預設index名稱，則需設定 If you are not using the default index name, you need to set up one) </font>

* add_locale: 增加時區的設定
 Increase the time zone setting

## 1-2. 註冊Winlogbeat為系統服務，使其開機後可自動執行 Register Winlogbeat as a system service so that it can be executed automatically after booting

上述1-1的操作，在我們將終端機關掉時，winlogbeat.exe就會結束。而在真實的情況中，我們會希望安裝完Winlogbeat後，其可以在背景默默的工作，此時就需要透過以下的步驟進行：
The above 1-1 operation, when we shut down the terminal, winlogbeat.exe will be turned off. In a real case, we hope that after Winlogbeat is installed, it can work silently in the background. At this time, we need to go through the following steps:

“以系統管理員身份”開啟Windows PowerShell。切換到解壓縮的Winlogbeat目錄中，確認有install-service-winlogbeat.ps1，接著在PowerShell中輸入以下指令：
Open Windows PowerShell" as a system administrator". Switch to the unzipped Winlogbeat directory, confirm that there is install-service-winlogbeat.ps1, and then enter the following command in PowerShell:


1. 	<b> set-executionpolicy remotesigned </b> --> 打開PowerShell執行指令碼的權限 Open PowerShell to execute script permissions
2.	<b> .\install-service-winlogbeat.ps1 </b> --> 將Winlogbeat註冊成“服務”，此時應可以在 “工作管理員“中的”服務“看到Winlogbeat，但是其 “狀態”預設是 “已停止” Register Winlogbeat as a "service". At the same time, you will be able to see Winlogbeat in "Services" in "工作管理員Work Manager", but its "Status" is preset to "Stopped"
3.	<b>在 “工作管理員“中的”服務“中，“啟動”Winlogbeat 
Execute Winlogbeat in "Service", "工作管理員Work Manager" </b>

這時，差不多已經完成80%的步驟了，但是因為每次重開機後，Winlogbeat又會默默的回到 “已停止”的狀態，實在是不聰明。這時候，可以透過撰寫一個bat檔案來執行“重開機後自動啟動”的功能 。如下：
Almost 80% of the steps have been completed. But Winlogbeat will return to the "stopped" status after each reboot so we suggest that you can execute the "automatically start after reboot" function by writing a bat file as follows:

1. 	開啟文字編輯器，裡面的內容只需一行  <font color="red"><b> sc start winlogbeat </b></font> 
Start the text editor, and we only need to type<font color="red"><b> "sc start winlogbeat" </b></font>
2.	將此檔案儲存成 Winlogbeat.bat (這邊要注意，不要存成.txt 或是其他副檔名)
Save this file as Winlogbeat.bat (please do not save it as .txt or other extension)
3.	將上述的檔案<font color="red"><b>放置windows的啟動目錄</b></font>中，即完成
Place the above file <font color="red"><b>in the Windows startup directory</b></font>, and it’s done.


<font color="red"><b>＊＊＊Winlogbeat.bat已經置於上述載點中 Winlogbeat.bat has been placed in the above loading point ＊＊＊</b></font>

這邊要注意：因為windows的版本差異，路徑和系統程式也不盡相同。本文範例啟動目錄如下：
Note: Because of the different versions of windows, the paths and system programs are also different. The sample startup directory of this article is as follows:


	Win10:  C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

	



# 2. Sysmon安裝 Installation of  Sysmon

[Sysmon下載點 Download](https://myspace.iii.org.tw/d/f/578608233711713089)


簡介：Sysmon.exe是一個Microsoft提供的log紀錄工具，其功能為根據”規則”生成windows上的log。此工具可於官網下載，下載後為一個zip檔，於解壓縮後會看到Sysmon.exe，Sysmon64.exe兩隻程式，接著利用terminal(以系統管理員身分執行)執行如下指令：
Introduction: Sysmon.exe is a log recording tool provided by Microsoft. Its function is to generate logs on windows according to "rules". This tool can be downloaded from the official website. After downloading, it will be a zip file. After decompression, you will see two programs, Sysmon.exe and Sysmon64.exe. Then use the terminal (run as a system administrator) to execute the following commands:

sysmon64 -i sysmonconfig-export.xml 

如果順利，按下Ctrl+Alt+Del 應該可以在“工作管理員”內看到如下畫面，如此即代表安裝完成並已經啟動該服務（僅需安裝一次，重開機後該服務會自動啟動免煩惱）。
If it goes well, press Ctrl+Alt+Del and you should be able to see the following screen in the "工作管理員work manager", which means that the installation is complete and the service has been started (only need to install once, the service will automatically start after restarting. ).

[官網參考資料連結](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)



### <font color="red">檢查sysmon執行成功示意圖 Check the schematic diagram of sysmon execution success</font>
![](https://github.com/shwang362000/ESM/blob/master/Document/ESM_Install/images/%E6%AA%A2%E6%9F%A5sysmon%E5%9F%B7%E8%A1%8C%E6%88%90%E5%8A%9F%E7%A4%BA%E6%84%8F%E5%9C%96.png
)




# 3. 其他細部設定 Other Settings

本次演練中有一個channel為監聽PowerShell所產出的相關軌跡，故可以做一些進階設定，如下所述。於 Windows中執行”本機群組原則編輯器”，開啟後做如下的設定。
In this exercise, there is a channel to monitor the relevant traces produced by PowerShell, so some advanced settings can be made, as described below. Run "本機群組原則編輯器 Local Group Policy Editor" in Windows, activate it and implement the following settings.


### <font color="red">群組原則編輯器操作示意圖 Schematic diagram of group policy editor operation</font>
![](https://github.com/shwang362000/ESM/blob/master/Document/ESM_Install/images/%E7%BE%A4%E7%B5%84%E5%8E%9F%E5%89%87%E7%B7%A8%E8%BC%AF%E5%99%A8%E6%93%8D%E4%BD%9C%E7%A4%BA%E6%84%8F%E5%9C%96.png)


## 3-1. 確認設定是否成功  Confirm whether the setting is successful

經過一連串的設定，最後總是要確認以上的設定都正確無誤，且該被監聽的動作已經被如實紀錄，可以利用以下方式來做檢查。開啟PowerShell，隨意輸入指令，如” Get-ChildItem”，接著進入事件檢視器，看看是否有正確紀錄輸入軌跡紀錄。檢視方式如下圖紅框，開啟”事件內容”即可做細部確認。
After a series of settings, it is always necessary to confirm that the above settings are correct and the monitored actions have been truthfully recorded. You can use the following methods to check. Open PowerShell, enter commands at will, such as "Get-ChildItem", and then enter the event viewer to see if the input track record is recorded correctly. The viewing method is shown in the red box as shown in the figure below, and you can confirm the details by turning on "Event Content".

### <font color="red">確認設定正確操作示意圖 Confirm the settings is correct </font>
![](https://github.com/shwang362000/ESM/blob/master/Document/ESM_Install/images/%E7%A2%BA%E8%AA%8D%E8%A8%AD%E5%AE%9A%E6%AD%A3%E7%A2%BA%E6%93%8D%E4%BD%9C%E7%A4%BA%E6%84%8F%E5%9C%96.png)
