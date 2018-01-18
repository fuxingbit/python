# @Time    : 2018/1/18 22:28
# @Author  : Alienzjn
# @Email   : zjning95@126.com
# @File    : decorator2.py

def foo():
    print('in the foo')
    #bar()相当于局部变量
    def bar():
        print('in the bar')

    bar()

foo()
