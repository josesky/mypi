#!/bin/bash

#kye=da2aa800-0ee0-3e80-a919-d99a4527ff8b

#app=linux-1.4.5.tar.gz

hpool () {

#mkdir -pv /root/uupool

#tar -zxvf $app  -C /root/uupool

#./cmd init -account_key $kye  -miner_name `hostname`

for i in `lsblk |grep 14.6T |awk '{print $1}'`;do mount /dev/${i} /data/${i};done

#directory=$(ls /data* | grep data | grep -w -v data| awk -F "/" '{print $2}' | cut -d ":" -f 1)

#directory=$(ls /data/* |grep data|grep -v final |awk -F "/" '{print $3}'  | cut -d ":" -f 1)
#
#for i in $directory
#do
#
#./cmd add -path /data/${i}/
#
#done
#
#./cmd stop

nohup /root/linux/hpool-miner-chia --config /root/linux/config.yaml >> /var/log/hpool.log 2>&1 &

}

hpool
