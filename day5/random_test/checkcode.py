# @Time    : 2018/4/28 16:37
# @Author  : Alienzjn
# @Email   : zjning95@126.com
# @File    : checkcode.py

import random

checkcode = ''

for i in range(4):
    current = random.randint(0, 4)

    # 字母
    if current == i:
        tmp = chr(random.randrange(65, 90))
    # 数字
    else:
        tmp = random.randint(0, 9)

    checkcode += str(tmp)

print(checkcode)