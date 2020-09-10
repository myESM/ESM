FROM python:3.8.5-buster

RUN pip install --no-cache-dir wheel==0.31.1 \
                Cython==0.28.2 \
                elasticsearch==6.3.1 \
                Flask==1.0.2 \
                xgboost==1.0.0 \
                scikit-learn==0.23.1 \
                pandas==0.25.0 \
                numpy==1.18.4

# 設定時區
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Sleeeeeeeeeeeeeeeeeeeeeeeeeeep
CMD ["sleep infinity"]
