
# @Time    : 2018/1/14 20:54
# @Author  : Alienzjn
# @Email   : zjning95@126.com
# @File    : encode.py



import sys

print(sys.getdefaultencoding())

s = "你好"

print(s)
print(s.encode("gbk").decode("gbk"))

print(s.encode("utf-8").decode("utf-8").encode("gb2312").decode("gb2312"))