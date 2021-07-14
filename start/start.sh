#!/bin/bash

## Just got a new machine or expanded own working  directory

curl -s start.sh

## Set local system

### Auto time update
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
ntpdate ntp.aliyun.com
echo "01 01 * * * /usr/sbin/ntpdate ntp.aliyun.com   > /dev/null 2>&1" >> /etc/crontab
systemctl restart crond.service

### Set ulimit
ulimit -n 1048576
sed -i "/nofile/d" /etc/security/limits.conf
echo "* hard nofile 1048576" >> /etc/security/limits.conf
echo "* soft nofile 1048576" >> /etc/security/limits.conf
echo "root hard nofile 1048576" >> /etc/security/limits.conf
echo "root soft nofile 1048576" >> /etc/security/limits.conf

## Set custom 

useradd -m -s /bin/bash  TT
line="TT ALL=(ALL) NOPASSWD: ALL" bash -c 'grep "$line" /etc/sudoers  || echo "$line" >> /etc/sudoers'

## Other

apt install tmux xclip  ansible 
