# 手动制表
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def print_table(tableData):
    x = len(tableData)          # 获取多少行
    y = len(tableData[0])       # 获取多少列
    
    column = []                 # 获取每一列的最大长度
    for i in range(y):                 # 0             1             2 3 4
        max_length = 0
        for j in range(x):             # 0,1,2,3,4     0,1,2,3,4
            if max_length < len(tableData[j][i]):
                max_length = len(tableData[j][i])
        column.append(max_length)
    
    print(column)
    # 打印阶段
    for i in range(x):
        for j in range(y):
            if j == 0:
                print(tableData[i][j].rjust(column[j]), end='\t')
            else:
                print(tableData[i][j].ljust(column[j]), end='\t')
        print("")

print_table(tableData)
