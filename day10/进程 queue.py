# @Time     :2018/7/15 下午9:27
# @Author   :Jennings
# @Email    :zjn@wiwi.ink

from multiprocessing import Process, Queue


def f(qq):
	qq.put([42, None, 'hello'])


if __name__ == '__main__':
	q = Queue()
	p = Process(target=f, args=(q,))
	p.start()
	print(q.get())  # prints "[42, None, 'hello']"
	p.join()


# 进程间通讯