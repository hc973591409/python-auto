# 拷贝文件
import os
import shutil

print(os.getcwd())

os.chdir(r'C:/Redis-x64-3.2.100')

# shutil.copy('1.txt', r'C:\\Users\\97359\\Documents\\GitHub\\python-auto\\第九章\\')
# shutil.copy('1.txt', r'C:\\Users\\97359\\Documents\\GitHub\\python-auto\\第九章\\2.txt')
# shutil.copy返回值位拷贝成功的路径

# 拷贝文件夹
>>> import shutil, os
>>> os.chdir('C:\\')
# 后面的目录不存在会自动创建
>>> shutil.copytree('C:\\bacon', 'C:\\bacon_backup')
'C:\\bacon_backup

# move实现剪切，文件已经存在就自动覆盖
>>> import shutil
>>> shutil.move('C:\\bacon.txt', 'C:\\eggs')
'C:\\eggs\\bacon.txt

# move实现更改名字
>>> shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')
'C:\\eggs\\new_bacon.txt'


# 删除文件和文件夹
import os
for filename in os.listdir():
if filename.endswith('.rxt'):
    os.unlink(filename)


