# TarOpenssl 实现文件加密

``` bash

当有重要的敏感数据的时候，给文件和目录额外加一层保护是至关重要的，特别是当需要通过网络与他人传输数据的时候。基于这个原因，
可以用到tar（Linux 的一个压缩打包工具）和OpenSSL来解决的方案。借助这两个工具，你真的可以毫不费力地创建和加密 tar 归档文件。
 
下面介绍使用 OpenSSL创建和加密 tar 或 gz（gzip，另一种压缩文件）归档文件：
牢记使用 OpenSSL 的常规方式是：
# openssl command command-options arguments
 
示例如下：
[root@ipsan-node03 ~]# cd /mnt/
[root@ipsan-node03 mnt]# ls
[root@ipsan-node03 mnt]# echo "123" > a.txt
[root@ipsan-node03 mnt]# echo "456" > b.txt
[root@ipsan-node03 mnt]# echo "789" > c.txt
[root@ipsan-node03 mnt]# ls
a.txt  b.txt  c.txt
 
现在要加密当前工作目录的内容（根据文件的大小，这可能需要一点时间）
[root@ipsan-node03 mnt]# tar -czf - * | openssl enc -e -aes256 -out test.tar.gz
enter aes-256-cbc encryption password:                          //假设这里设置的密码为123456
Verifying - enter aes-256-cbc encryption password:
 
上述命令的解释：
enc 使用加密进行编码
-e  用来加密输入文件的 enc 命令选项，这里是指前一个 tar 命令的输出
-aes256 加密用的算法
-out 用于指定输出文件名的 enc 命令选项，这里文件名是test.tar.gz
 
[root@ipsan-node03 mnt]# ls
a.txt  b.txt  c.txt  test.tar.gz
[root@ipsan-node03 mnt]# rm -rf a.txt
[root@ipsan-node03 mnt]# rm -rf b.txt
[root@ipsan-node03 mnt]# rm -rf c.txt
[root@ipsan-node03 mnt]# ls
test.tar.gz
 
对于上面加密后的tar包直接解压肯定是不行的！
[root@ipsan-node03 mnt]# tar -zvxf test.tar.gz
gzip: stdin: not in gzip format
tar: Child returned status 1
tar: Error is not recoverable: exiting now
 
要解密上述tar归档内容，需要使用以下命令。
[root@ipsan-node03 mnt]# openssl enc -d -aes256 -in test.tar.gz | tar xz -C /mnt/
enter aes-256-cbc decryption password:
[root@ipsan-node03 mnt]# ls
a.txt  b.txt  c.txt  test.tar.gz
 
上述命令的解释：
-d  用于解密文件
-C  将加压后的文件提取到目标目录下
```