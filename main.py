# -*- coding:utf-8 -*-
"""
Author:
名称：kubeovn demo
功能描述：KUBEOVN DEMO
"""

from flask import Flask, current_app, redirect, url_for, render_template
import requests
import json
import os

# app = Flask(__name__,
#             static_url_path='/python',  # 访问静态资源的url前缀，默认值是static
#             static_folder='static',  # 静态文件目录，默认就是static
#             template_folder='templates',  # 模板文件的目录，默认是templates
#             )
app = Flask(__name__, template_folder="templates")


# 获取pod ip地址
@app.route('/kube-ovn/get-pod-ip/<string:svc_name>', methods=["GET"])
def get_pod_ip(svc_name):
    k8s_api_server = os.getenv("K8S_API_SERVER")
    k8s_api_auth = os.getenv("K8S_API_AUTH")
    k8s_namespace = os.getenv("K8S_NAMESPACE")

    url = "https://" + k8s_api_server + ":6443/api/v1/namespaces/" + k8s_namespace + "/endpoints/" + svc_name

    payload = {}

    headers = {
        "Authorization": "Bearer " + k8s_api_auth
    }
    response = requests.request("GET", url, headers=headers, data=payload, verify=False)

    print(response.text)
    ip_list = []
    for item in json.loads(response.text).get("subsets")[0].get("addresses"):
        ip_list.append(item["ip"])

    ip_str = ""
    for ip in ip_list:
        ip_str = ip_str + "   " + ip
    ip_str = "Pod IP: " + ip_str

    return render_template("index.html", pod_ip_list=ip_str)


# 获取pod内部信息
@app.route('/kube-ovn/get-pod', methods=["GET"])
def get_pod(pod_ip):
    url = "https://" + pod_ip + "/kube-ovn/get-pod"

    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload, verify=False)

    print(response.text)
    return "aa"


if __name__ == '__main__':
    # 通过url_map可以查看整个flask中的路由信息
    print (app.url_map)
    service_port = os.getenv("SERVICE_PORT")

    # 启动flask程序
    app.run(host="0.0.0.0", port=5001)
