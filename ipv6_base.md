# Centos7/8配置ipv6

## 检查主机上是否已经开启对ipv6的支持

```ipv6
[root@localhost tmp]# sysctl -a | grep ipv6.*disable |grep net
net.ipv6.conf.all.disable_ipv6 = 0
net.ipv6.conf.default.disable_ipv6 = 0
net.ipv6.conf.eth0.disable_ipv6 = 0
net.ipv6.conf.eth1.disable_ipv6 = 0
net.ipv6.conf.lo.disable_ipv6 = 0
```
如果出现的是以上情况证明主机的ipv6是默认开启支持的。因为我们这边搜索的是disable

如果默认是1这个要进行修改使其永久生效

```
vi /etc/sysctl.conf | grep ipv6
net.ipv6.conf.all.disable_ipv6 = 1     
net.ipv6.conf.default.disable_ipv6 = 1 

重载/etc/sysctl.conf 使文件内容生效
sysctl -p
```

### 临时开启主机的ipv6支持

sysctl net.ipv6.conf.[interface].disable_ipv6 = 1       
sysctl net.ipv6.conf.default.disable_ipv6 = 1

## 配置永久生效的ipv6地址

/etc/sysconfig/network-scripts/ifcfg-eth0

```ipv6
IPV6INIT=yes
IPV6_AUTOCONF=no
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
IPV6ADDR=2400:A480:F200:0080:00D6:0000:0000:0076/64
IPV6_DEFAULTGW=2400:A480:F200:0080:0000:0000:0000:0001
```
配置ipv6 dns

echo >> /etc/resolv.conf

nameserver 2001:4860:4860::8888

重启使其生效

systemctl restart network

## 测试是否正常

```ping
[root@localhost tmp]# ping6 ipv6.tsinghua.edu.cn
PING ipv6.tsinghua.edu.cn(2402:f000:1:881::8:205 (2402:f000:1:881::8:205)) 56 data bytes
64 bytes from 2402:f000:1:881::8:205 (2402:f000:1:881::8:205): icmp_seq=1 ttl=55 time=12.1 ms
64 bytes from 2402:f000:1:881::8:205 (2402:f000:1:881::8:205): icmp_seq=3 ttl=55 time=11.0 ms


[root@localhost tmp]# ping6 2620:119:35::35
PING 2620:119:35::35(2620:119:35::35) 56 data bytes
64 bytes from 2620:119:35::35: icmp_seq=1 ttl=50 time=183 ms
64 bytes from 2620:119:35::35: icmp_seq=2 ttl=50 time=183 ms

```


### open dns

2620:119:35::35

2620:119:53::53


2001:4860:4860::8888
2001:4860:4860::8844

