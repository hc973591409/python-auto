>>> import os
>>> os.path.join('usr', 'bin', 'spam')
'usr\\bin\\spam'

在 OS X 或 Linux 上调用这个函数， 该字符串就会是
'usr/bin/spam'。

>>> myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
>>> for filename in myFiles:
print(os.path.join('C:\\Users\\asweigart', filename))
C:\Users\asweigart\accounts.txt
C:\Users\asweigart\details.csv
C:\Users\asweigart\invite.docx

# 当前工作目录
>>> import os
>>> os.getcwd()
'C:\\Python34'

# 改变工作目录
>>> os.chdir('C:\\Windows\\System32')
>>> os.getcwd()
'C:\\Windows\\System32'

# 创建目录,并且是递归方式创建,中间文件夹一并创建
>>> import os
>>> os.makedirs('C:\\delicious\\walnut\\waffles')


# os.path 模块
调用 os.path.abspath(path)将返回参数的绝对路径的字符串。这是将相对路径转
换为绝对路径的简便方法

调用 os.path.isabs(path)，如果参数是一个绝对路径，就返回 True，如果参数是
一个相对路径，就返回 False。

调用 os.path.relpath(path, start)将返回从 start 路径到 path 的相对路径的字符串。
如果没有提供 start，就使用当前工作目录作为开始路径

>>> os.path.abspath('.')
'C:\\Python34'
>>> os.path.abspath('.\\Scripts')
'C:\\Python34\\Scripts'
>>> os.path.isabs('.')
False
>>> os.path.isabs(os.path.abspath('.'))
True

>>> os.path.relpath('C:\\Windows', 'C:\\')
'Windows'
>>> os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')
'..\\..\\Windows'
>>> os.getcwd()
'C:\\Python34


os.path.dirname(path) 返回当前路径目录
os.path.basename(path) 返回文件名

>>> path = 'C:\\Windows\\System32\\calc.exe'
>>> os.path.basename(path)
'calc.exe'
>>> os.path.dirname(path)
'C:\\Windows\\System32

>>> calcFilePath = 'C:\\Windows\\System32\\calc.exe'
# split 返回一个元组, 第一个元素位目录,第二个文件名
>>> os.path.split(calcFilePath)
('C:\\Windows\\System32', 'calc.exe')

# getsize() 返回文件的字节数
>>> os.path.getsize('C:\\Windows\\System32\\calc.exe')
776192
# 遍历目录下的所有文件名
>>> os.listdir('C:\\Windows\\System32')
['0409', '12520437.cpx', '12520850.cpx', '5U877.ax', 'aaclient.dll',
--snip--
'xwtpdui.dll', 'xwtpw32.dll', 'zh-CN', 'zh-HK', 'zh-TW', 'zipfldr.dll']

# 检查路径是否存在
>>> os.path.exists('C:\\Windows')
True
# 
>>> os.path.exists('C:\\some_made_up_folder')
False
# 检差路径是不是一个目录
>>> os.path.isdir('C:\\Windows\\System32')
True
# 检测路径是不是一个文件
>>> os.path.isfile('C:\\Windows\\System32')
False
>>> os.path.isdir('C:\\Windows\\System32\\calc.exe')
True