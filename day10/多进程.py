# @Time     :2018/7/15 下午8:45
# @Author   :Jennings
# @Email    :zjn@wiwi.ink

import multiprocessing
import time, threading


def thread_run():
	print(threading.get_ident())


def run(name):
	time.sleep(1)
	print('hello', name)
	t = threading.Thread(target=thread_run,)
	t.start()


if __name__ == '__main__':
	for i in range(10):
		p = multiprocessing.Process(target=run, args=('bob %s' % i, ))
		p.start()
	# p.join()
