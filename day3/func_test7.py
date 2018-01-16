# @Time    : 2018/1/16 23:41
# @Author  : Alienzjn
# @Email   : zjning95@126.com
# @File    : func_test7.py

#高阶函数

def add(x,y,f):
    return f(x) + f(y)


res = add(3,-6,abs)

print(res)


b = '''{
            'bakend': 'www.oldboy.org',
            'record':{
                'server': '100.1.7.9',
                'weight': 20,
                'maxconn': 30
            }
        }'''

eval(b)

print(b)
