# @Time    : 2018/1/18 22:38
# @Author  : Jenliver
# @Email   : zjning95@126.com
# @File    : decorator3.py

import time

def timmer(func):    #timmer(test1)    func=test1
    def deco(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        stop_time=time.time()
        print("the func run time is %s " %(stop_time-start_time))
    return deco
@timmer    #test1=timmer(test1)
def test1():
    time.sleep(2)
    print('in the test1')

@timmer
def test2(name,age):
    time.sleep(2)
    print('in the test2:',name,age)

# test1=deco(test1)
# test1()
# test2=deco(test2)
# test2()

# test1=timmer(test1)
# test1()   #--->deco

test1()
test2("alex",22)