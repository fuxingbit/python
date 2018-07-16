# @Time     :2018/7/16 下午9:55
# @Author   :Jennings
# @Email    :zjn@wiwi.ink

from multiprocessing import Process, Lock

# 20个进程在共享同一块屏幕，不加锁可能输出会乱

def f(l, i):
	l.acquire()
	try:
		print('hello world', i)
	finally:
		l.release()


if __name__ == '__main__':
	lock = Lock()

	for num in range(20):
		Process(target=f, args=(lock, num)).start()
