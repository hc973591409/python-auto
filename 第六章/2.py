import sys
import pyperclip


PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
'luggage': '12345'}

if len(sys.argv) < 2:
    print("请输入账户名 如 python 2.py [acount] u 就可以拷贝密码")
    sys.exit()

# sys.argv[0] 是程序目录 sys.aegv[1]是外部输入
acount = sys.argv[1]
if acount in PASSWORDS:
    pyperclip.copy(PASSWORDS[acount])
    print("请在任意位置粘贴密码即可")
else:
    print('There is no acount named')

