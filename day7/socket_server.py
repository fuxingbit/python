# @Time     :2018/7/5 下午11:04
# @Author   :Jennings
# @Email    :zjn@wiwi.ink

import os
import socket

server = socket.socket()
server.bind(('localhost', 6960))  # 绑定端口
server.listen(5)  # 监听,最多5个链接

print("开始等待链接")

while True:
    conn, addr = server.accept()  # 等客户端消息
    # conn 就是客户端连过来而在服务器端为其生成的一个连接实例
    print(conn, addr)
    print("等到了链接")

    while True:
        data = conn.recv(1024)
        print('recv:', data.decode())
        if not data:
            print("client has lost.....")
            break
        # res = os.popen(data).read()
        conn.send(data.upper())
        # conn.sendall(res)

server.close()
