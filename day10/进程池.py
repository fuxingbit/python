# @Time     :2018/7/16 下午10:53
# @Author   :Jennings
# @Email    :zjn@wiwi.ink

from multiprocessing import Process, Pool
import time, os


def Foo(i):
	time.sleep(2)
	print("In process", os.getpid())
	return i + 100


def Bar(arg):
	print('-->exec done:', arg, os.getpid())


pool = Pool(5) # 允许进程池中同时运行5个进程

for i in range(10):
	pool.apply_async(func=Foo, args=(i,), callback=Bar)  # 并行   callback 回调
# pool.apply(func=Foo, args=(i,))   # 串行
print(os.getpid())
print('end')
pool.close()
pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。