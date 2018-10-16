import shelve

def shelve_save():
    # shelve 可以保存或者打开一个二进制文件， 用于存放python变量
    dic = {'age':10, 'name': 'Hu', 'color': 'yellow'}
    shelve_file = shelve.open('mydata')
    shelve_file['my'] = dic
    shelve_file.close()

# shelve_save()
# shelve就像一个变量一样，打开以后就可以把本地文件当作一个python字典来用
# 并且不需要指定打开模式， 只要打开就是一个字典，知道里面的数据表结构即可
def get_shelve():
    shelve_file = shelve.open('mydata')
    print(shelve_file['my'])
    shelve_file.close()

get_shelve()

