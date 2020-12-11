FROM python:3.7-slim

RUN pip install --no-cache-dir \
                pandas==1.1.1 \
                numpy==1.15.4 \
                scipy==1.1.0 \
                tensorflow==1.14.0 \
                Keras==2.2.4 \
                matplotlib==3.3.0 \
                scikit-learn==0.20.1 \
                elasticsearch==6.3.0 \
                networkx==2.4 \
                flask==1.1.2

# 設定時區
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /OMP

# Sleeeeeeeeep
CMD ["sleep infinity"]

