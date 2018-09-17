### sed 使用
Sed:
1、删除行首空格
   sed 's/^[ ]*//g' filename
   sed 's/^ *//g' filename
   sed 's/^[[:space:]]*//g' filename

2、行后和行前添加新行
   行后：sed 's/pattern/&\n/g' filename
   行前：sed 's/pattern/\n&/g' filename
   &代表pattern

3、使用变量替换(使用双引号)
    sed -e "s/$var1/$var2/g" filename

4、在第一行前插入文本
    sed -i '1 i\插入字符串' filename

5、在最后一行插入
    sed -i '$ a\插入字符串' filename

6、在匹配行前插入
    sed -i '/pattern/ i "插入字符串"' filename

7、在匹配行后插入
   sed -i '/pattern/ a "插入字符串"' filename

8、删除文本中空行和空格组成的行以及#号注释的行
   grep -v ^# filename | sed /^[[:space:]]*$/d | sed /^$/d
