### vim 常用功能
1. 让自己的操作可以重复
one two three four five six
首先光标定位在该行的行首，可使用^。然后键入f␣(␣表示空格)，此时光标定位在 one 和 two 之间的空格处，然后键入c␣","（修改空格，进入插入模式，然后增加","）:

- ;：重复上一次的f查找操作
- .：重复上一次的修改操作，跟;可以说是好基友，经常用来实现一些简单的重复操作.

```
vimer 必须要领会的一个精髓是：让你的操作可重复!!。如果上面的例子，我们用l或者->来定位空格的话，由于 one、two、three 这些单词的长度是不确定的，我们无法事先知道需要按多少次l，所以l定位是不可重复的。而通过f可以重复我们的查找操作，从而精确的定位到空格。另外，如果我们通过xi","代替c␣","也是不可重复的，因为xi","表示先删除空格，然后进入插入模式后键入","，这样就是两次分开的修改操作，而最近的操作变成了 “进入插入模式后键入","”，如果通过.重复这个操作，是无法删除空格的。

这需要大量的实践和练习，才能改掉鼠标流的思维定式。一般来说，尽量多用f、c、r是不错的选择。另外，尽可能的利用A、a、o、O来进入插入模式，而不是每次通过i进入插入模式。
```
- w、e、b：按照单词进行前后光标跳转，也可以组合数字进行跳转，不过以我的经验，与其去算要跳多少个单词，不如多按几次吧。
- I、A：移动到行首或行末的第一个字符处，并进入插入模式。
- H、M、L：光标分别跳转到可视区域的最上面、中间、最下面。
- Ctrl+D、Ctrl+U：有时，需要看的文本不在可视区域，通过这些组合进行上下翻页。
- ^、$、0：光标移动到行首和行尾（0 是绝对行首）。不过因为^和$都需要同时按住 shift，而且数字键我们往往难以盲打，所以我一般直接使用I+Esc、A+Esc。
- %：移动到与当前括号匹配的括号处。
- gj、gk：有时可视区域不够宽，而一行的字符有很多，导致了 wrap。那么通过 jk 是无法直观的定位到同一物理行，却不在同一个可视行里的位置，此时需要gj和gk。
- f、F：通过上面的例子，我们知道，f是 find 的意思，可以在一行内查找某个字符出现的位置，并直接跳转过去。比如f<可以从当前光标开始向右，找到第一个<，并移动过去。F 是向左查找。

##### 高效修改
- r：替换模式，替换当前光标所在位置的一个字符。R这个是替换当前字符到最后
- cw：change word可以删除从当前位置到一个单词的结尾，并进入插入模式。这种操作常用于修改一个变量。比如对于：int count=0;希望把count改成cnt，那么当光标位于c字符处的时候，按cw可直接删除count，并进入插入模式。然后直接继续输入cnt即可。
- caw：change a word可以删除当前光标所在位置的单词。对于int count=0;的例子，如果此时光标在count中间某处，比如u处，直接键入caw可以达到同样的效果。所以caw更强大一些。
- cI、cA：举一反三，dI是删除到行首 dA删除到行位 可以猜到c$是从当前位置删除到行尾，并进入插入模式。 通常模式下还是需要c^替换到开头 c$ 替换到结尾,同理d也一样
- ci"：change inside "可以用于修改当前位置附近，在相同配对的"中的内容。比如对于const char \*str="hello world";。当在双引号中间的任意位置键入ci"可以直接清空字符串，并继续输入新的希望的字符串。
- ci(、ci[：举一反三change inside ( change inside [。
- cit：这个比较特殊，可以直接编辑匹配的 xml 标签中的内容！经常编写 html 的童鞋可以熟悉一下。
- yi"：yank inside " 猜猜是啥意思？类似ci"只是把编辑操作编程复制操作，因为y是复制！是不是很强大。
- ya"：yank around " 复制整个字符串，包括双引号。
- yw、yaw、daw、d$…：好了，这些可以” 发明” 出来了。
- o、O：向下向上增加空行
- u、Ctrl+r：undo 和 redo

####

命令行工具里面还是不一样的
ctrl w 删除鼠标前面单词  
ctrl u 删除光标到最前段的字符

ctrl k 删除鼠标后所有字符串  
ctrl d 删除光标前字符  
ctrl b 向前移动光标不删除  
ctrl f 向后移动光标不删除
