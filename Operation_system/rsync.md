# rsync 同步yum源
#### rsync 同步时候的目录
```
rsync -avz /etc/ /tmp  是吧etc目录下的文件同步过来了
rsync -avz /etc  /tmp  是把etc这个目录在下面创建了/tmp/etc
```
#### 默认情况下的特性
1. 读取源文件和目的文件不一样就出发更新
2. 不会同步modify time 会记录到新创建时候的time
3. 不太关注目的端的文件权限，如果目的端没有这个文件和源端一直，有的话文件权限不会变。
4. 想一直的话尽量用root来进行

#### 一些选项
```
-t, --times
              This  tells  rsync  to  transfer modification times along with the files and update them on the remote system.  Note that if this option is not used, the
              optimization that excludes files that have not been modified cannot be effective; in other words, a missing -t or -a will  cause  the  next  transfer  to
              behave  as  if  it  used  -I, causing all files to be updated (though rsync’s delta-transfer algorithm will make the update fairly efficient if the files
              haven’t actually changed, you’re much better off using -t).
1. -t 主要是同步远程的时间，主要是比较时间戳和文件大小
2. 可能会出现时间戳和文件大小一样但是内容不一样的情况
3. 这个时候就用到了 -I

-I, --ignore-times          don't skip files that match in size and mod-time
1.会挨个发起文件同步
2.比较慢
3.目的目录的文件时间为同步的当前时间
4.目录的时间不变

-z, --compress              compress file data during the transfer
传输过程压缩
-g group
-o owner

--delete 按照源端的情况，如果源端没有目的端删除
  -n (-n) to see what files would be deleted to make sure

  [root@localhost tmp]# rsync -rv --delete -n /etc/yum.repos.d/ /tmp/yum.repos.d/
  sending incremental file list
  ***deleting .updated****
  CentOS-Base.repo
  CentOS-Base.repo.backup


  --exclude=PATTERN       exclude files matching PATTERN
  --exclude-from=FILE     read exclude patterns from FILE
  --include=PATTERN       don't exclude files matching PATTERN
  --include-from=FILE     read include patterns from FILE
  --files-from=FILE       read list of source-file names from FILE

这些是忽略同步的 也可以使用一个文件把列表列出来


-P                          same as --partial --progress
断了续传

-r, --recursive             recurse into directories

-a, --archive               archive mode; equals -rlptgoD (no -H,-A,-X)

```
