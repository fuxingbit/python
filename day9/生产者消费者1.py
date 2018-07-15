# @Time     :2018/7/15 下午4:45
# @Author   :Jennings
# @Email    :zjn@wiwi.ink

import threading, time
import queue

q = queue.Queue(maxsize=10)


def producer():
	count = 1
	while True:
		q.put("骨头 %s" % count)
		print("生产了骨头",count)
		count += 1
		time.sleep(0.5)


def consumer(name):
	# while q.qsize() > 0:
	while True:
		print("%s 取到 [%s] 并且吃了它。。" % (name, q.get()))
		time.sleep(1)


p = threading.Thread(target=producer, )
c = threading.Thread(target=consumer, args=("zlx",))
c1 = threading.Thread(target=consumer, args=("zdd",))
p.start()
c.start()
c1.start()
