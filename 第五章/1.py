spam = {'color': 'red', 'age':42}
print(spam['color'])
print(spam.keys())
# dict_keys(['color', 'age']) 字典键列表
print(spam.values())
# dict_values(['red', 42]) 返回值列表
print(spam.items())
# dict_items([('color', 'red'), ('age', 42)]) 键值列表

# 检查是否存在键
if 'age' in spam.keys():
    print('True')
else:
    print('False')

spam['egg'] = 2
print(spam)
# dic.get(key, default) key不存在的时候，输出default的值
print('i have '+ str(spam.get('egg', 0)) +'eggs')
print('i have '+ str(spam.get('cups', 0)) +'cups')

# 当key不存在的时候输出white，存在的时候按原值输出，后来写这句话并不会覆盖原来的数字
spam.setdefault('color', 'white')

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for charater in message:
    # 每个字符的初始值都设置为0
    count.setdefault(charater, 0)
    # i 出现第一次 count[i] = 0+1 第二次的时候 count[i] +1
    count[charater] = count[charater] + 1

print(count)

