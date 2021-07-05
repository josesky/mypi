# tmux使用

## 配置文件

可以把自己定义的配置文件放在~/.tmux.conf

```conf
# Start windows and panes at 1, not 0
set -g  base-index 1
setw -g pane-base-index 1

# allow mouse to scroll the screen

#set -g mouse on

set -g mouse on
set -g terminal-overrides 'xterm*:smcup@:rmcup@'

# List of plugins
#set -g @plugin 'tmux-plugins/tpm'
#set -g @plugin 'tmux-plugins/tmux-sensible'
#set -g @plugin 'tmux-plugins/tmux-resurrect'
#set -g @plugin 'tmux-plugins/tmux-yank'

# Initialize TMUX plugin manager (keep this line at the very bottom of tmux.conf)
#run -b '~/.tmux/plugins/tpm/tpm'

# copy to os true
# You must install xsel or xclip

tmux_conf_copy_to_os_clipboard=true

```

## 配置生效

如果配置未生效，可以通过tmux kill-server来强行关闭Tmux

- 查看当前配置

    tmux show -g  


## 快捷键及 用途

```key
c	创建新窗口
&	关闭当前窗口
[0-9]	数字键切换到指定窗口
p	切换至上一窗口
n	切换至下一窗口
l	前后窗口间互相切换
w	通过窗口列表切换窗口
,	重命名当前窗口，便于识别
.	修改当前窗口编号，相当于重新排序
f	在所有窗口中查找关键词，便于窗口多了切换


”	将当前面板上下分屏
%	将当前面板左右分屏
x	关闭当前分屏
!	将当前面板置于新窗口,即新建一个窗口,其中仅包含当前面板
q	显示面板编号
o	选择当前窗口中下一个面板
{	向前置换当前面板
}	向后置换当前面板
z	最大化当前所在面板在z退出当前面板
方向键	移动光标选择对应面板
page up	向上滚动屏幕，q 退出
page down	向下滚动屏幕，q 退出
alt+o	逆时针旋转当前窗口的面板
ctrl+o	顺时针旋转当前窗口的面板
alt+方向键	以 5 个单元格为单位移动边缘以调整当前面板大小

q	快速显示当前面板上的数字选择数字选中窗口
{   顺时针替换窗口位置

```