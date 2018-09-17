!$ 上个命令的参数


miner minerd 挖矿木马程序

  自动

计划任务
开机自启动
系统命令被替换

使用非root 用户添加

crontab -u bin -e
crontab -u bin  -l

所有的计划任务都在这个目录下有文件
/var/spool/cron/


高级 crontab 篡改系统的计划任务
ls /etc/cron
#### 这个是日志切割
vim /etc/cron.daily/logrotate

查看计划任务文件是否被修改
[root@localhost cron]# md5sum /etc/cron.daily/logrotate
ca539e563f23aaac7a232008245b53dd  /etc/cron.daily/logrotate
[root@localhost cron]# vim /etc/cron.daily/logrotate
[root@localhost cron]# md5sum /etc/cron.daily/logrotate
9d17d50f6ce02e2d649bcc1fe43bf8a0  /etc/cron.daily/logrotate

系统的安装完毕后 都固定下来了
find /etc/cron* -type f | xargs -I {} md5sum {}  > /usr/share/file_md5.v1
修改后
find /etc/cron* -type f | xargs -I {} md5sum {}  > /usr/share/file_md5.v2

#### 我在我的生产环境来进行验证

find /etc/* -type f | xargs -I {} md5sum -I {} > /usr/shar/admin_c.v1

find /etc/* -type f | xargs -I {} md5sum -I {} > /usr/shar/check.v1

1、对比法查看文件 md5sum

2、find -mtime -1 当天修改的文件

3、 用rmp -V 检查文件包的名称 文件包的完整性
S size 大小不一致
