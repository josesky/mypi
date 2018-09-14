# Ansible 使用

## Ansible 安装

```ansible
# CentOS 7
yum install git python-pip -y
# pip安装ansible(国内如果安装太慢可以直接用pip阿里云加速)
#pip install pip --upgrade
#pip install ansible
pip install pip --upgrade -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
pip install --no-cache-dir ansible -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
```

## Ansible 常见问题

### 报错如下:

/usr/lib/python2.7/site-packages/requests/__init__.py:80: RequestsDependencyWarning: urllib3 (1.22) or chardet (2.2.1) doesn't match a supported version

原因：

python库中urllib3 (1.21.1) or chardet (2.2.1) 的版本不兼容

解决方法：  

pip uninstall urllib3  
pip uninstall  chardet  
pip install requests  