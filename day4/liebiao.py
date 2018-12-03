# @Time    : 2018/1/20 18:40
# @Author  : Jenliver
# @Email   : zjning95@126.com
# @File    : liebiao.py

#[ i*2 for i in range(10) ]

#生成器，generator
#只有在调用时才会生成相应的数据,只记录当前位置，只有一个__next__()方法。2.7中是：next()

#( i*i for i in range(10) )

a = []

for i in range(10):
    a.append(i*2)

print(a)