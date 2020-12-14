#!/usr/bin/env bash

echo " ----------EE Express RESRfull API Devp--------------"
SERVICE_NAME=$SERVICE_NAME  # kube_ovn_demo_service
SERVICE_PORT=$SERVICE_PORT  # 6000
SERVICE_DIR=$SERVICE_DIR    # app


echo "parameter:$SERVICE_NAME"
count=`ps -ef|grep $SERVICE_PORT|grep -v grep|wc -l`

echo "Current process count:$count"
if [ 0 == $count ];then
    echo "Start app Restart"
    cd /$SERVICE_DIR

    python main.py
    echo "End API Restart"
  else
    ID=`ps -ef | grep $SERVICE_PORT| grep -v "grep" | awk '{print $2}'|head -1`
    echo "Current process id :$ID"
    echo "Start Kill API Process..."
    for id in $ID
        do
            kill $id
            echo "killed $id"
            sleep 2
            echo "Please Wait..."
        done
    echo "End Kill API Process"

    sleep 3
    echo "Start API Restart..."
    echo "Please Wait..."
    cd /$SERVICE_DIR
    python main.py
    echo "End API Restart"
fi
