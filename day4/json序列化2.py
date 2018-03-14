# @Time    : 2018/3/14 15:40
# @Author  : Alienzjn
# @Email   : zjning95@126.com
# @File    : json序列化.py

#import json

import pickle

info = dict(name="zjn", age=23)

f = open("test.txt", "wb")

pickle.dump(info, f)      #f.write(pickle.dumps(info))

f.close()

