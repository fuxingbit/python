# @Time     :2018/7/14 下午10:15
# @Author   :Jennings
# @Email    :zjn@wiwi.ink

import threading, time


def run(n):
	print("task: ", n)
	time.sleep(2)
	print("task done", n)


start_time = time.time()
t_obls = []

for i in range(50):
	t = threading.Thread(target=run, args=("t-%s" % i,))
	t.start()
	t_obls.append(t)


for t in t_obls:
	t.join()


print("----------all threads has finished....--------")
print("cost:", time.time()-start_time)
