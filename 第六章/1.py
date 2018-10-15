# 由于字符串是一个不可变的数据结构,所以所有的字符串方法,返回都是都一个新字符串
spam = 'Hello World'
spam = spam.upper()
# 字符串转大写
print(spam.isupper())
# 判断字符串是不是都是大写

spam = spam.lower()
# 字符串转小写

print(spam.islower())
# 判断字符串是不是都是小写

print(spam)

salpha()返回 True， 如果字符串只包含字母， 并且非空；
isalnum()返回 True，如果字符串只包含字母和数字，并且非空；
isdecimal()返回 True，如果字符串只包含数字字符，并且非空；
isspace()返回 True，如果字符串只包含空格、制表符和换行，并且非空；
istitle()返回 True，如果字符串仅包含以大写字母开头、后面都是小写字母的单词

startswith()和 
endswith()方法返回 True， 如果它们所调用的字符串以该方法传入
的字符串开始或结束。否则， 方法返回 False

字符串连接函数 join
如果有一个字符串列表， 需要将它们连接起来，成为一个单独的字符串， join()
方法就很有用。 join()方法在一个字符串上调用， 参数是一个字符串列表， 返回一个
字符串。

字符串切割函数split()

用 rjust()、 ljust()和 center()方法对齐文本
'Hello'.rjust(10)是说我们希望右对齐，将'Hello'放在一个长度为 10 的字符串中。
'Hello'有 5 个字符， 所以左边会加上 5 个空格， 得到一个 10 个字符的字符串， 实现
'Hello'右对齐。
rjust()和 ljust()方法的第二个可选参数将指定一个填充字符， 取代空格字符。在
交互式环境中输入以下代码：
>>> 'Hello'.rjust(20, '*')
'***************Hello'
>>> 'Hello'.ljust(20, '-')
'Hello------------------------'

用 strip()、 rstrip()和 lstrip()删除空白字符