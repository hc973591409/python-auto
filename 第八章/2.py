# open打开一个文件
# 默认位read模式
helloFile = open('C:\\Users\\your_home_folder\\hello.txt')


# read 读取文件内容 
>>> helloContent = helloFile.read()
>>> helloContent
'Hello world!'

# readlines 按行读取 返回一个列表
>> sonnetFile = open('sonnet29.txt')
>>> sonnetFile.readlines()
[When, in disgrace with fortune and men's eyes,\n', ' I all alone beweep my
outcast state,\n', And trouble deaf heaven with my bootless cries,\n', And
look upon myself and curse my fate,']


# 写入文件   'w'模式 没有就创建，有就重新写入
>>> baconFile = open('bacon.txt', 'w')
# write 写入
>>> baconFile.write('Hello world!\n')
13
>>> baconFile.close()
# 'a' 追加的方式
>>> baconFile = open('bacon.txt', 'a')
>>> baconFile.write('Bacon is not a vegetable.')
25
>>> baconFile.close()

# 默认读模式，不能写入
>>> baconFile = open('bacon.txt')
>>> content = baconFile.read()
>>> baconFile.close()
>>> print(content)
Hello world!
Bacon is not a vegetable.







