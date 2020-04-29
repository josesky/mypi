### 2>&1

```
2>&1
每次查重定向问题时，我们总会看到这句话，一般人很难理解这到底是在干嘛。我一开始以为是2要大于1什么的，真是笑话。
其实这是个重定向的设置，设置让2重定向到1，也就是让stderr标准错误重定向到stdout标准输出，然后两个并在一起再重定向。其中&没什么意思只是区分开来1是代表stdout而不是代表一个文件名。
用起来的格式是：cmd > file 2>&1。
为什么设置要放在后面呢?
具体暂时还不知道，只知道是这么用，放在前面还不行只能放在后面。
比如：
$ git push > log.txt 2>&1
```
### 域名解析顺序

在linux中，往往解析一个域名时，先会找/etc/hosts文件，如果/etc/hosts文件没有对应，才会去找DNS，那么有什么方式，让主机先找DNS呢？
当然有，在/etc/nsswitch.conf这个文件里定义，
#vi /etc/nsswitch.conf
hosts:      files dns    //默认配置

从配置文件就可以看出系统是先files（/etc/hosts）解析，再从dns（/etc/resolv.conf）解析。

修改成下面这样：
hosts:      dns files  （centos6）

hosts:     dns files myhostname （centos7）
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



#### Operation_memory
  - 1 buffer 内存中的buffer是为了提高效率，让需要写入硬盘的数据先写入buffer在后台慢慢在写入硬盘

  - 2 cache 为了提高效率，硬盘中读取的数据先暂存到cache，避免重复读取硬盘。

  - 3 swap 存内存中需要历史交换的数据
  
```
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
  
```
#### vmstat
```
[root@tianxia ~]# vmstat -t 3
procs -----------memory---------- ---swap-- -----io---- --system-- -----cpu------ ---timestamp---
r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
0  0      0  68780   4252 709252    0    0    12   149   17   11  0  0 100  0  0	2017-09-21 14:46:29 CST
1  0      0  71356   4276 698864    0    0   587     0  223  172  0  0 99  1  0	2017-09-21 14:46:32 CST
0  0      0  75564   4284 698988    0    0     0    33  118   80  0  0 100  0  0	2017-09-21 14:46:35 CST
0  0      0  74604   4284 694244    0    0     0    71  572  181  6  0 94  0  0	2017-09-21 14:46:38 CST
```

##### 具体标示意思

```
  1)cache 缓存较多的数据，是系统对硬盘读比较多，buffer多是系统对硬盘写比较多。
  2）si so 是硬盘读写。长期大于0是系统要经常读写swap
  3）bi bo 是硬盘的读写，针对内存是in和out；这个主要是看是否符合预期如果不符合要检查。
  4）us 经常大于50%说明用户进程占用cpu时间长，需要对程序效率进行提升。
  5）sy 是内核占用的如果较高需要检查系统
  6）wa cpu等I/O较高标示硬盘瓶颈，检查程序的随机读写
  7) r  标示正在运行队列中任务数。总数超过cpu核心数cpu性能瓶颈。
```

##### 查看当前连接状况
```
ss -tnp | grep ':80\>' |  awk '{print $5}' | awk -F : '{print $4}' | sort | uniq -c | sort -rn | more

```
针对uniq用法  
```
[zhangy@BlackGhost ~]$ uniq --help  
用法：uniq [选项]... [文件]  
从输入文件或者标准输入中筛选相邻的匹配行并写入到输出文件或标准输出。  
  
不附加任何选项时匹配行将在首次出现处被合并。  
  
长选项必须使用的参数对于短选项时也是必需使用的。  
 -c, --count              //在每行前加上表示相应行目出现次数的前缀编号  
 -d, --repeated          //只输出重复的行  
 -D, --all-repeated      //只输出重复的行，不过有几行输出几行  
 -f, --skip-fields=N     //-f 忽略的段数，-f 1 忽略第一段  
 -i, --ignore-case       //不区分大小写  
 -s, --skip-chars=N      //根-f有点像，不过-s是忽略，后面多少个字符 -s 5就忽略后面5个字符  
 -u, --unique            //去除重复的后，全部显示出来，根mysql的distinct功能上有点像  
 -z, --zero-terminated   end lines with 0 byte, not newline  
 -w, --check-chars=N      //对每行第N 个字符以后的内容不作对照  
 --help              //显示此帮助信息并退出  
 --version              //显示版本信息并退出  
 ```
 
 针对sort用法
 ```
 -b, --ignore-leading-blanks  ignore leading blanks
  -d, --dictionary-order      consider only blanks and alphanumeric characters
  -f, --ignore-case           fold lower case to upper case characters
  -g, --general-numeric-sort  compare according to general numerical value
  -i, --ignore-nonprinting    consider only printable characters
  -M, --month-sort            compare (unknown) < 'JAN' < ... < 'DEC'
  -h, --human-numeric-sort    compare human readable numbers (e.g., 2K 1G)
  -n, --numeric-sort          compare according to string numerical value
  -R, --random-sort           sort by random hash of keys
      --random-source=FILE    get random bytes from FILE
  -r, --reverse               reverse the result of comparisons
      --sort=WORD             sort according to WORD:
                                general-numeric -g, human-numeric -h, month -M,
                                numeric -n, random -R, version -V
  -V, --version-sort          natural sort of (version) numbers within text
 ```
##### for 循环
```
1、for k in $( seq 1 10);do curl www.baidu.com;done  
2、for ((i=1;i<=30;i=i++));do curl www.baidu.com;done  
3、for k in {1..10};do ping -c 1 www.baidu.com;done
4、for k in `cat /root/aa.txt`;do curl $k ;done 
 
 ```
 
 
##### nslookup和dig
```
查看域名dns用的是那个
nslookup -qt=ns  www.baidu.com

查看域名的ip记录是否有cnd可以用不同的ns进行查看
nslookup www.baidu.com 8.8.8.8 
nslookup www.baidu.com 9.9.9.9

追踪一个dns解析过程
dig +trace www.baidu.com
```


##### 重置windows网络状态
```
netsh interface ipv4 reset
netsh interface ipv6 reset
netsh winsock reset

```
##### 查看机器型号
    dmidecode


##### xz -z 要压缩的文件
```
如果要保留被压缩的文件加上参数 -k ，如果要设置压缩率加入参数 -0 到 -9调节压缩率。如果不设置，默认压缩等级是6

解压
xz -d 要解压的文件

同样使用 -k 参数来保留被解压缩的文件。

创建或解压tar.xz文件的方法
解压：tar Jcvf其中J参数解压.xz文件

创建tar.xz文件：只要先 tar cvf xxx.tar xxx/ 这样创建xxx.tar文件先，然后使用 xz -z xxx.tar 来将 xxx.tar压缩成为 xxx.tar.xz
```
##### 修改windows格式为linux格式

    $ dos2unix filename 
    直接转换成unix格式
    

####  tcpdump 屏蔽端口 
    tcpdump -i eno1  host 192.168.9.106 -nn -vv  and port ! 6622 -w /tmp/kkkk2.pcap

#### arping 查看ip的mac地址
    这个命令是
    arping -I eth0 192.168.9.1 
    
#### xfs 扩容lvm

     xfs_growfs /dev/mapper/vg_mysql0121366-LogVol01
    
    
### tasklist taskkill   
```
这里我们不需要下载任何工具，只要用Windows自带的小助手即可。首先打开命令提示符窗口，输入命令“tasklist /m BackDoorDll.dll”
两种方法删除顽固的DLL文件
tasklist命令

　　这条命令是意思是检测指定名字的文件被哪些进程所调用,从结果可以看出原来DLL病毒文件插入到了进程iexplore.exe 中，此进程ID为3240，那我们现在关闭该进程，用命令taskkill /f /PID 3240，它的意思是强行终止ID号为3240的进程(图3)。当然，我们也可以用任务管理器结束该进程。

两种方法删除顽固的DLL文件
tasklist命令
```
