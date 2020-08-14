# 簡介
Use docker to build suricata + EFK

# 部署
### 進到 suricata/dist/suricata.yaml 修改 suircata 的 yaml 檔
修改 `HOME_NET` 成要防護的網段(ex. VM 的 IP)
### 進到 suricata/dist/Dockerfile 修改 Dockerfile
修改最後一行的 `enp0s8` 成要監控的網卡
