# 强口令检测
# 位数不得低于8 位, 有小写 有大写 有数字
import re
import pyperclip

def chack(string):
    if len(string) < 8:
        print('too short')
        return False
    
    regex1 = re.compile('[A-Z]')
    # 如果匹配不上就返回None
    if re.search(regex1, string) == None:
        print("请输入至少一个大写字母")
        return False
    regex2 = re.compile('[a-z]')
    # 如果匹配不上就返回None
    if re.search(regex2, string) == None:
        print("请输入至少一个小写字母")
        return False

    regex3 = re.compile('\d')
    # 如果匹配不上就返回None
    if re.search(regex3, string) == None:
        print("请输入至少一个数字")
        return False

    print("符合要求")
    return True


string = 'fasdjAfsd1f'
chack(string)
    


    