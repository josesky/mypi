# webhooks 

当想push 的时候直接执行。需要使用webhook

## 选用一个webhooks

https://github.com/adnanh/webhook

## 进行简单配置

```config
[
  {
    "id": "mypi",
    "execute-command": "/var/scripts/redeploy.sh",
    "command-working-directory": "/data/mypi"
  }
]

```

## 进行系统上命令执行

```config
root@SS:/var/scripts# cat redeploy.sh
#!/bin/sh

cd /data/mypi

git pull
```

## 在github进行配置

https://github.com/josesky/mypi/settings/hooks

添加一个webhook

然后输入之前配置的http://centos8.com:9000/hooks/mypi
然后就可以了。

## 验证

在自己的机器上查看一下修改的内容看是否已经改变。如果改变，恭喜流程走通了。

如果没有通过开启webhook的冗余日志进行查看,分析错误原因。

## 注意

````config
[
  {
    "id": "mypi",
    "execute-command": "/var/scripts/redeploy.sh",
    "command-working-directory": "/data/mypi"
  }
]
```

其中执行目录要对应，id也要进行对应。

http://centos8.com:9000/hooks/mypi