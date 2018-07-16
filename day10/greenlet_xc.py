# @Time     :2018/7/16 下午11:56
# @Author   :Jennings
# @Email    :zjn@wiwi.ink

from greenlet import greenlet


def test1():
	print(12)
	gr2.switch()
	print(34)
	gr2.switch()


def test2():
	print(56)
	gr1.switch()
	print(78)


gr1 = greenlet(test1) # 启动一个协程
gr2 = greenlet(test2)
gr1.switch()