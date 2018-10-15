import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for charater in message:
    count.setdefault(charater, 0)
    count[charater] += 1
# 漂亮打印 程序运行的时候，输出看起来更干净，排序过滤
pprint.pprint(count)
# 输出到屏幕
string = pprint.pformat(count)
# 输出到字符串
print(string)