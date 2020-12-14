#!/usr/bin/env bash

echo " ----------EE Express RESRfull API Devp--------------"
NAME=$SERVICE_NAME
PORT=$SERVICE_PORT  # 600 0

echo "parameter:$NAME"
count=`ps -ef|grep $PORT|grep -v grep|wc -l`

echo "Current process count:$count"
if [ 0 == $count ];then
    echo "Start app Restart"
    cd /$NAME

    python main.py
    echo "End API Restart"
  else
    ID=`ps -ef | grep $PORT| grep -v "grep" | awk '{print $2}'|head -1`
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
    cd /$NAME
    python main.py
    echo "End API Restart"
fi
