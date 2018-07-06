# @Time    : 2018/7/6 20:08
# @Author  : Jennings
# @Email   : zjn@wiwi.ink

import importlib

# __import__('import_lib.metaclass') #这是解释器自己内部用的
# importlib.import_module('import_lib.metaclass') #与上面这句效果一样，官方建议用这个

aa = importlib.import_module('lib.aa')

print(aa.C().name)

# mod = __import__("lib.aa") # lib
# obj = mod.aa.C()
# print(obj.name)




