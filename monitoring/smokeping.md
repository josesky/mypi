# smokeping 安装使用

## 简介

  Smokeping是一款开源最佳网络延迟可视化监控软件。

> [官方网站](https://oss.oetiker.ch/smokeping/index.en.html)为：<https://oss.oetiker.ch/smokeping/index.en.html>

### 软件安装

- 当前环境Cetnso7.5

#### 安装依赖的软件包

- 能通过yum安装的可以通过yum安装,安装epel源
    > yum -y install epel-release
- 安装必须要的包
    > yum install fping curl bind-utils httpd httpd-devel mod_fcgid  rrdtool perl-rrdtool
- 下载最近的安装包
    > curl -O <https://oss.oetiker.ch/smokeping/pub/smokeping-2.7.2.tar.gz>
- 需要安装很多perl的扩展看着样子很多
    > yum -y install cpan perl perl-FCGI perl-CGI perl-Digest-HMAC perl-Net-Telnet perl-Net-OpenSSH perl-Net-SNMP perl-LDAP perl-Net-DNS perl-IO-Pty-Easy perl-Test-Simple perl-Sys-Syslog perl-lib www-perlperl-IO-Socket-SSL perl-Socket6 perl-CGI-SpeedyCGI perl-FCGI perl-Time-HiRes perl-ExtUtils-MakeMaker perl-GSSAPI perl-XML-Writer perl-Module-Build

#### 安装smokeping软件

- 安装软件

    > ./configure --prefix=/opt/smokeping
    > /usr/bin/gmake install

- 配置软件目录

    > cd /opt/smokeping/etc
    > cp config.dist config
    > cp /opt/smokeping/etc/basepage.html.dist /opt/smokeping/etc/basepage.html

- 编辑配置文件

```bash
    cat << EOF > /opt/smokeping/etc/config
    *** General ***

    owner    = tianxia
    contact  = tianxia@centos8.com
    mailhost = my.mail.host
    sendmail = /usr/sbin/sendmail

    # NOTE: do not put the Image Cache below cgi-bin
    # since all files under cgi-bin will be executed ... this is not
    # good for images.
    imgcache = /var/www/smokeping/cache
    imgurl   = cache
    datadir  = /opt/smokeping/data
    piddir  = /opt/smokeping/var
    cgiurl   = http://127.0.0.1/smokeping/smokeping.fcgi
    smokemail = /opt/smokeping/etc/smokemail.dist
    tmail = /opt/smokeping/etc/tmail.dist

    # specify this to get syslog logging
    syslogfacility = local0

    # each probe is now run in its own process
    # disable this to revert to the old behaviour
    # concurrentprobes = no

    *** Alerts ***

    to = peter@random.com
    from = smokealert@random.com

    +bigloss
    type = loss
    # in percent
    pattern = ==0%,==0%,==0%,==0%,>0%,>0%,>0%
    comment = suddenly there is packet loss

    +someloss
    type = loss
    # in percent
    pattern = >0%,*12*,>0%,*12*,>0%
    comment = loss 3 times  in a row

    +startloss
    type = loss
    # in percent
    pattern = ==S,>0%,>0%,>0%
    comment = loss at startup

    +rttdetect
    type = rtt
    # in milli seconds
    pattern = <10,<10,<10,<10,<10,<100,>100,>100,>100
    comment = routing messed up again ?

    +hostdown
    type = loss
    # in percent
    pattern = ==0%,==0%,==0%, ==U
    comment = no reply

    +lossdetect
    type = loss
    # in percent
    pattern = ==0%,==0%,==0%,==0%,>20%,>20%,>20%
    comment = suddenly there is packet loss

    *** Database ***

    step     = 60
    pings    = 30

    # consfn mrhb steps total

    AVERAGE  0.5   1  1008
    AVERAGE  0.5  12  4320
        MIN  0.5  12  4320
        MAX  0.5  12  4320
    AVERAGE  0.5 144   720
        MAX  0.5 144   720
        MIN  0.5 144   720

    *** Presentation ***

    template = /opt/smokeping/etc/basepage.html

    + charts

    menu = Charts
    title = The most interesting destinations

    ++ stddev
    sorter = StdDev(entries=>4)
    title = Top Standard Deviation
    menu = Std Deviation
    format = Standard Deviation %f

    ++ max
    sorter = Max(entries=>5)
    title = Top Max Roundtrip Time
    menu = by Max
    format = Max Roundtrip Time %f seconds

    ++ loss
    sorter = Loss(entries=>5)
    title = Top Packet Loss
    menu = Loss
    format = Packets Lost %f

    ++ median
    sorter = Median(entries=>5)
    title = Top Median Roundtrip Time
    menu = by Median
    format = Median RTT %f seconds

    + overview

    width = 600
    height = 50
    range = 10h

    + detail

    width = 600
    height = 200
    unison_tolerance = 2

    "Last 3 Hours"    3h
    "Last 30 Hours"   30h
    "Last 10 Days"    10d
    "Last 400 Days"   400d

    #+ hierarchies
    #++ owner
    #title = Host Owner
    #++ location
    #title = Location

    *** Probes ***

    + FPing
    binary = /usr/sbin/fping

    + EchoPingHttp

    + DNS
    binary = /usr/bin/dig
    pings = 5
    step = 180


    *** Targets ***

    probe = FPing

    ## You have to edit and uncomment all what you want below this.
    # Please, refer to smokeping_config man page for more info
    # The given adresses aren't real to avoid DoS.

    menu = Top
    title = Network Latency Grapher
    remark = Random Company Ltd.

    + Local
    menu = SmokersLab
    title = Network Management

    #
    ####### LATENCY ########
    #

    ++ Latency

    menu = Latency
    title = Measure of Latency using icmp ping
    +++ telecom-beijing
    menu = 北京电信
    title = 北京电信
    alerts = someloss
    host = 220.181.22.11

    EOF
```

### 配置httpd 设置页面访问

#### 创建需要的目录并赋权限

```bash
mkdir /opt/smokeping/data
mkdir /opt/smokeping/var
mkdir /var/www/smokeping
mkdir /var/www/smokeping/cache
cp -R /opt/smokeping/htdocs/* /var/www/smokeping
mv /var/www/smokeping/smokeping.fcgi.dist /var/www/smokeping/smokeping.fcgi
chown -R apache:apache /var/www/smokeping
````

## 创建程序运行的虚拟机

```bash
cat << EOF > /etc/httpd/conf.d/smokeping.conf
Alias /smokeping "/var/www/smokeping"
<Directory /var/www/smokeping>
Options Indexes FollowSymLinks MultiViews ExecCGI
AllowOverride All
Order allow,deny
Allow from all
DirectoryIndex smokeping.fcgi
</Directory>
EOF
```

## 启动服务

#### 启动smokeping

> /opt/smokeping/bin/smokeping --config=/opt/smokeping/etc/config --debug-daemon

#### 启动httpd

systemctl start httpd
