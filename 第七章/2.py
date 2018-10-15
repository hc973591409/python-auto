import re

# 创建regex对象
regex = re.compile(r'\d+')

string = '123-456-789'
print(re.findall(regex, string))
# 有分组就会列表['123', '456', '789']

numRegex = re.compile(r'\d+')
print(numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens'))