# strip的正则表达式版本

import re

def mystrip(string, t_s=r'\s'):
    t_format = r'^%s*(.*?)%s*$' %(t_s,t_s)
    print(t_format)
    regex = re.compile(t_format)
    m = re.match(regex, string)
    return m.groups()[0]


string = 'aaaahello worldaaa'
string = mystrip(string, 'a')
print(string)
string2 = '   hello world    '
string2 = mystrip(string2)
print(string2)

