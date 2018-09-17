
### 关于CRLF
```
[root@zz_t_zz_nginx01 ~]# file tomcat8.sh
tomcat8.sh: Bourne-Again shell script, UTF-8 Unicode text executable
[root@zz_t_zz_nginx02 ~]# file tomcat8.sh
tomcat8.sh: Bourne-Again shell script, UTF-8 Unicode text executable, with CRLF line terminators

CRLF的意思
就是回车(CR, ASCII 13, \r) 换行(LF, ASCII 10, \n)。
换行字符可以看作是行的结束符，也可以看作行之间的分隔符，这两种处理方式之间存在一些歧义。
下面列出各系统换行字元编码的列表
LF：在Unix或Unix相容系统（GNU/Linux，AIX，Xenix，Mac OS X，...）、BeOS、Amiga、RISC OS
CR+LF：DOS（MS-DOS、PC-DOS等）、微软视窗操作系统（Microsoft Windows）、大部分非Unix的系统

yum -y install doc2unix

[root@zz_t_zz_nginx02 ~]# doc2unix tomcat8.sh

```
