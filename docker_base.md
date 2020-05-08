# Docker network and Firewalld

>基础不牢地动山摇


## Docker 安装

操作系统：CentOS Linux release 8.1.1911 (Core)

### 卸载之前版本

```uninstall
sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine
```

### 使用yum仓库进行安装

- 通过使用yum-utils 来设置标准仓库

yum install -y yum-utils

- 添加docker的yum仓库

sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo

- 安装dokcer引擎

sudo yum install docker-ce docker-ce-cli containerd.io

安装的时候会有一下报错：
> package docker-ce-3:19.03.8-3.el7.x86_64 requires containerd.io >= 1.2.2-3, but none of the providers can be installed
yum install -y https://download.docker.com/linux/centos/7/x86_64/stable/Packages/containerd.io-1.2.6-3.3.el7.x86_64.rpm

安装后就可以正常安装了。

- 选择自己需要安装的版本

[root@lk-office ~]# yum list docker-ce --showduplicates | sort -r
Installed Packages
Extra Packages for Enterprise Linux Modular 8 - 1.1 kB/s | 7.4 kB     00:06
Extra Packages for Enterprise Linux 8 - x86_64  8.3 kB/s | 9.8 kB     00:01
docker-ce.x86_64    3:19.03.8-3.el7                            docker-ce-stable
docker-ce.x86_64    3:19.03.8-3.el7                            @docker-ce-stable
docker-ce.x86_64    3:19.03.7-3.el7                            docker-ce-stable
docker-ce.x86_64    3:19.03.6-3.el7                            docker-ce-stable
docker-ce.x86_64    3:19.03.5-3.el7                            docker-ce-stable
docker-ce.x86_64    3:19.03.4-3.el7                            docker-ce-stable

yum install docker-ce-<VERSION_STRING> docker-ce-cli-<VERSION_STRING> containerd.io

### 把自己的单用户加入docker组里面

usermod -aG docker tianxia

## Docker 默认自带网络

docker 安装完毕后自带三种网络模式

```network
[root@hk zones]# docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
12d77be5854e        bridge              bridge              local
b39a62a2dedc        host                host                local
5002c1a90b3c        none                null                local
```

- bridge ：如果没有指定网络驱动类型默认就是这种。当应用程序在需要通信的独立容器运行的时候，通常使用桥接这种方式
- host ：这种是可以直接使用宿主机的网络的。
- none ：没有任何网络。通常用于自定义的网络中。

- overlay ：
- macvlan ：
- network plugins：

## firewalld -nat

```firewalld
[root@hk zones]# iptables -t nat -nvL
Chain PREROUTING (policy ACCEPT 27048 packets, 1175K bytes)
 pkts bytes target     prot opt in     out     source               destination
 8366  340K DOCKER     all  --  *      *       0.0.0.0/0            0.0.0.0/0            ADDRTYPE match dst-type LOCAL

Chain INPUT (policy ACCEPT 2190 packets, 119K bytes)
 pkts bytes target     prot opt in     out     source               destination

Chain POSTROUTING (policy ACCEPT 3936 packets, 283K bytes)
 pkts bytes target     prot opt in     out     source               destination
    0     0 MASQUERADE  all  --  *      !docker0  172.17.0.0/16        0.0.0.0/0

Chain OUTPUT (policy ACCEPT 3936 packets, 283K bytes)
 pkts bytes target     prot opt in     out     source               destination
    0     0 DOCKER     all  --  *      *       0.0.0.0/0           !127.0.0.0/8          ADDRTYPE match dst-type LOCAL

Chain DOCKER (2 references)
 pkts bytes target     prot opt in     out     source               destination
    0     0 RETURN     all  --  docker0 *       0.0.0.0/0            0.0.0.0/0
```

### 转发非docker0 口出去的数据包

>MASQUERADE  all  --  *      !docker0  172.17.0.0/16        0.0.0.0/0 

把不是docker0接口流量发出的且ip段是172.17.0.0/16 的ip进行伪装，发出去。

## 自定义网络

可以自己定义自己的网络，这里看下相互之间是隔离的

>docker network create --driver bridge --getway 192.168.2.1 --subnet 192.168.2.0/24 net_bridge_2.0

>docker network create --driver bridge --getway 192.168.1.1 --subnet 192.168.1.0/24 net_bridge_1.0

我们可以创建自定义网络的镜像

 docker run -tid --network=net_bridge1.0 --ip 192.168.1.2 --name=busybox1.2 busybox

```firwall
Chain DOCKER-ISOLATION-STAGE-1 (1 references)
 pkts bytes target     prot opt in     out     source               destination
    0     0 DOCKER-ISOLATION-STAGE-2  all  --  br-7ab21d7c9bfc !br-7ab21d7c9bfc  0.0.0.0/0            0.0.0.0/0
    0     0 DOCKER-ISOLATION-STAGE-2  all  --  br-6d74f3bbb767 !br-6d74f3bbb767  0.0.0.0/0            0.0.0.0/0
    0     0 DOCKER-ISOLATION-STAGE-2  all  --  docker0 !docker0  0.0.0.0/0            0.0.0.0/0

Chain DOCKER-ISOLATION-STAGE-2 (3 references)
 pkts bytes target     prot opt in     out     source               destination
    0     0 DROP       all  --  *      br-7ab21d7c9bfc  0.0.0.0/0            0.0.0.0/0
    0     0 DROP       all  --  *      br-6d74f3bbb767  0.0.0.0/0            0.0.0.0/0
    0     0 DROP       all  --  *      docker0  0.0.0.0/0            0.0.0.0/0
```

网络之间相互隔离的


查看docker 网络详细信息使用 
docker network inspect net_bridge_2.0

```net
{
        "Name": "net_bridge_2.0",
        "Id": "7ab21d7c9bfc28052b50cd9a8e479606a6d6667eb261a2abaaebbe78f408aa05",
        "Created": "2020-04-22T18:09:28.685470516+08:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "192.168.2.0/24",
                    "Gateway": "192.168.2.1"
                }
            ]
        },
```

## docker与firewall互动

docker启动后参数中如果加了端口映射,就会自动将端口开放给所有网络设备访问,这种情况下即使在本机的系统防火墙中加规则也无效, 因为docker会自动添加一个优先级最高的针对这个映射端口全开放规

>给docker的启动服务添加"--iptables=false"参数, 禁止docker去操作防火墙




https://access.redhat.com/documentation/zh-cn/red_hat_enterprise_linux/7/html/security_guide/sec-using_firewalls#sec-Start_firewalld
