# pure-ftpd

### 安装
> yum install pure-ftpd

### 创建账号

```
groupadd zzuser
useradd zzuser -g zzuser -d /Date/zzuser -s /sbin/nologin
pure-pw useradd zzuser -u zzuser -g zzuser -d /Date/zzuser/

 ```


#### 这个时候一定不能忘记了使用
 >pure-pw mkdb 
