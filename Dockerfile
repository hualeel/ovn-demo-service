FROM alpine:3.7
MAINTAINER Henry li

# 环境变量
ENV SERVICE_NAME=ovn_demo_service \
SERVICE_PORT=5000 \
SERVICE_DIR=$SERVIE_NAME \

PYPI=https://mirrors.aliyun.com/pypi/simple/

# 创建工作目录
RUN mkdir -p /$SERVICE_DIR
COPY . /$SERVICE_DIR
WORKDIR /$SERVICE_DIR

# 添加apk国内源，安装扩展包
RUN echo "http://mirrors.aliyun.com/alpine/v3.8/main/" > /etc/apk/repositories && \
    echo "http://mirrors.aliyun.com/alpine/v3.8/community" >> /etc/apk/repositories && \
    apk get python2 && \
    pip install -i $PYPI --upgrade pip && \
    pip install -i $PYPI -r requirements.txt && \
    chmod 700 ./run.sh

# 端口
EXPOSE $SERVICE_PORT
CMD sh ./run.sh