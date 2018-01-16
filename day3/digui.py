# @Time    : 2018/1/16 22:52
# @Author  : Alienzjn
# @Email   : zjning95@126.com
# @File    : digui.py


# def calc(n):
#     print(n)
#     if int(n/2) > 0:
#         return calc( int(n/2) )
#     print("-->",n)
#
# calc(10)

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)


print(fact(9))
