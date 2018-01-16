# @Time    : 2018/1/15 22:41
# @Author  : Alienzjn
# @Email   : zjning95@126.com
# @File    : func_test4.py

def test(x,y):
    print(x)
    print(y)

#x,y形参，1，2实参

#test(2,1)    #位置参数，与形参一一对应

#test(y=1,x=2)   #关键字参数，与形参顺序无关

#关键字参数不能写到位置参数前面

test(2,y=3)


def test1(x,y=2):
    print(x)
    print(y)

test1(2)
test1(1,y=3)

#默认参数特点：调用函数的时候，默认参数非必须传递
#用途：连接信息默认值