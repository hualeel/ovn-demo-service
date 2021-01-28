# -*- coding:utf-8 -*-
"""
Author:
名称：kubeovn demo
功能描述：KUBEOVN DEMO
"""

from flask import Flask, current_app, redirect, url_for, render_template
from flask_cors import *
import requests
import json
import os
import random

app = Flask(__name__, template_folder="templates")


# 获取pod ip list
@app.route('/<string:ns>/<string:svc_name>', methods=["GET"])
@cross_origin()
def get_pod_ip(ns, svc_name):
    k8s_api_server = os.getenv("py")
    k8s_api_auth = os.getenv("K8S_API_AUTH")
    # k8s_namespace = os.getenv("K8S_NAMESPACE")
    k8s_namespace = ns

    url = "https://" + k8s_api_server + ":6443/api/v1/namespaces/" + k8s_namespace + "/endpoints/" + svc_name

    payload = {}

    headers = {
        "Authorization": "Bearer " + k8s_api_auth
    }
    response = requests.request("GET", url, headers=headers, data=payload, verify=False)

    if (response.status_code >= 200) and (response.status_code <= 300):

        print(response.text)
        pod_ip_list = []
        for item in json.loads(response.text).get("subsets")[0].get("addresses"):
            pod_ip_list.append(item["ip"])

        # ip_str = ""
        # for ip in ip_list:
        #     ip_str = ip_str + ip + ";"
        # ip_str = "Pod IP: " + ip_str
        # pod_ip_list = ["128.0.0.1", "192.0.0.1"]
        print(pod_ip_list)
        pod_id = random.choice(pod_ip_list)

        pod_ip_list_str = " ; "
        for each in pod_ip_list:
            pod_ip_list_str = each + pod_ip_list_str

        # 通过pod ip访问应用
        url1 = "http://" + pod_id + ":6002/get-pod"
        payload1 = {}
        headers1 = {}
        response1 = requests.request("GET", url1, headers=headers1, data=payload1)

        if (response1.status_code >= 200) and (response1.status_code <= 300):
            msg_text = pod_ip_list_str + "<br>" + response1.text
        else:
            msg_text = response1.status_code
        # return msg_text
        # return render_template("index.html", pod_ip_list=pod_ip_list)
    else:
        msg_text = response.status_code
    return msg_text


if __name__ == '__main__':
    print(app.url_map)
    service_port = os.getenv("SERVICE_PORT")

    # 启动flask程序
    app.run(host="0.0.0.0", port=service_port)
