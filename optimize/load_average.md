# load average  

平均负载：是单位时间内，系统处于可运行状态(Running)和不可以中断状态(Disk sleep)的平均进程数，也就是平均活跃进程数。

## 平均负载不单单指的是cpu的使用率

平均负载包括正在使用的cpu的进程，还包括等待cpu和等待I/O的进程举个例子：

- CPU 密集型，使用大量的cpu资源导致平均负载升高，这个时候CPU平均负载对应一致
- I/O 密集型，等待I/O导致平均负载比较高，这个时候CPU也可能不高，这个不是完全对应
- 等待CPU的进程调度也会导致平均负载升高，此时CPU使用率也会比较高
  
## 实战分析

准备软件包 stress 和 sysstat [mpstat pidstat]

- stress-ng 是一个系统级的压测工具
- mpstat 多核心cpu分析工具
- pidstat 进程性能分析工具，可以看到进程的cpu，内存，I/O，上下文切换


stress-ng -i 1 --hdd 1 --timeout 600（--hdd表示读写临时文件）

mpstat -p ALL 5 
>-P ALL 表示监控所有 CPU，后面数字 5 表示间隔5秒钟输出一组数据  

```mpstat 
12:29:23 AM  CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
12:29:25 AM  all   89.67    0.00   10.33    0.00    0.00    0.00    0.00    0.00    0.00    0.00
12:29:25 AM    0   84.77    0.00   15.23    0.00    0.00    0.00    0.00    0.00    0.00    0.00
12:29:25 AM    1   94.53    0.00    5.47    0.00    0.00    0.00    0.00    0.00    0.00    0.00

```

pidstat -p 24096 -u 2  
>具体的进程pid 间隔5s 输出一组数据，如果不加入会打印所有的活动的进程

```pidstat
12:36:38 AM   UID       PID    %usr %system  %guest    %CPU   CPU  Command
12:36:40 AM     0     24096   16.42    0.00    0.00   16.42     0  stress-ng-cpu
12:36:42 AM     0     24096   20.50    0.00    0.00   20.50     1  stress-ng-cpu
12:36:44 AM     0     24096   26.87    0.00    0.00   26.87     1  stress-ng-cpu
12:36:46 AM     0     24096   18.00    0.00    0.00   18.00     1  stress-ng-cpu
12:36:48 AM     0     24096   20.90    0.00    0.00   20.90     1  stress-ng-cpu
```
