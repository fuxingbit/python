# @Time    : 2018/7/2 18:11
# @Author  : Jennings
# @Email   : zjn@wiwi.ink

class Dog(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eatting ...%s " % (self.name, food))

def bulk(self):
    print("%s is yelling...." % self.name)


d = Dog("Alex")
choice = input(">>>>:").strip()

# print(hasattr(d, choice))
# print(getattr(d, choice))
if hasattr(d, choice):
    getattr(d, choice)
    # func = getattr(d, choice)
    # func("oldboy")
else:
    setattr(d, choice, bulk)
    func = getattr(d, choice)
    func(d)


# 反射
#     hasattr(obj, name_str),判断一个对象obj是否有对应name_str字符串方法
#     getattr(obj, name_str),根据字符串去获取obj对象里的对应的方法的内存地址

