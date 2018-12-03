# @Time    : 2018/4/28 16:18
# @Author  : Jenliver
# @Email   : zjning95@126.com
# @File    : random1.py

import random

print(random.random())

print(random.randint(4, 80))

print(random.randrange(1, 3))    #顾头不顾尾，1,2

print(random.choice('safhasdjf'))    #从序列中随机获取一个元素
print(random.choice([1, 3, 7]))

# 从指定序列中随机获取指定长度的片段
print(random.sample('hello', 2))

print(random.uniform(3, 9))    #随机浮点数指定区间

# 洗牌
items = [1, 2, 3, 4, 5, 6, 7]
print(items)
random.shuffle(items)
print(items)