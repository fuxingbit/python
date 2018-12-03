# @Time    : 2018/4/27 16:58
# @Author  : Jenliver
# @Email   : zjning95@126.com
# @File    : main.py


#import module_alex

# print(module_alex.name)
# module_alex.say()



# from module_alex import *
# from module_alex import logging as logging_alex

import sys,os

x = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(x)

import module_alex


print(module_alex.name)
module_alex.say()

# def logging():
#     print("in the main")
#
# logging()
#
# logging_alex()