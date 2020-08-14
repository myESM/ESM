FROM python:3.8.5-slim

# 建立資料夾; -p 建立子目錄
COPY ./Winlog /usr/src/Winlog
RUN pip install --no-cache-dir -r /usr/src/Winlog/requirements.txt

# 指定docker image 進入點
WORKDIR /usr/src/Winlog

# 設定時區
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# RUN python3 main.py
CMD ["python3", "winlog_api.py"]
