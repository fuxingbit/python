# @Time     :2018/7/1 下午5:52
# @Author   :Jennings
# @Email    :zjn@wiwi.ink

class Dog(object):
	def __init__(self, name):
		self.name = name
		self.__food = None

	# @staticmethod  #实际上跟类没关系了
	@property
	def eat(self):
		print("%s is eatting %s " % (self.name, self.__food))

	@eat.setter
	def eat(self, food):
		print("set food is :", food)
		self.__food = food
		print("delete done")

	@eat.deleter
	def eat(self):
		del self.__food

d = Dog("zlx")
# d.eat()
d.eat
d.eat = 'baozi'
d.eat

del d.eat
d.eat


# 属性方法
# 把一个方法变成静态属性