# @Time    : 2018/6/1411:17
# @Author  : Jennings
# @Email   : zjn@wiwi.ink

import shelve
import datetime

d = shelve.open('shelve_test')  # 打开一个文件

# name = ["alex", "rain", "test"]
# info = {"age": 22, "jod": "it"}
# date = datetime.datetime.now()
#
# d["name"] = name  # 持久化列表
# d["info"] = info  # 持久化dict
# d["date"] = date

print(d.get("name"))
print(d.get("info"))
print(d.get("date"))

d.close()
