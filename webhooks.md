# webhooks 

当想push 的时候直接执行。需要使用webhook

## 选用一个webhooks

https://github.com/adnanh/webhook

## 进行简单配置

```config
root@SS:/var/scripts# cat hooks.json
[
  {
    "id": "opt-tools",
    "execute-command": "/var/scripts/redeploy.sh",
    "command-working-directory": "/data/opt-tools"
  }
]
```

## 进行系统上命令执行

```config
root@SS:/var/scripts# cat redeploy.sh
#!/bin/sh

cd /data/opt-tools

git pull
```

## 在github进行配置

https://github.com/josesky/mypi/settings/hooks

添加一个webhook

然后输入之前配置的http://centos8.com:9000/hooks/redeploy-webhook
然后就可以了。

## 验证

在自己的机器上查看一下修改的内容看是否已经改变。如果改变，恭喜流程走通了。