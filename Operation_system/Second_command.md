### 使用nohup 及时在终端退出也不影响

nohup /usr/local/frp/frps -c /usr/local/frp/frps.ini > /tmp/frps.log 2>&1 &

### 查看当前cpu核心数

grep 'model name' /proc/cpuinfo


#### Centos7 防火墙
centos 7 默认使用了firewalld ，iptables-service 没有安装

所以，如果要用iptables，首先要禁用firewalld,同时安装iptables-service 。否则不会在开机时去读iptables设置的规则

 

Java代码  收藏代码
systemctl stop firewalld  
systemctl disable firewalld  
yum install iptables-services -y  
systemctl enable iptables  
 

保存规则

Java代码  收藏代码
/usr/libexec/iptables/iptables.init save  
  
##或者  
iptables-save > /etc/sysconfig/iptables  



#### 关于mtu

默认的MTU 是1500 其实真正传输只有1472
Linux 下:
ping -c 3 -s 1473 -M do www.bakdu.com

**Windows设置部分片**:
ping -l 1473 -f www.baidu.com

ping -i 0 快速的ping 

#### iptables 的一些转发

我们可以使用 sysctl net.ipv4.ip_forward 来查看这个内核参数的数值
可以使用sysctl -w 进行临时性写入
使用vi /etc/sysctl.conf 永久写入
net.ipv4.ip_forward = 1

iptables -A PREROUTING -d 133.133.177.52/32 -p tcp -m tcp --dport 33899 -j DNAT --to-destination 192.168.0.225:3389
iptables -A POSTROUTING -d 192.168.0.225/32 -p tcp -m tcp --dport 3389 -j SNAT --to-source 172.16.88.52

iptables -A FORWARD -d 192.168.0.225/32 -p tcp -m tcp --dport 3389 -j ACCEPT

iptables -t nat -A POSTROUTING -s 192.168.122.0/24 -o eth0 133.133.66.11 -j MASQUERADE

\- ｏ　是出口外网的网卡

#### centos7 添加ip和路由


ip addr add 192.168.100.10/24 dev eth0
ip addr show eth0

ip addr del 192.168.100.10/24 dev eth0

查看数据包从哪里来

[root@ansible ~]# ip route get 16.255.132.12
16.255.132.12 via 172.31.143.253 dev eth0 src 172.31.132.20 
    cach




显示网络统计  ip -s link 

当你需要获取一个特定网络接口的信息时，在网络接口名字后面添加选项ls即可。使用多个选项-s会给你这个特定接口更详细的信息。特别是在排除网络连接故障时

ip -s -s link ls eth0

ip route list
ip route add 10.8.8.0/24 via 10.0.0.1 dev eth0

修改默认路由
ip route add default via 10.0.0.1 dev eth0
ip route del 10.8.8.0/24
ip route del default

#### ss 查看tcp 连接数

    ss -n | awk ' {++S[$1]} END {for(a in S) print a, S[a]}'

    这里通过awk 的++S 来加第一列中所有一样的, 通过一个循环然后在把加的结果输出,这里要用ss 因为这个比netstat 这个速度要快

#### Linux 取出文件中不是#，还有空行的

    [root@localhost tmp]# egrep ^[^#$] aa.txt
    ni shi shui a
    nihao #

    ^
    在通配符中表示取反
    例如：[^abc] 表示匹配除了abc外的任意一个字符
    grep -v "^#" file | grep -v '^$'

#### Operation_memory

-   1 buffer 内存中的buffer是为了提高效率，让需要写入硬盘的数据先写入buffer在后台慢慢在写入硬盘

-   2 cache 为了提高效率，硬盘中读取的数据先暂存到cache，避免重复读取硬盘。

-   3 swap 存内存中需要历史交换的数据


      1）没有swap的在系统内分区
      fdisk /dev/sdb
      mkswap /dev/sdb1
      swapon /dev/sdb1
      swapoff /dev/sdb1

      2)在根分区创建swap文件
      [root@tianxia ~]# dd if=/dev/zero of=/tmp/swapfile bs=1M count=1000
      [root@tianxia ~]# mkswap /tmp/swapfile
      [root@tianxia ~]# swapon /tmp/swapfile

      3)系统对swap设置
      [root@tianxia ~]# cat /proc/sys/vm/swappiness
      60
      设置为1
      echo '1' > /proc/sys/vm/swappiness
      同时
      sed -i '$ a\vm.swappiness=1 ' /etc/sysctl.conf
      sysctl -p

#### vmstat

    [root@tianxia ~]# vmstat -t 3
    procs -----------memory---------- ---swap-- -----io---- --system-- -----cpu------ ---timestamp---
    r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
    0  0      0  68780   4252 709252    0    0    12   149   17   11  0  0 100  0  0	2017-09-21 14:46:29 CST
    1  0      0  71356   4276 698864    0    0   587     0  223  172  0  0 99  1  0	2017-09-21 14:46:32 CST
    0  0      0  75564   4284 698988    0    0     0    33  118   80  0  0 100  0  0	2017-09-21 14:46:35 CST
    0  0      0  74604   4284 694244    0    0     0    71  572  181  6  0 94  0  0	2017-09-21 14:46:38 CST

##### 具体标示意思

      1)cache 缓存较多的数据，是系统对硬盘读比较多，buffer多是系统对硬盘写比较多。
      2）si so 是硬盘读写。长期大于0是系统要经常读写swap
      3）bi bo 是硬盘的读写，针对内存是in和out；这个主要是看是否符合预期如果不符合要检查。
      4）us 经常大于50%说明用户进程占用cpu时间长，需要对程序效率进行提升。
      5）sy 是内核占用的如果较高需要检查系统
      6）wa cpu等I/O较高标示硬盘瓶颈，检查程序的随机读写
      7) r  标示正在运行队列中任务数。总数超过cpu核心数cpu性能瓶颈。

##### 通过wget得到解决

wget ftp://IP:PORT/_ --ftp-user=xxx --ftp-password=xxx -r

注:
星号_必须有,否则下载下来的就一个文件index.html
    -r参数就是用来目录下载的