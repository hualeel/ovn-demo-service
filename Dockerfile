FROM hualeel/python3_flask:latest
MAINTAINER Henry li

# 环境变量
ENV SERVICE_PORT=6001 \
SERVICE_DIR=app \
PYPI=https://mirrors.aliyun.com/pypi/simple/ \
K8S_API_AUTH=xxxxxxxxx
RUN python -m pip install --upgrade pip

ENV K8S_NAMESPACE=tke-poc-test
COPY . /$SERVICE_DIR
WORKDIR /$SERVICE_DIR


EXPOSE $SERVICE_PORT
CMD [ "python", "./main.py" ]
