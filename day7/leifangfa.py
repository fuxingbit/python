# @Time     :2018/7/1 下午5:37
# @Author   :Jennings
# @Email    :zjn@wiwi.ink


class Dog(object):
    name = 'huazai'

    def __init__(self, name):
        self.name = name

    # @staticmethod  #实际上跟类没关系了
    @classmethod
    def eat(self, food):
        print("%s is eatting %s " % (self.name, food))

    def __call__(self, *args, **kwargs):
        print("running call ", args, kwargs)

    def __str__(self):
        return "<obj:%s>" % self.name


# print(Dog.__dict__)  # 打印类里的所有属性，不包括实例属性
d = Dog("zlx")

print(d)

# print(d.__dict__)  # 打印所有实例属性，不包括类属性
# d.eat("baozi")

# d(1,2,3,4, name=333)
# Dog("zlx")()

# 类方法
# 只能访问类变量，不能访问实例变量
