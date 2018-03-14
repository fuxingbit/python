# @Time    : 2018/3/14 15:56
# @Author  : Alienzjn
# @Email   : zjning95@126.com
# @File    : json反序列化.py

import json

# import pickle

# 只dump一次，load一次

f = open("test.txt", "r")


data = json.load(f)

print(data["age"])

