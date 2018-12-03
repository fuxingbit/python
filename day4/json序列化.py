# @Time    : 2018/3/14 15:40
# @Author  : Jenliver
# @Email   : zjning95@126.com
# @File    : json序列化.py

#import json

import pickle

info = dict(name="zjn", age=23)

f = open("test.txt", "wb")

#print(json.dumps(info))
#f.write(json.dumps(info))
f.write(pickle.dumps(info))

f.close()

