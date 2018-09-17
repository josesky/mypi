### lvm磁盘卷组
#### 创建lvm分区
1. 使用fdsik /dev/vdb创建一个分区
2. pvcreate /dev/vdb1 来创建一个逻辑卷组。
3. 使用vgcreate 创建一个名为vg_ansible卷组  vgcreate vg_ansible /dev/vdb1
4. 创建一个lv_ansible的分区
  1. 使用vgdisplay 查看到Free的PE
  2. lvcreate -l 2559 -n lv_ansible vg_ansible
5. 先格式化一下 mkfs.xfs /dev/vg_ansible/lv_ansible


#### LVM分区扩容
1. 先fdisk /dev/vdb 创建一个分区
2. partprobe  让新的分区被识别
3. pvcreate /dev/vdb2
4. vgextend vg_ansible /dev/vdb2
5. 使用vgdisplay 查看到Free的PE
6.  lvextend -l +7679  /dev/vg_ansible/lv_ansible  
    lvextend -L +3G /dev/vg_ansible/lv_ansible
7. xfs_growfs /dev/mapper/vg_ansible-lv_ansible

#### LVM 快照
##### 使用dd命令进行备份
1. 取消当前分区的挂载避免数据被写入
2. dd 当前分区到新的硬盘
  1. #dd if=/dev/mapper/lv_data  of=/dev/vdc
  2. 直接这种方式的话会经历漫长的等待到奔溃。
    1. 怎么能看到dd进度
      watch -n 5 pkill -URS1 ^dd$
      这种可以看到dd的进度
    2. 怎么能快些
      因为默认的话是1024字节,或者更大 4096
      #dd if=/dev/mapper/lv_data  of=/dev/vdc bs=1024k
      使用dd命令把本机硬盘8G的东西倒到另有一块硬盘/temp目录下面的systemos.img成一个文件
      dd if=/dev/sda of=/temp/systeoms.img bs=1024k
      使用dd命令把systemos.img倒入到这台机器
