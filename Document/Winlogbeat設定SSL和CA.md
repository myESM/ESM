# Winlogbeat 設定 SSL 和 CA

本設定的目的是在所有不同節點之間設定安全性。X-Pack 是 Elastic 軟體包，它基本上負責所有 Elastic Security 功能。所需的一個關鍵元件是設定每個節點之間的 SSL 連線，可以通過多種方法進行。我們也將使用 X-Pack 來執行此操作。

# 1. 產生 CA (Certificate Authority)

首先，在安裝了 Elasticsearch 的主機上，我們需要建立一個 YAML 檔案 /usr/share/elasticsearch/instances.yml，它將包含我們要使用 SSL 保護的不同節點/範例。就這裡而言，只有 Elasticsearch 和 Winlogbeat。

    instances:
        - name: "elasticsearch"
            ip:
            - "192.168.0.104"
        - name: "winlogbeat"
            ip:
            - "192.168.56.1"

接下來，我們將使用 Elastic 的 certutil 工具為我們的範例生成證書。 這也將生成一個證書頒發機構（Certificate Authority）。

    sudo /usr/share/elasticsearch/bin/elasticsearch-certutil cert ca --pem --in instances.yml --out certs.zip   

這將為我們的每個範例建立一個 .crt 和 .key 檔案，以及一個 ca.crt 檔案。你可以使用 unzip 來解壓縮不同的證書。

    unzip /usr/share/elasticsearch/certs.zip -d /usr/share/elasticsearch/

現在我們有了我們的證書，我們可以設定每個範例。

# 2. 設定 Elasticsearch SSL

首先，我們需要建立一個資料夾將證書儲存在我們的 Elasticsearch 主機上。

    mkdir /etc/elasticsearch/certs/ca -p

接下來，我們需要將解壓縮的證書複製到其相關資料夾中並設定正確的許可權。

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

現在重新啟動 Elasticsearch。

    service elasticsearch restart

# 3. 設定 Winlogbeat SSL

