# 逗号连接列表
def insert_and(li):
    li1 = li[:-1]
    li2 = li[-1]
    str1 = ','.join(li1)
    str2 = str1 + ', and ' + str(li2)
    return str2


spam = ['1', '2', '3', '4']
string = insert_and(spam)
print(string)


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# 00 10 20 30 40
# 01 11 21 31 41
# 02 12 22 32 42

for x in range(len(grid[0])):
    for y in range(len(grid)):
        print(grid[y][x],end='')

    print('')
