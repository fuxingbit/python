# @Time     :2018/7/14 下午10:15
# @Author   :Jennings
# @Email    :zjn@wiwi.ink

import threading, time


def run(n):
	print("task: ", n)
	time.sleep(2)
	print("task done", n, threading.current_thread())


start_time = time.time()
t_obls = []   # 存线程实例

for i in range(50):
	t = threading.Thread(target=run, args=("t-%s" % i,))
	t.setDaemon(True)  # 把当前线程设置为守护线程
	t.start()
	t_obls.append(t)  # 为了不阻塞后面线程的启动，不在这里join，先放到一个列表里


# for t in t_obls:  #循环线程实例列表，等待所有线程执行完毕
# 	t.join()

time.sleep(2)

print("----------all threads has finished....--------", threading.current_thread(), threading.active_count())
print("cost:", time.time()-start_time)

# run("t1")
# run("t2")
