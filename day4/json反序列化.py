# @Time    : 2018/3/14 15:56
# @Author  : Alienzjn
# @Email   : zjning95@126.com
# @File    : json反序列化.py

#import json

import pickle

f = open("test.txt", "rb")

#data = json.loads(f.read())
data = pickle.loads(f.read())

print(data["age"])
