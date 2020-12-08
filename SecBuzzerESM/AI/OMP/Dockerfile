FROM python:3.7-slim

# 建立資料夾; -p 建立子目錄
RUN mkdir -p /usr/omp/code
COPY ./code /usr/omp/code
RUN pip install --no-cache-dir -r /usr/omp/code/requirements.txt

# 指定docker image 進入點
WORKDIR /usr/omp/code

# 設定時區
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# RUN python3 main.py
CMD ["python3", "api.py"]

