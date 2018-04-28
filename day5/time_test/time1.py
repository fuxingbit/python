# @Time    : 2018/4/28 10:25
# @Author  : Alienzjn
# @Email   : zjning95@126.com
# @File    : time1.py

import time

print(time.time())

print(time.localtime())

x = time.localtime()

# print(x.tm_year)

print(time.mktime(x))

y = time.strftime("%Y-%m-%d %H:%M:%S", x)

print(y)

z = time.strptime("2018-04-28 11:41:50", "%Y-%m-%d %H:%M:%S")

print(z)

w = time.asctime()

print(w)

print(time.ctime())
