# @Time     :2018/7/14 下午10:15
# @Author   :Jennings
# @Email    :zjn@wiwi.ink

import threading
import time


class MyThread(threading.Thread):
	def __init__(self, n, sleep_time):
		# threading.Thread.__init__(self)
		super(MyThread, self).__init__()
		self.n = n
		self.sleep_time = sleep_time


	def run(self):  # 定义每个线程要运行的函数

		print("running task:%s" % self.n)
		time.sleep(self.sleep_time)
		print("task done:", self.n)



t1 = MyThread("t1", 2)
t2 = MyThread("t2", 4)
t1.start()
t2.start()

t1.join()

print("main theard....")
