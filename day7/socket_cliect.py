# @Time     :2018/7/5 下午10:58
# @Author   :Jennings
# @Email    :zjn@wiwi.ink

import socket

client = socket.socket()  # 声明socket类型，同时生成docket连接对象

client.connect(('localhost', 6969))

# client.send(b'hello world')

while True:

	msg = input('>>>:').strip()
	client.send(msg.encode())

	data = client.recv(1024)

	print("recv:", data.decode())

client.close()
