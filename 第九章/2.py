# 文件发送到计算机的垃圾箱或回收站，而不是永久删除它们。如果因程序缺陷而用
# send2trash 删除了某些你不想删除的东西，稍后可以从垃圾箱恢复
import send2trash

import os


for path in os.listdir():
    if path.endswith('.txt'):
        # 打开指定的path  扔到垃圾箱，如果失误就从垃圾箱回复
        send2trash.send2trash(path)
