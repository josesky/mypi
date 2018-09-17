# systemctl
```
[root@zz_p_yum network-scripts]# systemctl disable firewalld
Removed symlink /etc/systemd/system/dbus-org.fedoraproject.FirewallD1.service.
Removed symlink /etc/systemd/system/basic.target.wants/firewalld.service.


[root@zz_p_yum network-scripts]# systemctl enable nginx.service
Created symlink from /etc/systemd/system/multi-user.target.wants/nginx.service to /usr/lib/systemd/system/nginx.service.

```

systemd:
    CentOS 7的服务systemctl脚本存放在：/usr/lib/systemd/，有系统（system）和用户（user）之分，即：/usr/lib/systemd/system ，/usr/lib/systemd/user
    每一个服务以.service结尾，一般会分为3部分：[Unit]、[Service]和[Install]，就以nginx为例吧，具体内容如下：


创建service:
在／usr/lib/systemd/system下创建nginx.service文件内容如下（看应用需求也可以在 ／usr/lib/systemd/usr下创建）：
[Unit]
Description=nginx - high performance web server
Documentation=http://nginx.org/en/docs/
After=network.target remote-fs.target nss-lookup.target

[Service]
Type=forking
PIDFile=/run/nginx.pid
ExecStartPre=/usr/sbin/nginx -t -c /etc/nginx/nginx.conf
ExecStart=/usr/sbin/nginx -c /etc/nginx/nginx.conf
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s QUIT $MAINPID
PrivateTmp=true

[Install]
WantedBy=multi-user.target

[Unit]
Description : 服务的简单描述
Documentation ： 服务文档
After= : 依赖，仅当依赖的服务启动之后再启动自定义的服务单元

[Service]
Type : 启动类型simple、forking、oneshot、notify、dbus
Type=simple（默认值）：systemd认为该服务将立即启动。服务进程不会fork。如果该服务要启动其他服务，不要使用此类型启动，除非该服务是socket激活型。

Type=forking：systemd认为当该服务进程fork，且父进程退出后服务启动成功。对于常规的守护进程（daemon），除非你确定此启动方式无法满足需求，使用此类型启动即可。使用此启动类型应同时指定 PIDFile=，以便systemd能够跟踪服务的主进程。

Type=oneshot：这一选项适用于只执行一项任务、随后立即退出的服务。可能需要同时设置 RemainAfterExit=yes 使得 systemd 在服务进程退出之后仍然认为服务处于激活状态。

Type=notify：与 Type=simple 相同，但约定服务会在就绪后向 systemd 发送一个信号。这一通知的实现由 libsystemd-daemon.so 提供。

Type=dbus：若以此方式启动，当指定的 BusName 出现在DBus系统总线上时，systemd认为服务就绪。



PIDFile ： pid文件路径
ExecStartPre ：启动前要做什么，上文中是测试配置文件 －t
ExecStart：启动
ExecReload：重载
ExecStop：停止
PrivateTmp：True表示给服务分配独立的临时空间


[Install]
WantedBy：服务安装的用户模式，从字面上看，就是想要使用这个服务的有是谁？上文中使用的是：multi-user.target ，就是指想要使用这个服务的目录是多用户。



systemctl   status tomcat.service （服务详细信息）

systemctl   is-active tomcat.service（仅显示是否Active)

显示所有已启动的服务

systemctl   list-units --type=service
