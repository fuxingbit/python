# @Time    : 2018/1/21 22:24
# @Author  : Alienzjn
# @Email   : zjning95@126.com
# @File    : feibonaqi.py


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        #print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

#fib(10)

# f = fib(100)
#
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())


g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break