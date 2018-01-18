# @Time    : 2018/1/18 22:05
# @Author  : Alienzjn
# @Email   : zjning95@126.com
# @File    : decorator1.py


import time

def bar():
    time.sleep(3)
    print('in the bar')

def test1(func):
    start_time=time.time()
    func()
    stop_time=time.time()
    print("the func run time is %s " %(stop_time-start_time))


# test1(bar)
# bar()

def test2(func):
    print(func)
    return func

# print(test2(bar))
bar=test2(bar)
bar()