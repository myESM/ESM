FROM python:3.8.5-buster

RUN pip install --no-cache-dir \
                xgboost==1.2.0 \
                scikit-learn==0.23.2 \
                numpy==1.19.1 \
                pandas==1.1.2 \
                flask==1.1.2 \
                elasticsearch==7.9.1

# 設定時區
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Sleeeeeeeeeeeeeeeeeeeeeeeeeeep
CMD ["sleep infinity"]
