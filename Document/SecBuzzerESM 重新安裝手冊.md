# SecBuzzerESM 重新安裝手冊

進入Ubuntu中，因安裝過程需使用 root 權限，請先進行帳號的切換

```bash
sudo su
```

# 1. 關閉現行所有的docker container
```bash
docker kill $(docker ps -q)
docker rm $(docker ps -a -q)
```

# 2. 刪除所有docker image
```bash
docker rmi $(docker images -q)
```

# 3. 將docker與docker-compose清掉
```bash
rm /usr/bin/docker*
rm /usr/local/bin/docker-compose
```

# 4. 備份env
```bash
cp /opt/SecBuzzerESM/SecBuzzerESM.env /home/esm/
```

# 5. 移除SecBuzzerESM
```bash
rm -r /opt/SecBuzzerESM
```

# 6. 重新安裝...
剩餘步驟可參考SecBuzzerESM 離線安裝手冊或是連線安裝手冊
內容是一樣的
