# @Time    : 2018/4/28 16:07
# @Author  : Alienzjn
# @Email   : zjning95@126.com
# @File    : datatime1.py

import datetime

# print(datetime.date())

print(datetime.datetime.now())

# 当前时间+3天
print(datetime.datetime.now()+datetime.timedelta(3))
print(datetime.datetime.now()+datetime.timedelta(-3))

# 当前时间+3小时
print(datetime.datetime.now()+datetime.timedelta(hours=3))
print(datetime.datetime.now()+datetime.timedelta(hours=-3))
print(datetime.datetime.now()+datetime.timedelta(minutes=30))

c_time = datetime.datetime.now()
print(c_time.replace(minute=3, hour=5))  #时间替换
