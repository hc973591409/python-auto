# 多重赋值技巧

cat = ['fat', 'black', 'loud']
size, color, disposition = cat
# 变量数必须严格等于列表数
print(size, color, disposition)

# 通过值获取列表对应的索引index
spam = ['hello', 'hi', 'howdy', '12']
# 如果不在就抛出异常，如果由重复的就返回第一次出现的索引
print(spam.index('hello'))

# 追加,append 尾部添加
spam.append("mouse")

print(spam)

# insert。特定位置添加
spam.insert(2, 'cat')
print(spam)

# 按照值删除列表内容，如果多次出现只删除第一个, 删除不存在的值就抛出异常
spam.remove('cat')
print(spam)

# 列表排序
spam = [1,9,2,8,3,7,3,6,4]
spam.sort()
# 默认从小到大排序
# 需要用到逆序才能从大到小
spam.sort(reverse=True)
print(spam)


