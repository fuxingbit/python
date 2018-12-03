# @Time    : 2018/1/16 21:31
# @Author  : Jenliver
# @Email   : zjning95@126.com
# @File    : func_test5.py

#*args:接受N个位置参数，转换成元组
# def test(*args):
#     '''传递不固定的多个参数'''
#     print(args)
#
# test(1,3,4,6,8,9)
# test(*[1,3,4,6,8,9])  # args = tuple([1,3,4,6,8,9])

# def test(x,*args):
#     print(x)
#     print(args)
#
# test(1,2,3,4,5,6,7)

#**kwargs:把N个关键字参数，转换成字典的方式
# def test2(**kwargs):
#     print(kwargs)
#     print(kwargs['name'])
#     print(kwargs['age'])
#
#
# test2(name='alex',age=100,sex='F')
# test2(**{'name':'alex','age':80})

# def test3(name,**kwargs):
#     print(name)
#     print(kwargs)
#
# # test3('alex')
# test3('alex',sex='F',age=90)

#**kwargs放到形参最后面
# def test4(name,age=80,**kwargs):
#     print(name)
#     print(age)
#     print(kwargs)
#
# test4('alex',sex='m',hobby='tesla')
# test4('alex',sex='m',hobby='tesla',age=3)
# test4('alex',age=5,sex='m',hobby='tesla')

def test4(name,age=80,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
    logger("TEST4")

def logger(source):
    print("from %s" % source)

test4('alex',age=5,sex='m',hobby='tesla')

#程序从上往下执行，在定义之前应用会报错

