FROM continuumio/anaconda3:2020.07

# 建立資料夾; -p 建立子目錄
COPY ./ETA-ATTACK /usr/src/ETA-ATTACK
RUN pip install --no-cache-dir -r /usr/src/ETA-ATTACK/requirements.txt

# 指定docker image 進入點
WORKDIR /usr/src/ETA-ATTACK

# 設定時區
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# RUN python3 main.py
CMD ["python3", "eta_attack_api.py"]
