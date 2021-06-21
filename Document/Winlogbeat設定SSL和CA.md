# Winlogbeat 設定 SSL 和 CA

本設定的目的是在所有不同節點之間設定安全性。X-Pack 是 Elastic 軟體包，它基本上負責所有 Elastic Security 功能。所需的一個關鍵元件是設定每個節點之間的 SSL 連線，可以通過多種方法進行。我們也將使用 X-Pack 來執行此操作。

以下提供操作步驟：

1. 產生憑證 (Certificate) 和 CA
2. 設定 Elasticsearch SSL
3. 設定 Winlogbeat SSL
4. Windows 安裝憑證
5. 啟動 Winlogbeat

本設定說明文件的環境為：Elasticsearch 安裝在 Ubuntu 18.04 (Linux) 環境中，而 Winlogbeat 安裝在 Windows 10 環境中。操作前請先確認 Winlogbeat 可以成功打資料至 Elasticsearch。

# 1. 產生憑證 (Certificate) 和 CA

首先，在安裝了 Elasticsearch 的主機上，我們需要建立一個 YAML 檔案 /usr/share/elasticsearch/instances.yml，它將包含我們要使用 SSL 保護的不同節點/範例。就這裡而言，只有 Elasticsearch 和 Winlogbeat。以下範例的 ip 請自行置換成您的 Elasticsearch 和 Winlogbeat 的 ip。

    instances:
        - name: "elasticsearch"
            ip:
            - "192.168.0.104"
        - name: "winlogbeat"
            ip:
            - "192.168.56.1"

接下來，我們將使用 Elastic 的 certutil 工具為我們的範例生成憑證。 這也將生成一個憑證頒發機構（Certificate Authority）。

    sudo /usr/share/elasticsearch/bin/elasticsearch-certutil cert ca --pem --in instances.yml --out certs.zip   

這將為我們的每個範例建立一個 .crt 和 .key 檔案，以及一個 ca.crt 檔案。你可以使用 unzip 來解壓縮不同的憑證。

    unzip /usr/share/elasticsearch/certs.zip -d /usr/share/elasticsearch/

現在我們有了我們的憑證，我們可以設定每個範例。

# 2. 設定 Elasticsearch SSL

首先，我們需要建立一個資料夾將憑證儲存在我們的 Elasticsearch 主機上。

    mkdir /etc/elasticsearch/certs/ca -p

接下來，我們需要將解壓縮的憑證複製到其相關資料夾中並設定正確的許可權。

    sudo cp ca/ca.crt /etc/elasticsearch/certs/ca
    sudo cp elasticsearch/elasticsearch.crt /etc/elasticsearch/certs
    sudo cp elasticsearch/elasticsearch.key /etc/elasticsearch/certs
    sudo chown -R elasticsearch: /etc/elasticsearch/certs
    sudo chmod -R 770 /etc/elasticsearch/certs

接下來，我們需要將 SSL 設定新增到我們的 /etc/elasticsearch/elasticsearch.yml 檔案中。

    # Transport layer
    xpack.security.transport.ssl.enabled: true
    xpack.security.transport.ssl.verification_mode: certificate
    xpack.security.transport.ssl.key: /etc/elasticsearch/certs/elasticsearch.key
    xpack.security.transport.ssl.certificate: /etc/elasticsearch/certs/elasticsearch.crt
    xpack.security.transport.ssl.certificate_authorities: [ "/etc/elasticsearch/certs/ca/ca.crt" ]
    
    # HTTP layer
    xpack.security.http.ssl.enabled: true
    xpack.security.http.ssl.verification_mode: certificate
    xpack.security.http.ssl.key: /etc/elasticsearch/certs/elasticsearch.key
    xpack.security.http.ssl.certificate: /etc/elasticsearch/certs/elasticsearch.crt
    xpack.security.http.ssl.certificate_authorities: [ "/etc/elasticsearch/certs/ca/ca.crt" ]

現在啟動或是重新啟動 Elasticsearch。

    service elasticsearch start
    service elasticsearch restart

# 3. 設定 Winlogbeat SSL

我們需要為執行 Winlogbeat 的主機設定 SSL。 

首先將憑證複製到執行 Winlogbeat 的主機上，您需要同時複製 Winlogbeat 憑證和 CA 憑證。步驟如下：

1. 在 winlogbeat 資料夾 (有 winlogbeat.yml 檔跟 winlogbeat.exe 檔的) 中建立 certs 資料夾。在 Windows 資料夾視窗空白處按右鍵「新增 > 資料夾」即可。

2. 在 certs 資料夾中新增 ca 資料夾。在 Windows 資料夾視窗空白處按右鍵「新增 > 資料夾」即可。

3. 將步驟「1. 產生憑證 (Certificate) 和 CA」所產生的 ca.crt 檔複製到 ca 資料夾中。複製方式可以直接用 vi 打開 ca.crt 檔後，複製其全部文字內容，再到 Windows 開啟任一文字編輯器 (例如 Visual Studio Code) 貼上，再另存新檔成 ca.crt 檔即可。

4. 將步驟「1. 產生憑證 (Certificate) 和 CA」所產生的 winlogbeat.crt 檔複製到 certs 資料夾中。複製方式可以直接用 vi 打開 winlogbeat.crt 檔後，複製其全部文字內容，再到 Windows 開啟任一文字編輯器 (例如 Visual Studio Code) 貼上，再另存新檔成 winlogbeat.crt 檔即可。

5. 將步驟「1. 產生憑證 (Certificate) 和 CA」所產生的 winlogbeat.key 檔複製到 certs 資料夾中。複製方式可以直接用 vi 打開 winlogbeat.key 檔後，複製其全部文字內容，再到 Windows 開啟任一文字編輯器 (例如 Visual Studio Code) 貼上，再另存新檔成 winlogbeat.key 檔即可。

檔案複製完成後，檔案目錄結構示意如下：

    winlogbeat 資料夾
    |-- certs 資料夾
    |   |-- ca 資料夾
    |   |   |-- ca.crt
    |   |-- winlogbeat.crt
    |   |-- winlogbeat.key
    |-- winlogbeat.yml
    |-- winlogbeat.exe
    |-- ...其他 winlogbeat 相關檔案和資料夾

接下來，我們需要將更改新增到 winlogbeat.yml 的 Elasticsearch 設定。

    # Elastic Output
    output.elasticsearch.protocol: https
    output.elasticsearch.ssl.certificate: "certs/winlogbeat.crt"
    output.elasticsearch.ssl.key: "certs/winlogbeat.key"
    output.elasticsearch.ssl.certificate_authorities: ["certs/ca/ca.crt"]

如果我們現在啟動 Winlogbeat，則會收到一個錯誤訊息，即我們的憑證來自不受信任的來源。因此，我們需要做的是將我們的憑證新增為 Windows 主機上的受信任憑證。

# 4. Windows 安裝憑證

開啟 Windows 的「本機安全性原則」。以 Windows 10 為例，「本機安全性原則」會位在「Windows 系統管理工具 > 本機安全性原則」。

## 4.1 安裝本機安全性原則

Windows 10 家庭版預設沒有「本機安全性原則」功能，需要自行安裝。打開任一文字編輯器 (例如 Visual Studio Code)，在任意位置 (例如 winlogbeat 資料夾內) 新建一個空白檔案，將以下程式碼複製貼上後，儲存檔案為「安裝本機安全性原則.bat」。

    @echo off
    pushd "%~dp0"
    dir /b C:\Windows\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientExtensions-Package~3*.mum >List.txt
    dir /b C:\Windows\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientTools-Package~3*.mum >>List.txt
    for /f %%i in ('findstr /i . List.txt 2^>nul') do dism /online /norestart /add-package:"C:\Windows\servicing\Packages\%%i"
    pause

找到該 .bat 檔案，右鍵點選選擇以管理員身份執行，會出現部署的進度，完成之後按任意鍵退出，然後就可以在「Windows 系統管理工具 > 本機安全性原則」開啟了。

## 4.2 設定本機安全性原則

開啟「本機安全性原則」視窗，然後轉到「安全性設定 > 公開金鑰原則 > 憑證路徑驗證設定」，點兩下進入「憑證路徑驗證設定 - 內容」視窗。

在「憑證路徑驗證設定 - 內容」視窗的「存放區」頁籤，勾選「定義這些原則設定」，然後勾選 「允許使用者信任的根 CA 用以驗證憑證」和「允許使用者信任對等信任憑證」選項（如果尚未選中）。

最後，勾選「協力廠商根 CA 與企業根 CA」。

點擊「套用」按鈕，然後點擊「確定」按鈕，完成設定。

## 4.3 安裝憑證

接下來在 Windows 搜尋欄中搜尋 certmgr.msc，進入「certmgr - 憑證」視窗。

在「certmgr - 憑證」視窗，點開左側的「受信任的根憑證授權單位」資料夾，進入「憑證」資料夾。此時視窗的右側會顯示憑證清單。在憑證清單的任意位置的空白處按右鍵，選擇「所有工作 > 匯入」。

然後簡單地按照嚮導操作，並選擇我們之前建立的 ca.crt，依照指示按「下一步」，最後出現匯入成功的視窗。

ca.crt 匯入成功後，再重複以上動作匯入 winlogbeat.crt。

# 5. 啟動 Winlogbeat

以系統管理員身份執行「命令提示字元」，移動到 winlogbeat 資料夾，輸入以下指令啟動 Winlogbeat。

    winlogbeat.exe -e -c winlogbeat.yml

此時 Winlogbeat 應該沒有錯誤訊息，並可以成功打資料至 Elasticsearch。
