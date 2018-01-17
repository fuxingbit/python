# @Time    : 2018/1/17 21:05
# @Author  : Alienzjn
# @Email   : zjning95@126.com
# @File    : decorator.py

#装饰器：
#本质是函数，装饰其他函数，就是为其他函数添加附加功能
#原则：1。不能修改被装饰的函数的源代码
#     2.不能修改被装饰的函数的调用方式

#http://egon09.blog.51cto.com/9161406/1836763

#实现装饰器知识储备：
#1.函数即“变量”
#2.高阶函数
#3.嵌套函数

import time

def timmer(func):
    def warpper(*args,**kwargs):
        start_time=time.time()
        func()
        stop_time=time.time()
        print('the func run time is %s ' %(stop_time-start_time))
    return warpper

@timmer
def test1():
    time.sleep(1)
    print("In the test1")

test1()