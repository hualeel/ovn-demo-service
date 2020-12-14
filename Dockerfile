FROM registry.cn-qingdao.aliyuncs.com/biz-express/apline-python:v20181229
MAINTAINER Henry li

ENV APP_DIR=appdir \
EE_PYPI=https://mirrors.aliyun.com/pypi/simple/ \
EE_API_SERVICE_PORT=5000

# 创建工作目录
RUN mkdir -p /$APP_DIR
COPY . /$APP_DIR
WORKDIR /$APP_DIR

# 添加apk国内源，安装扩展包
RUN echo "http://mirrors.aliyun.com/alpine/v3.8/main/" > /etc/apk/repositories && \
    echo "http://mirrors.aliyun.com/alpine/v3.8/community" >> /etc/apk/repositories && \
    pip install -i $EE_PYPI --upgrade pip && \
    pip install -i $EE_PYPI -r requirements.txt && \
    chmod 700 ./run.sh

# 端口
EXPOSE $EE_API_SERVICE_PORT
CMD sh ./run.sh