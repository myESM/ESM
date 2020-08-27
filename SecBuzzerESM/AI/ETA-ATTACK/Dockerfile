FROM continuumio/anaconda3:2020.07

# 建立資料夾; -p 建立子目錄
COPY ./ETA1 /usr/src/ETA1
RUN pip install --no-cache-dir -r /usr/src/ETA1/requirements.txt

# 指定docker image 進入點
WORKDIR /usr/src/ETA1

# 設定時區
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# RUN python3 main.py
CMD ["python3", "eta1_api.py"]
