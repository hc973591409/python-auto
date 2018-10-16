import os

for folder_name, sub_folders, filnames in os.walk('.\第九章'):
    print('当前文件是：' + folder_name)
    for sub_folder in sub_folders:
        print('子目录是：' + sub_folder)
    for filename in filnames:
        print('file inside :'+ folder_name + ":" + filename)

9-30 - 1100
