# VIM 我的一些用法


## vim 的进入方式

```access

vim +n file 打开具体报错行
vim + file 最后一样
vim +/pattern file 

vim +On file1 file2  打开连个文件竖屏
ctrl + w h	     光标定位到左边左边	
ctrl + w l 	     光标定位到右边
向下/上/左/右移动  j/k/h/l
窗口打开模式 本窗口/新窗口 f/F



vim +on file1 file2  横屏打开两个文件
ctrl + w j
ctrl + w k
```


## 复制 y 和删除 d

```yd
yw 复制光标开始的一个单词
y$ 复制光标到行尾
yfyou 复制当前光标到you单词中的内容

dw 删除一个单词 
df ” 删除到出现的第一个双引

```


## 可视化模式

```v
可视化 v 是通过 hjkl 进行选择正行的内容

ctr + v 块 是可以通过此进行 竖直行的整体性插入


```


## 命令模式

普通模式下输入: 进入命令模式

```command
%s/$/sth/ 在行尾追加sth


```

# 光标移动

```g
`` 当前文件中上次跳转之前的位置
`. 跳转到上修改的地方
%  可以在括号间跳转
{Hi this is a test}
怎么快速的吧{} 改为[]

首先光标移动到{然后按% 然后r] 然后`` 再次输入r[

<ctrl>+o 跳转回之前的位置
<ctrl>+i 返回跳转之前的位置
% 跳转到下一个匹配,如在<div>上按%，则跳转到相应的</div>

f'd' 跳转到下一个单词位置

## 其他

```other

r 替换字符
:s/old/new 替换该行第一个匹配串
:s/old/new/g 替换全行的匹配串
:%s/old/new/g 替换整个文件的匹配串

ggVG 全选
u 恢复更改
J 合并下一行
gU 光标处转大写
ggguG 整篇文章大写转化为小写
:e /tmp/a 在同一个编辑器内打开/tmp/a文件。同一个编辑器的缓冲区是剪贴板是共享的，可以方便在多个文件中复制
bp 跳转到上一个缓冲区
bn 跳转到下一个缓冲区


u 撤销
<ctrl>+r 取消撤销

<ctrl>+g 显示当前行以及文件信息


```


```boss
HJKL 让右手歇歇，毕竟右手 “很累”


这是 vim 中的光标上下左右的移动，刚开始使用 vim 的同学可能觉得这并没有什么卵用，我用键盘上的上下左右就可以了！我们知道，vim 的大部分快捷键需要在命令模式下完成，而且 HJKL 也是需要在命令模式下才生效的，如果你经常在插入模式下工作，当然不会去用 HJKL。然而，当你真正开始更多的使用命令模式的时候，你会懒到不想把右手挪到 “上下左右” 那儿去，这个时候 HJKL 成为无需思考的反射行为。HJKL 的好处就是减少了右手的位移距离。毕竟右手还有很多 “事情” 要做。



让你的操作可重复

我们来举个例子，假设如下文本



one two three four five six


我希望改成



"one","two","four","five","six"


首先光标定位在该行的行首，可使用^。然后键入f␣(␣表示空格)，此时光标定位在 one 和 two 之间的空格处，然后键入c␣","（修改空格，进入插入模式，然后增加","）:



one","two three four five six


接着按;.，光标将先查找下一个空格，即重复f␣，这个空格位于 two 和 three 之间，然后.可以重复上一次的修改操作，即c␣","：



one","two","three four five six


接着重复按若干次;.即可完成所有中间字符的修改：

one","two","three","four","five","six


最后应用I和A，添加开始和最后的双引号就可以了。



通过这个例子，vimer 必须要领会的一个精髓是：让你的操作可重复!!。如果上面的例子，我们用l或者->来定位空格的话，由于 one、two、three 这些单词的长度是不确定的，我们无法事先知道需要按多少次l，所以l定位是不可重复的。而通过f可以重复我们的查找操作，从而精确的定位到空格。另外，如果我们通过xi","代替c␣","也是不可重复的，因为xi","表示先删除空格，然后进入插入模式后键入","，这样就是两次分开的修改操作，而最近的操作变成了 “进入插入模式后键入","”，如果通过.重复这个操作，是无法删除空格的。



这需要大量的实践和练习，才能改掉鼠标流的思维定式。一般来说，尽量多用f、c、r是不错的选择。另外，尽可能的利用A、a、o、O来进入插入模式，而不是每次通过i进入插入模式。



高效移动

光标移动效率是 vim 程序员达到甚至超过鼠标流程序员的关键技能。vim 中的移动光标的方式有很多，我来举几个我实际使用过程中应用比较频繁的技巧：



set relativenumber(显示相对行号)。我无意间发现的一个十分实用的技巧，比set number显示行号更好用。通过这个设置，行号的显示会根据当前的光标的相对位置显示成偏移数，并动态变化。这个好处是，可以利用数字+j 数字+k来进行多行跳转，因为是编译行数，所以数字不会太大。否则就算要向下移动 10 行，我们可能也需要用138gg。







w、e、b：按照单词进行前后光标跳转，也可以组合数字进行跳转，不过以我的经验，与其去算要跳多少个单词，不如多按几次吧。

I、A：移动到行首或行末的第一个字符处，并进入插入模式。

H、M、L：光标分别跳转到可视区域的最上面、中间、最下面。

Ctrl+D、Ctrl+U：有时，需要看的文本不在可视区域，通过这些组合进行上下翻页。

^、$、0：光标移动到行首和行尾（0 是绝对行首）。不过因为^和$都需要同时按住 shift，而且数字键我们往往难以盲打，所以我一般直接使用I+Esc、A+Esc。

%：移动到与当前括号匹配的括号处。

gj、gk：有时可视区域不够宽，而一行的字符有很多，导致了 wrap。那么通过 jk 是无法直观的定位到同一物理行，却不在同一个可视行里的位置，此时需要gj和gk。

f、F：通过上面的例子，我们知道，f是 find 的意思，可以在一行内查找某个字符出现的位置，并直接跳转过去。比如f<可以从当前光标开始向右，找到第一个<，并移动过去。F 是向左查找。

;：重复上一次的f查找操作

.：重复上一次的修改操作，跟;可以说是好基友，经常用来实现一些简单的重复操作，比录制宏要简单很多。经常有意识的使用这种简单重复，是 vimer 编辑思路进阶的分水岭。


高效修改

vim 的另一个优势是高效修改。在 vim 下修改就要改掉传统鼠标流的思维方式，切忌提到修改就按i。有很多高效的修改办法，而且这些办法往往是可重复的。下面举一些我常用的例子：

r：替换模式，替换当前光标所在位置的一个字符。虽然你同样可以i进入插入模式，然后删掉那个字符，再输入需要的字符，但这种操作是鼠标流思维方式。替换是一个可重复操作，多用没坏处。

cw：change word可以删除从当前位置到一个单词的结尾，并进入插入模式。这种操作常用于修改一个变量。比如对于：int count=0;希望把count改成cnt，那么当光标位于c字符处的时候，按cw可直接删除count，并进入插入模式。然后直接继续输入cnt即可。

caw：change a word可以删除当前光标所在位置的单词。对于int count=0;的例子，如果此时光标在count中间某处，比如u处，直接键入caw可以达到同样的效果。所以caw更强大一些。

c$、c^：举一反三，可以猜到c$是从当前位置删除到行尾，并进入插入模式。

ci"：change inside "可以用于修改当前位置附近，在相同配对的"中的内容。比如对于const char *str="hello world";。当在双引号中间的任意位置键入ci"可以直接清空字符串，并继续输入新的希望的字符串。

ci(、ci[：举一反三change inside ( change inside [。

cit：这个比较特殊，可以直接编辑匹配的 xml 标签中的内容！经常编写 html 的童鞋可以熟悉一下。

yi"：yank inside " 猜猜是啥意思？类似ci"只是把编辑操作编程复制操作，因为y是复制！是不是很强大。

ya"：yank around " 复制整个字符串，包括双引号。

yw、yaw、daw、d$…：好了，这些可以” 发明” 出来了。

o、O：向下向上增加空行

u、Ctrl+r：undo 和 redo



上面的例子体现了 vim 组合的思想，很多命令可以通过组合得到不同的效果。



Visual 模式是鼠标流后遗症，不过也有妙用

v、V、Ctrl+v是 Visual 模式，类似用鼠标选中一些文本。我在早期使用 vim 时候，十分喜欢用v，比如要删除一个单词，我往往会用vwd，试图用vw选中一个单词，然后d删除。这种方式明显是鼠标流的后遗症。直到我学会上面介绍的一些技巧后，v已经很少用了。不过Ctrl+v是Block Visual模式，类似选中列，这个技巧有时很有用。比如有如下文本：



one
two
three
four


希望变成



"one, two, three, four"


首先将光标定位到 one 的 o 处，Ctrl+v，3j，$，A，,，Esc，V，3j，J。这一套连招下来，出来了：



one, two, three, four,


如果要合的行数很多，就比较有优势了。问我怎么知道按3j，上文提到的set relativenumber帮到你。



总结


在开发效率上，不敢说 vim 优于 IDE，不过 vim 的编辑和修改速度是比鼠标快的。使用 vim 的过程就是自我否定和自动重塑的过程，如果你不断的学习技巧的话，编辑习惯会一再被推翻，一再重塑。不断有新的理解注入到日常的工作中。最终会形成自己编辑风格。


https://mp.weixin.qq.com/s?__biz=MzAxODI5ODMwOA==&mid=2666542307&idx=1&sn=84a5ed8b6f0c005aa8c47f2570b653f1&chksm=80dcf048b7ab795e21a0e44e6092552c424e6bee6185043814bd333e72a21035424603d3727b&scene=0#rd

```
