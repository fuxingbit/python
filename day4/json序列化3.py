# @Time    : 2018/3/14 15:40
# @Author  : Jenliver
# @Email   : zjning95@126.com
# @File    : json序列化.py

import json

info = dict(name="zjn", age=23)

f = open("test.txt", "w")
f.write(json.dumps(info))


info["age"] = 22
f.write(json.dumps(info))

f.close()

