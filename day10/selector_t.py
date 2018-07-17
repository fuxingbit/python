# @Time    : 2018/7/17 18:09
# @Author  : Jennings
# @Email   : zjn@wiwi.ink

import selectors
import socket

sel = selectors.DefaultSelector()


def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)  # 新连接注册 read 回调函数


def read(conn, mask):
    data = conn.recv(1024)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn, mask)
        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


sock = socket.socket()
sock.bind(('localhost', 10000))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()  # 默认阻塞，有活动连接就返回活动的连接列表
    for key, mask in events:
        callback = key.data  # accept
        callback(key.fileobj, mask)  # key.fileobj = 文件句柄