# Windows 系统检查

## Win查看异常登录ip

在日志中搜索 4648

## 小技巧

```cmd
对应端口 netstat -ano | findstr “port”
查看当前正在的连接 netstat -ano | findstr "ESTABLISHE"


查看对应的程序位置 运行输入 wmic，cmd界面 输入 process

查看运行的服务 tasklist /svc
```

## 查看服务器被远程登录ip

```log
在日志查看器中导出日志为 log.txt格式

然后进行分析

cat log.txt  | grep -E '源网络地址|审核成功' | grep -v -w - | grep '源网络地址:' -B 1 | awk '{print $1,$2,$3}'

提取出具体的ip.txt 然后调用接口进行ip和归属地的匹配发现有异常及时的做进一步检查

from qqwry import QQwry

with open('ip.txt', 'r') as f:
    print(f.readline())

    for line in f.readlines():
        #llip = print(line.strip())
        print(line)

        q = QQwry()
        q.load_file('qqwry.dat')
        print(line)
        result = q.lookup(line)
        print(result)

