# From 
```
http://blog.jobbole.com/54595/

```
#### 一些常用参数
-r 扫描端口的时候按照顺序扫描  
-sP 扫描一个段网络，常用来发现主机  
-n 不解析域名  
-v 详细信息，可以用-vv  
-PA 用tcp 方式发送ack  
-PS 用tcp方式发送syn  
-p 端口如22,23 1-65533  
-exclude 可以排除不想扫描的主机  
-v 详细信息  
-O 操作系统  
-F 快速扫描  
-sS 隐蔽性扫描 但是tcpdump 仍能抓取到数据包  
-sV 选项找出远程主机上运行的服务版本  
-sT 扫描常用的端口
-sN 骗过防火墙

#### 常用扫描方式  
- 1  扫描网段中生存的主机  
```
[root@cs68 ~]# nmap -n -sP 192.168.100.0/24

Starting Nmap 5.51 ( http://nmap.org ) at 2017-01-13 04:05 CST
Nmap scan report for 192.168.100.2
Host is up (0.0023s latency).
MAC Address: 8E:AB:8E:E9:15:40 (Unknown)
Nmap scan report for 192.168.100.7
Host is up (0.0092s latency).
MAC Address: 1C:CD:E5:70:FB:03 (Unknown)
```
- 2 快速扫描一个主机开放的端口  
扫描常见端口，且要查看进度
```

[root@cs68 ~]# nmap  -vv -n -sT 192.168.100.200

Starting Nmap 5.51 ( http://nmap.org ) at 2017-01-13 04:08 CST
Initiating ARP Ping Scan at 04:08
Scanning 192.168.100.200 [1 port]
Completed ARP Ping Scan at 04:08, 0.01s elapsed (1 total hosts)
Initiating Connect Scan at 04:08
Scanning 192.168.100.200 [1000 ports]
Discovered open port 22/tcp on 192.168.100.200
```
扫描指定端口,可以指定区间

```

[root@cs68 ~]# nmap  -n -p 22,80 192.168.100.200

Starting Nmap 5.51 ( http://nmap.org ) at 2017-01-13 04:11 CST
Nmap scan report for 192.168.100.200
Host is up (0.00035s latency).
PORT   STATE    SERVICE
22/tcp open     ssh
80/tcp filtered http
MAC Address: 00:0C:29:F9:9C:73 (VMware)

[root@cs68 ~]# nmap  -n -p 1-200  192.168.100.200

Starting Nmap 5.51 ( http://nmap.org ) at 2017-01-13 04:11 CST
Nmap scan report for 192.168.100.200
Host is up (0.00043s latency).
Not shown: 199 filtered ports
PORT   STATE SERVICE
22/tcp open  ssh
MAC Address: 00:0C:29:F9:9C:73 (VMware)
```
真对防火墙后端口扫描  
```
[root@cs68 ~]# nmap  -n -p 22,65532  192.168.100.200

Starting Nmap 5.51 ( http://nmap.org ) at 2017-01-13 04:12 CST
Nmap scan report for 192.168.100.200
Host is up (0.00026s latency).
PORT      STATE    SERVICE
22/tcp    open     ssh
65532/tcp filtered unknown
MAC Address: 00:0C:29:F9:9C:73 (VMware)

Nmap done: 1 IP address (1 host up) scanned in 0.11 seconds
[root@cs68 ~]# nmap  -sN -n -p 22,65532  192.168.100.200

Starting Nmap 5.51 ( http://nmap.org ) at 2017-01-13 04:13 CST
Nmap scan report for 192.168.100.200
Host is up (0.00027s latency).
PORT      STATE         SERVICE
22/tcp    open|filtered ssh
65532/tcp open|filtered unknown
MAC Address: 00:0C:29:F9:9C:73 (VMware)

Nmap done: 1 IP address (1 host up) scanned in 1.34 seconds


```
查看端口监听的服务
```

[root@cs68 ~]# nmap  -sN  -p 22,65532 -sV  192.168.100.200

Starting Nmap 5.51 ( http://nmap.org ) at 2017-01-13 04:15 CST
Nmap scan report for 192.168.100.200
Host is up (0.00028s latency).
PORT      STATE         SERVICE VERSION
22/tcp    open          ssh     OpenSSH 6.6.1 (protocol 2.0)
65532/tcp open|filtered unknown
MAC Address: 00:0C:29:F9:9C:73 (VMware)

Service detection performed. Please report any incorrect results at http://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 1.80 seconds

``` 
