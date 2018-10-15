# 复制一段文本,在每行前面加上一个 *
import pyperclip


text = pyperclip.paste()                    # 从剪切板获取文本
li = text.split('\n')                       # 按行切割文本, 得到一个字符串列表
li_new = []                                 # 新建一个空列表
for line in li:                             # 遍历列表
    li_new.append('*'+line)                 # 每一行都加上* 追加到li

string = '\n'.join(li_new)                  # 连接列表,获得新字符串
pyperclip.copy(string)
