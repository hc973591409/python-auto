# 一个神奇的数学序列
def collatz(num):
    if num%2 == 0:
        num /= 2
    
    else:
        num = 3*num +1
    
    return num

num = 3
while num != 1:
    num = collatz(num)
    print(num)

