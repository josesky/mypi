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

