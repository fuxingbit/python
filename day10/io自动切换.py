# @Time     :2018/7/17 上午12:10
# @Author   :Jennings
# @Email    :zjn@wiwi.ink

import gevent


def func1():
    print('\033[31;1m111111111111111111...\033[0m')
    gevent.sleep(2)
    print('\033[31;1m22222222222222...\033[0m')


def func2():
    print('\033[32;1m3333333333333333...\033[0m')
    gevent.sleep(1)
    print('\033[32;1m44444444444444...\033[0m')


def func3():
    print('\033[33;1m55555555555555555...\033[0m')
    gevent.sleep(0)
    print('\033[33;1m66666666666666666666...\033[0m')


gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
    gevent.spawn(func3),
])
