# VsCode 使用历程

 从Atom 转移到VsCode,只是因为这个vim 更好用!

## 插件安装

为了极大提升可玩度

### 插件功能及介绍
  
- Vim
- GitLens git功能
- Markdown All In On
- MarkdownLint 语法检查
- Python
- vscode-ico
- Material Icon Them

## 快捷键

常用快捷键

## 外观及设置

根据自己的习惯来选择自己喜欢的颜色主题
在坐下面的设置中选择颜色和主题

### 主题设置

可以感觉自己的喜好,安装不同的颜色主题

- 装了自己喜欢的小图标插件vscode-icons
  - \>icon 选择首选
  - 选择vscode-icons后发现左侧的小图标变的很好看了

### 字体及大小设置

在setting中编辑自己喜欢的字体及大小

- 设置编辑区字体打下和工作区字体大小
  - 设置工作区字体大小
  > // 调整窗口的缩放级别。原始大小是 0，每次递增(例如 1)或递减(例如 -1)表示放大或缩小 20%。也可以输入小数以便以更精细的粒度调整缩放级别.  
"window.zoomLevel": 0

  - 设置字体大小
  >"editor.fontSize": 16,

### 我的自定义设置

```json

{
    "editor.fontSize": 12,
    "terminal.integrated.shell.windows": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
    "git.autofetch": true,
    "window.zoomLevel": 0.5,
    "markdown.preview.fontSize": 12,
    "terminal.integrated.fontSize": 12,
    "git.path": "D:\\github\\Git\\bin\\git.exe",
    "workbench.colorTheme": "Tomorrow Night Blue",
    "workbench.statusBar.feedback.visible": false,
    "workbench.iconTheme": "vscode-icons"
}

```

### 警告处理

#### git 插件安装后提示搜索不到  

  1. Ctrl + Shift + P
  2. 搜索settings.json
  3. 在新的窗口输入git.path
  4. 在用户栏目中输入我当前的git的目录"git.path": "D:\github\Git\bin\git.exe" 保存后重载