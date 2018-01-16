# @Time    : 2018/1/16 22:07
# @Author  : Alienzjn
# @Email   : zjning95@126.com
# @File    : func_test6.py


# sex='man' #全局变量
# school = 'oldboy edu.'
#
# def change_name(name):
#     global school   #全局变量
#     school = 'Mage Linux'
#     print("before change",name)
#     name = "ALEX LI"    #局部变量只在函数里生效，这个函数就是这个变量的作用域
#     age = 23    #局部变量
#     print("after name",name,sex,school)
#
# name = "alex"
#
# change_name(name)
# print(name,"school:",school)

names = ["Alex","Jack","Rain"]
def change_name():
    print(names)
    names[0] = "金角大王"
    print("inside func:",names)

change_name()
print(names)