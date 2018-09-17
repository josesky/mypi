### 必须要掌握的命令
1、进程的暂停和启用
```
查看kill 所有的参数使用 kill -l
kill -STOP [pid]  kill -19 【pid】  
发送SIGSTOP (19)停止一个进程，而并不消灭这个进程。

注意暂停进程的状态是【Ts】
kill -CONT [pid]   kill -18 【pid】 发送SIGCONT (18)重新开始一个停止的进程。
```
2、踢掉正在远程的终端
```
pkill -kill -t pts/0
```

4、netstat 只显示：80 绝对显示
```
netstat -anp  | grep "\<80\>"  
查看链接数  
netstat -st | grep conn  
不过这个命令会被ss所代替
```
5、添加网卡的路由
```
[root@pp network-scripts]# vi /etc/sysconfig/network-scripts/route-eth0  
10.0.0.0/8 via 10.200.0.1
命令行下添加：
ip route add 10.0.0.0/8 via 10.200.0.1
ip route del default gw 10.88.88.1
```

6、查看最近所有用户登录时间
```
[root@pp network-scripts]# lastlog
$sername         Port     From             Latest    
root             pts/1    192.168.100.110  Thu Apr 14 00:40:18 +0800 2016    


查看所有ip的暴力扫描root账号的记录
lastb root | awk '{print $3}' | sort -rn | uniq -c | more
awk -F ：
sort 默认是按照升序排列的，-r 是倒序排列，-n 是按照数值大小排序。 -t是使用那些字符进行分割  -k 是已第几行进行排序。
[root@vpn ~]# sort  -t ":" -k 2 -n -r  /tmp/aa.txt
pear:90:2.3
banana:30:5.5
orange:20:3.4
apple:10:2.5

uniq 它一般会和sort命令进行组合使用，因为uniq 不会检查重复的行，除非它们是相邻的行。
 -c, --count              //在每行前加上表示相应行目出现次数的前缀编号  
 -d, --repeated          //只输出重复的行  
 -D, --all-repeated      //只输出重复的行，不过有几行输出几行
```


7、查看硬件信息
```
dmesg查看系统启动命令
dmesg | grep error 来查看系统启动硬件报错。

```
8、例如dig这个命令通常有些最小化安装的时候没有安装

```
[root@cs68 ~]# yum provides */dig | more
dig 命令来查看域名解析的  
dig @8.8.8.8 www.baidu.com 使用指定dns服务器来进行域名解析。  
dig www.baidu.com +trace     追踪域名解析的过程。  
dig -6 www.baidu.com             用ipv6 解析  
dig -x 116.255.12.12 反向解析ip  
dig @8.8.8.8 -t ns zzidc.com 查看这个域名的ns记录。  
dig + tcp www.baidu.com
```


9、 查看登陆成功的记录
cat /var/log/secure | grep Accepted

10、namp常用
```
nmap -T4 -A -v 192.168.55.11
A主机发现，端口扫描，应用程序，版本侦测，操作系统识别。
T4 0~5 级别越高，扫描速度越快
-v 参苏可以显示扫描细节
-sn 对主机进行发现扫描，不进行端口扫描  -sn 192.168.55.*
```

11、查看当前系统里面 比较大前三个文件或目录
```
du -sh  /*  | sort -nr | head -3
du -csh /* | sort -rn | head -n 10
也可以用这个
find / -type f -size +10M | more
```


14、系统之间传输
```
lrzsz
rz windows --》 linux
rz recive
sz wenjian.txt --> windows
source
```

15、ssh 运行root登陆。需要改两个地方。第一是修改允许root登陆。允许密码验证。
```
允许root用户登陆
PermitRootLogin yes
允许密码验证
PasswordAuthentication yes

```

16、去掉里面的#和空格
```
：.,$s/^\([[:space:]]*\)#/\1/g

```

17、变量a='a/b/c' 怎么取c
```
echo $a |cut -d '/' -f 3
-d ：自定义分隔符，默认为制表符。
-f ：与-d一起使用，指定显示哪个区域。

echo $a |awk -F'/' '{print$3}'

```

19、查看进程树命令(cs7默认没有)
```
pstree
pstree -a
```

20、centos安装epel的yum源
```
yum search epel
yum -y install epel-release
```

21、把用户加入到一个组中 把天下加入root组
```
usermod -G root tianxia
```


23、ping 加时间
```
while true; do ping -c 1 www.weather.com.cn | awk '{print "["strftime("%F %H:%M:%S")"]:"$0}' |grep from >> ping.log;sleep 1; done &
```



25、modprobe -r 是用来删除模块的
```
        modprobe -l | grep ipvs
        lsmod            |grep ipvs
```

26、find 查找1天内修改的文件  
```
atime 访问 ctime 权限更改  mtime 修改内容  
    find ./* -mtime  -1  | xargs cp -v /opt
    find ./* -mtime  -2 -exec cp -v {} /opt \
    find  / -mtime -20 | cpio -admvp /tmp
    find . -regextype posix-egrep -mindepth 1 ! -regex './(dev|tmp)($|/.*)' ! -name Makefile -a ! -name .svn | cpio -admvp /home/dir2
find 的 -regextype 参数指定正则表达式类型，posix-egrep 为 egrep 用的扩展正则表达式，-mindepth 使 find 的输出中不包括目录本身，-regex 参数指定过滤的文件的正则表达式，-regex 前面的感叹号表示跳过，'./(dev|tmp)($|/.*)' 这个正则表达式即表示跳过目录中的第一层 dev 和 tmp 目录以及下面所有的文件和文件夹，最后两个 -name 指定要跳过文件名为 Makefile 和 .svn 的文件，这样在备份版本库的时候非常有用。
cpio 命令将 find 的输出文件列表依次拷贝到 /home/dir2 目标目录中，-a 表示不更新文件的访问时间，-d 指定自动创建目录，-m 指定保留文件的修改时间，-p 指定 cpio 工作在 Copy-pass 模式，这是专门用来拷贝目录树的一种模式。
    拒绝相应的路径
    find / -name iptables ! -path "/etc/sysconfig"
    打包时候跳过目录
tar -jcvf tomcat.tar.bz2 --exclude=tomcats/tomcat8082/logs --exclude=tomcats/tomcat8083/logs tomcats/
注意：要打的包必须要在命令最后不然没效果。
将 /etc/ 内的所有文件备份下来，并且保存其权限！
tar -zxvpf /tmp/etc.tar.gz /etc
#这个 -p 的属性是很重要的，尤其是当您要保留原本文件的属性时！
在 /home 当中，比 2010/06/01 新的文件才备份
tar -N '2010/06/01' -zcvf home.tar.gz /home
备份 /home, /etc ，但不要 /home/dmtsai
tar --exclude /home/dmtsai -zcvf myfile.tar.gz /home/* /etc


find /var/log/* -name "secure*" -exec cp -v {} /tmp/ \;

-I 必须指定替换字符　－i 是否指定替换字符-可选
find /var/log/* -name "secure*" | xargs -I {} cp -v {} /tmp/

find /var/log/* -name "secure*" | xargs -i  cp -v {} /tmp/
控制目录深度:
[root@localhost ~]# find / -maxdepth 3 -name "*.log"
/var/log/boot.log
/var/log/yum.log


find / -path "/sys" -prune -o  -mtime -1
忽略的目录为
“-path "/sys" -prune -o ”
如果要忽略两个以上的路径如何处理？
find /home/carryf /( -path "/home/carryf/astetc" -o -path "/home/carryf/etc" /) -prune -o -type f  -print

find /home/carryf /( -path "/home/carryf/astetc" -o -path "/home/carryf/etc" /) -prune -o -type f  -name "cdr_*.conf" -print

    grep 查询的跳过
    grep -r ipv4 --exclude-dir=/sys

```

27、需要有程序的思维
```
for i in {0..9};do mv ./$i* /upload/;done
for i in
```

28、Linux下查看某个目录下的文件、或文件夹个数用到3个命令:ls列目录、用grep过虑、再用wc统计。
举例说明：
```
1、查看统计当前目录下文件的个数
　　ls -l | grep "^-" | wc -l
2、查看统计当前目录下文件的个数，包括子目录里的。
　　ls -lR| grep "^-" | wc -l
3、查看某目录下文件夹(目录)的个数，包括子目录里的。
　　ls -lR| grep "^d" | wc -l
````

29、curl
```
-o：将文件保存为命令行中指定的文件名的文件中
-O：使用URL中默认的文件名保存文件到本地

 将文件下载到本地并命名为mygettext.html
curl -o zzidc.l http://www.zzidc.com/

 将文件保存到本地并命名为gettext.html
curl -O http://www.zzidc.com/

```

30、top中的cpu查看可以按1查看多个cpu的运行情况。
```
find /var/log/ -size +10k -type f -print0 | xargs -0  ls -Ssh | sort  -z
```

32、添加多端口
```
iptables -A INPUT -s 10.153.0.105/32 -p tcp -m multiport --dports 4888,10009,10011,8890,9990 -m comment --comment "vps_cloud_yunweipingtai" -j ACCEPT
```

数据库查看二进制文件
```
 mysqlbinlog  --base64-output=decode-rows -v   --start-date='2017-04-26 15:20:00' --stop-date='2017-04-26 15:22:00' /tmp/mysql-bin.000010
```

31、pstree 以梳状结构显示进程。
```
    统计线程数：
    [root@cs68-template ~]# pstree -u mysql
    mysqld───75*[{mysqld}]
    显示很多：
    [root@cs68-template ~]# pstree -p mysql
    mysqld(32602)─┬─{mysqld}(32603)
              ├─{mysqld}(32606)
              ├─{mysqld}(32607)

    ps -Lf 32602显示多个启动线程
    [root@cs68-template ~]#  ps -Lf 32602 | more
UID        PID  PPID   LWP  C NLWP STIME TTY      STAT   TIME CMD
mysql    32602 32079 32602  0   77 18:33 pts/2    Sl     0:01 /usr/local/mysql/bin/mysqld --basedir=/usr/local/mysql --datadir=/data/mydb -
-plugin-dir=/usr/local/mysql/lib/plugin --user=mysql --log-error=/data/mydb/mysql_52_error.log --open-files-limit=65533 --pid-file=/data/my
db/mysql_52.pid --socket=/tmp/mysql.sock --port=3306

    pstack显示每个进程的栈跟踪
    [root@cs68-template ~]# pstack  32602 | more
Thread 77 (Thread 0x7f5440526700 (LWP 32603)):
#0  0x00007f5449862817 in sigwaitinfo () from /lib64/libc.so.6
#1  0x0000000000f1e7fb in timer_notify_thread_func ()
#2  0x0000000000f2fbd1 in pfs_spawn_thread ()
#3  0x00007f544affeaa1 in start_thread () from /lib64/libpthread.so.0
#4  0x00007f5449917aad in clone () from /lib64/libc.so.6
```

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
