Nginx默认是不允许列出整个目录的。如需此功能，打开nginx.conf文件或你要启用目录浏览虚拟主机的配置文件，在server或location 段里添加上autoindex on;来启用目录流量，下面会分情况进行说明。

另外Nginx的目录流量有两个比较有用的参数，可以根据自己的需求添加：

autoindex_exact_size off;
默认为on，显示出文件的确切大小，单位是bytes。
改为off后，显示出文件的大概大小，单位是kB或者MB或者GB

autoindex_localtime on;
默认为off，显示的文件时间为GMT时间。
改为on后，显示的文件时间为文件的服务器时间
