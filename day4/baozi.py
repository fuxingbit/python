# @Time    : 2018/1/22 21:58
# @Author  : Alienzjn
# @Email   : zjning95@126.com
# @File    : baozi.py

import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield

       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))

# c = consumer("Alex")
# c.__next__()
#
# b1 = "韭菜馅"
# c.send(b1)
# c.__next__()


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)
        c2.send(i)

producer("alex")

#单线程下的并行效果