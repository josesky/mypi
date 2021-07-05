# shell 的判断

[ -z string ] “string”的长度为零则为真 
[ -n string ] or [string] “string”的长度为非零non-zero则为真

## shell 参数传递 

```shell
root@server6:~# cat tt.sh
#!/bin/bash

echo "Shell 传递参数实例！";
echo "执行的文件名：$0";
echo "第一个参数为：$1";
echo "第二个参数为：$2";
echo "第三个参数为：$3";
echo "传递脚本参数个数：$#";
echo "以一个字符串显示所有参数传递：$*";
echo "PID：$$";
echo "返回每个独立参数：$@";
echo "命令退出时候的状态：$?";

echo "-- \$* 演示 ---"
for i in "$*"; do
    echo $i
done

echo "-- \$@ 演示 ---"
for i in "$@"; do
    echo $i
done
root@server6:~# bash tt.sh 1 2 3
Shell 传递参数实例！
执行的文件名：tt.sh
第一个参数为：1
第二个参数为：2
第三个参数为：3
传递脚本参数个数：3
以一个字符串显示所有参数传递：1 2 3
PID：3133101
返回每个独立参数：1 2 3
命令退出时候的状态：0
-- $* 演示 ---
1 2 3
-- $@ 演示 ---
1
2
3

```