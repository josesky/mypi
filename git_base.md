#  git基础

我需要git来做版本控制

## 安装了gitlab

```docker
sudo docker run --detach \
   --hostname git.centos8.com \
   --publish 443:443 --publish 80:80 --publish 2222:22 \
   --name gitlab \
   --restart always \
   --volume /docker_data/gitlab/config:/etc/gitlab \
   --volume /docker_data/gitlab/logs:/var/log/gitlab \
   --volume /docker_data/gitlab/data:/var/opt/gitlab \
   gitlab/gitlab-ce:latest

# 版本和文件的映射都是先宿主机后容器，就是宿主机的端口映射容器


docker run -d --name gitlab_runner2 --restart always \
 --link gitlab3 \
 -v /docker_data/gitlab_runner/config:/etc/gitlab-runner \
 -v /docker_data/gitlab_runner/docker.sock:/var/run/docker.sock \
 registry.docker-cn.com/gitlab/gitlab-runner

```

## 学习git的相关基础命令

1. 安装git的windows客户端

```git
下载地址：https://git-scm.com/download/win
  安装注意事项：就是安装的时候选择gitbash这种方式。
               换行符的处理上选择“Checkout Windows-style，commit Unix-styleline endings”
```

2. 初始化设置

设置git的邮箱地址

```git
Git global setup
git config --global user.name "josesky"
git config --global user.email "josesky@live.cn"
git config --global color.ui auto

#cat ~/.gitconfig
[user]
        name = josesky
        email = josesky@live.cn

[gui]
        encoding = utf-8
[i18n]
    commitencoding = GB2312 #log编码，window下默认gb2312,声明后发到服务器才不会                                                                                                              乱码
        logoutputencoding = utf-8
[svn]
    pathnameencoding = GB2312 #支持中文路径
[color]
        ui = auto
[alias]
        s = status
        c = commit
        lg = log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%C                                                                                                              reset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
[core]
        quotepath = false
[i18n "commit"]
        encoding = utf-8

```

3. 了解开源界比较牛气的一个站点github.com在这里注册一个域名并设置Ssh Key的形式进行连接。

```git
$ ssh-keygen.exe  -t rsa -C "josesky@live.cn"
一路回车即可
找到网站自己搭建的gitlab上面在setting中找到“SSH Key” 添加
.ssh/id_rsa.pub中的信息(注意：这里是这个文件的中所有信息)

$ ssh -T git@git.centos8.com
Welcome to GitLab, josesky!
说明ssh可以正常连接。
Create a new repository
#克隆一个仓库
git clone git@git.centos8.com:josesky/Hello-World.git
cd Hello-World
touch README.md
#添加文件的版本控制,到缓冲区
git add README.md
#进行提交,并使用-m 添加本次提交的描述。如果不加-m 会打开文本编辑器让你输入。
git commit -m "add README"
#推送master分支到远程。
git push -u origin master

#### 日志和状态

```git

# 用来查看仓库的状态

git status
# 查看提交日志
git  log
git log -pretty=short
git log --pretty=oneline
# 以图表的形式进行显示
git log --graph
git log 只能查看当前状态点为终点的历史日志，这里使用
git reflog 显示当前仓库的所有操作。
>[root@localhost support]# git reflog
>>0cd2b00 HEAD@{0}: checkout: moving from backup to master
>>359569a HEAD@{1}: commit: love you

git log --pretty=oneline --abbrev-commit
$ git log --pretty=oneline --abbrev-commit
5d0f6a2 (HEAD -> master, origin/master) Merge branch 'master' of gitlab.gainet.com:swalf/public
f33151d huangyanqi new
e35169b add work context from hanhailong
8ff6885 changes by wzh
c2b0a56 changes by wzh


# 查看指定目录，文件的日志

git log README.md
# 查看日志带来的改动
git log -p README.md
# 查看更前后的差别为
git diff
# 提交前查看最近的差别,这里的HEAD是最近提交的指针。
git diff HEAD HEAD~2
git diff branch branch1
比较当前和缓冲区的
git diff --cache

##### 查看具体用户提交记录
git log --author="qiaosen"

```

#### 分支

```git 

# 创建分支并切换到分支下
git checkout -b Centos8-A
分开为
git branch Centos8-A
git checkout Centos8-A

查看分支
git branch -a
git branch -d <name> 删除分支
git branch -D <name> 强制删除分支(因分支中没有提交)

# 分支合并
合并分支，先切回master分支，然后为了明确记录本次分支和并我们需要创建和并提交合并时候加上--no-ff
git merge --no-ff -m"这样的合并是有记录的" cao

1. 在同样的文件中修改了同一行的文件。
   a. 合并后提示失败，查看无法合并的文件这个时候会有both modified 编辑文件进行手动修改如果两个都保留的话就删除修改提示后再次提交。
   b. 在合并就可以了。
2. 分支的推送时候的冲突
   a. git push origin cao
   b. 推送失败是因为远程比你本地的更新，这个时候要先下载远程的git pull
   c. There is no tracking information for the current branch. 这个是需要先进本地分支和远程分支的关联
   git branch --set-upstream cao  origin/cao
   d. 如果合并有冲突，则解决冲突，并在本地提交，没有冲突或者解决掉冲突后，再用git push origin branch-name推送就能成功

```

#### 回溯历史版本

```git

git reset
要让仓库的HEAD、暂存区、当前工作树回溯到指定的状态需要使用
git reset --hard HEAD^ 回退到上个版本。
git reset --hard HEAD~10 会退到前10个版本
git reset --hard 359569a 需要具体标时间点的哈希值。

场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令git checkout -- file。
git checkout其实是用版本库里的版本替换工作区的版本，无论工作区是修改还是删除，都可以“一键还原”。

场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步:
第一步用命令git reset HEAD file
第二步用命名git checkout file

```


#### 修改提交信息

git commit -amend

压缩历史发现历史版本中有拼写错误的，在进行commit 提交的是有点尴尬这是就可以用这个压缩为一个历史
git rebase -i
临近的使用
git rebase -i HEAD~2
在编辑器中会有两个pick把不需要的那个提交该为fixup

### git alias

```git 

$ git config --global alias.co checkout
$ git config --global alias.ci commit
$ git config --global alias.br branch

git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

```

#### 仓库初始化及配置

```git

Existing folder
cd existing_folder
git init
# 设置本的仓库的远程仓库。
git remote add origin git@git.centos8.com:josesky/Hello-World.git
git add .
git commit -m "Initial commit"
git push -u origin master

Existing Git repository
cd existing_repo
git remote rename origin old-origin
git remote add origin git@git.centos8.com:josesky/Hello-World.git
推送至远程仓库
git push -u origin master
-u 是在推送的同时将origin仓库的master分支设置为本地仓库当前分支的upstream（上游）
git push -u origin feature-D
git push -u origin --all 推送所有分支到远程
git push -u origin --tags


拉取远程仓库的分支
git pull origin feature-D

```

#### 忽略文件和路径

```git 

.gitignore来忽略一些不需要提交的文件

-   可以在前面添加 / 来避免递归
   /tianxia 仅在当前目录下忽略天下文件夹，但是不包括josesky/tianxia 文件夹
-   使用在后面添加/ 来忽略文件下所有文件
       tianxia/   忽略天下文件夹下所有文件
-   ！来进行否定忽略 *.apk 人后！mm.apk 则这个文件mm.apk不被忽略
-   \* 用来匹配零个或多个字符，如*.[oa]忽略所有以".o"或".a"结尾，*~忽略所有以~结尾的文件（这种文件通常被许多编辑器标记为临时文件）；[]用来匹配括号内的任一字符，如[abc]，也可以在括号内加连接符，如[0-9]匹配0至9的数；?用来匹配单个字符。

```

#### 远程仓库相关命令

```git

检出仓库：$ git clone git://github.com/josesky/jquery.git
查看远程仓库：$ git remote -v
添加远程仓库：$ git remote add [name] [url]
删除远程仓库：$ git remote remove
拉取远程仓库：$ git pull [remoteName] [localBranchName]
推送远程仓库：$ git push [remoteName] [localBranchName]
如果想把本地的某个分支test提交到远程仓库，并作为远程仓库的master分支，或者作为另外一个名叫test的分支，如下 :

$git push origin test:master         // 提交本地test分支作为远程的master分支
$git push origin test:test              // 提交本地test分支作为远程的test分支

删除分支：$ git branch -d [name] ---- -d选项只能删除已经参与了合并的分支，对于未有合并的分支是无法删除的。如果想强制删除一个分支，可以使用-D选项
合并分支：$ git merge [name] ----将名称为[name]的分支与当前分支合并
创建远程分支(本地分支push到远程)：$ git push origin [name]
删除远程分支：$ git push origin :heads/[name] 或 $ gitpush origin :[name]
创建空的分支：(执行命令之前记得先提交你当前分支的修改，否则会被强制删干净没得后悔)**

#### 版本(tag)操作相关命令
查看版本：$ git tag
创建版本：$ git tag [name]
删除版本：$ git tag -d [name]
查看远程版本：$ git tag -r
创建远程版本(本地版本push到远程)：$ git push origin [name]
删除远程版本：$ git push origin :refs/tags/[name]
合并远程仓库的tag到本地：$ git pull origin --tags
上传本地tag到远程仓库：$ git push origin --tags
创建带注释的tag：$ git tag -a [name] -m 'yourMessage'
给之前的提交创建分支
git tag -a tianxia -m 'tianxia2' 7747abd

在仓库根目录下创建名称为“.gitignore”的文件，写入不需要的文件夹名或文件，每个元素占一行即可，如下：
# Maven
target/
../target
target/*
*.class
*.ser
*.ec
.metadata/

```



```git 

git stash 隐藏当前工作区,改动数据
git pull
git stash list
git stash pop

一是用git stash apply恢复，但是恢复后，stash内容并不删除，你需要用git stash drop来删除；

另一种方式是用git stash pop，恢复的同时把stash内容也删了：

```

#### 查看文件所有行的改动

git blame README  
git blame file

##### 查看具体用户提交记录

git log --author="qiaosen"
