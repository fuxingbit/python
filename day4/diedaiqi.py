# @Time    : 2018/1/29 20:59
# @Author  : Jenliver
# @Email   : zjning95@126.com
# @File    : diedaiqi.py

#可以直接作用于for循环的对象统称为可迭代对象：Iterable。
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

from collections import Iterable

from collections import Iterator


isinstance('abc',Iterable)
isinstance((x for x in range(5)),Iterator)

isinstance(iter('abc'),Iterator)

#>>> isinstance('abc',Iterator)
#False
#>>> isinstance(iter('abc'),Iterator)
#True

# for x in [1,2,3,4,5]:
#     pass

it = iter([1,2,3,4,5])

while True:
    try:
        x = next(it)
    except StopIteration:
        break
