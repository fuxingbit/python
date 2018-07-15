# @Time     :2018/7/14 下午10:15
# @Author   :Jennings
# @Email    :zjn@wiwi.ink

import threading, time


def run(n):
	lock.acquire() # 获取锁
	global num
	num += 1
	time.sleep(1)
	lock.release() # 释放锁


# 3.x加不加锁都行，2.x 要加锁
lock = threading.Lock()
num = 0

start_time = time.time()
t_obls = []   # 存线程实例

for i in range(50):
	t = threading.Thread(target=run, args=("t-%s" % i,))
	t.start()
	t_obls.append(t)  # 为了不阻塞后面线程的启动，不在这里join，先放到一个列表里


for t in t_obls:  #循环线程实例列表，等待所有线程执行完毕
	t.join()

print("----------all threads has finished....--------", threading.current_thread(), threading.active_count())
print("num:", num)

