# @Time     :2018/7/1 下午5:21
# @Author   :Jennings
# @Email    :zjn@wiwi.ink


class Dog(object):
    '''
	描述狗这个对象
	'''

    def __init__(self, name):
        self.name = name

    # @staticmethod  #实际上跟类没关系了
    def eat(self, food):
        print("%s is eatting %s " % (self.name, food))

# d = Dog("zlx")
# d.eat("baozi")

# 打印类的描述信息
# print(Dog.__doc__)


# 静态方法
# 只是名义上归类管理，实际上在静态方法里访问不了类或实例中的任何属性
