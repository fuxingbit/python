# @Time    : 2018/1/29 22:21
# @Author  : Alienzjn
# @Email   : zjning95@126.com
# @File    : neizhihanshu.py

#abs()
#取绝对值

#all()
#有0则false

#any()
#全空/0则false

#print(ascii([1,2,"恺威和史蒂夫"]))

#print(bin(255))
#数字十进制转二进制

#bool(1)
#判断真假

# bytearray()
# #可修改的二进制字节格式
#
# a = bytes("abcde",encoding='utf-8')
# b = bytearray("abcde",encoding='utf-8')
#
# print( b[1] )
# b[1] = 100
# print(b)

#print(a.capitalize(),a)

# def sayhi():pass
# #判断是否可调用
# print( callable(sayhi))

# chr(97)
#
# ord('a')

# code = "for i in range(10):print(i)"
#
# c = compile(code, '', 'exec')
# exec(c)

# code1 = "1+3/2*6"
# d = compile(code1, '', 'eval')
#
# eval(code1)

# code = '''
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         #print(b)
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
# g = fib(6)
# while True:
#     try:
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break
#
# '''

#py_obj = compile(code, "err.log", "exec")
#exec(py_obj)

#exec(code)

#返回除数和余数
# print(divmod(5, 4))

# def shu(n):
#     print(n)
#
# shu(3)
#
# #(lambda n:print(n))(5)
# calc = lambda n:print(n)
# calc(5)

#res = filter(lambda n:n>5, range(10))
# res = map(lambda n:n*n, range(10))
# #res = [lambda i:i*i for i in range(10)]
# for i in res:
#     print(i)
# import functools
#
# res = functools.reduce(lambda x, y:x+y, range(10))
# print(res)
#不可变集合
#frozenset([])

#以key：value的形式返回这个文件、程序的全局变量
#print(globals())

#十进制转十六进制
#hex(255)

#十进制转八进制
# oct(16)

#返回2的8次方
#pow(2,8)


#round(1.2222, 2)

