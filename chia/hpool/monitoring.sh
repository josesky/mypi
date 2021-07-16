#!/bin/bash

set -x

## Testing process
date=$(date +%Y-%m-%d-%H:%M:%S)

process=$(ps -ef | grep hpool-miner-chia | wc -l)

if [ "$process" -lt 2  ];then
        echo "${date} : WARING  Hpool stoped we will reboot it !!" >> /var/log/hpool/hpool_moriting.log
        /bin/bash /root/start.sh
else
        echo "${date} : Hpool runing good !!" >> /var/log/hpool/hpool_moriting.log
fi
