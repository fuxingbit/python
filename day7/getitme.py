# @Time     :2018/7/1 下午7:57
# @Author   :Jennings
# @Email    :zjn@wiwi.ink


class Foo(object):

	def __getitem__(self, key):
		print('__getitem__', key)

	def __setitem__(self, key, value):
		print('__setitem__', key, value)

	def __delitem__(self, key):
		print('__delitem__', key)


obj = Foo()

result = obj['k1']  # 自动触发执行 __getitem__
obj['k2'] = 'alex'  # 自动触发执行 __setitem__
del obj['k1']