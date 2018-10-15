# 编写代码，如果变量 spam 中存放 1，就打印 Hello，如果变量中存放 2，就
# 打印 Howdy，如果变量中存放其他值，就打印 Greetings!

spam = 3

if spam == 1:
    print("hello")
elif spam == 2:
    print('Howdy')
else:
    print('Greetings')

# round()函数
print(round(1.2))
print(round(1.5))
print(round(-1.6))
# 1  四舍五入函数
# 2
# -2

# abs函数 取绝对值
print(abs(1.2))
print(abs(2))
print(abs(-1.2))
print(abs(-2))

# 函数中修改全局变量

def chenge_global():
    # 函数中修改全局变量必须用global声明式全局变量
    global num
    num = 100


num  = 10
chenge_global()
print(num)

