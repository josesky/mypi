# 内网穿透工具frp使用说明
https://github.com/fatedier/frp/blob/master/README_zh.md
```
因为需要保证服务一直运行，使用supervisor自启

sudo apt install supervisor
然后在/etc/supervisor/conf.d下新建一个配置文件frp.conf，输入以下内容。command应该是你放置frp软件的位置。

[program:frp]
command = /home/ubuntu/frp_0.14.1_linux_386/frps -c /home/ubuntu/frp_0.14.1_linux_386/frps.ini
autostart = true
然后启动supervisor，如果事先已经安装好了supervisor那么就重新启动。之后查看一下supervisor的运行状态，看看frp是否已在运行。

# 重启supervisor
sudo systemctl restart supervisor
# 查看supervisor运行状态
sudo supervisorctl status
