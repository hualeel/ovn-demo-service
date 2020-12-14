# -*- coding:utf-8 -*-
"""
Author:
名称：kubeovn demo
功能描述：KUBEOVN DEMO
"""

from flask import Flask, current_app, redirect, url_for
import requests
import json
import os

app = Flask(__name__,
            static_url_path='/python',  # 访问静态资源的url前缀，默认值是static
            static_folder='static',  # 静态文件目录，默认就是static
            template_folder='templates',  # 模板文件的目录，默认是templates
            )


# 配置参数的使用方式
# 1.使用配置文件
# app.config.from_pyfile("config.cfg")

# 2.使用对象配置参数
# class Config(object):
#     DEBUG = True
#     ITCAST = "python" # 自用参数
# app.config.from_object(Config)

# 3.直接操作config的字典对象
# app.config["DEBUG"] = True

# 以装饰器形式绑定路由
@app.route('/kube-ovn/get-pod-ip/<string:svc_name>', methods=["GET"])
def get_pod_ip(svc_name):
    pod_ip_list = []
    url = "https://139.186.153.231:6443/api/v1/namespaces/default/endpoints/" + svc_name

    payload = {}
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkZLZjQ4NEFmd3gxbXByQ3hia1JfVVN6aTVOQzVtVlUwbFJ4RXcwRE02V2sifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi10b2tlbi05anBtbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50Lm5hbWUiOiJhZG1pbiIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6ImU0MmQ2Nzc1LTk4NDQtNDRjOS1hZDY5LWYxZDgxNDkyZWI4NSIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDprdWJlLXN5c3RlbTphZG1pbiJ9.vPBQtVXfstiB-e-4lkAJpNBpnLnFPGxv0vK88Vl52sjcxG15pOqGeAcHEqq_YfcgQ7NrgZlsK7nOF4XGTByNbVEYdz9e3INNt5eX5DDDNSxhi9PkrOZex9wmikeFzZiQZG4yaVU2MjaemW7dwSKI6CtAwwEsSwOAld2csl2YaF-dKenHFJ7DyH5sykvybsyphaERthH3s3UyQKeE6pwa8MITMlkyk0B6SDqYMpfvh01mVfy31q_hvjaoTqc7QJrZEcyeNU-AJvgn-NLBrEcDdjWduRbOCcdXsE7sk7Fmf1dptxjBq3cv7s1AOPKz80xUhYtMWMPp0Jj5dkwa7H08Bw'
    }

    response = requests.request("GET", url, headers=headers, data=payload, verify=False)

    print(response.text)
    pod_ip = json.loads(response.text).get("subsets")[0].get("addresses")[0].get("ip")
    return pod_ip


if __name__ == '__main__':
    # 通过url_map可以查看整个flask中的路由信息
    print (app.url_map)
    service_port = os.getenv("SERVICE_PORT")

    # 启动flask程序
    app.run(host="0.0.0.0", port=service_port)
