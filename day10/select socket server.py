# @Time    : 2018/7/17 15:58
# @Author  : Jennings
# @Email   : zjn@wiwi.ink

import select
import socket
import queue

server = socket.socket()
server.bind(('localhost', 9009))
server.listen(100)

server.setblocking(False)  # 不阻塞

msg_dic = {}
inputs = [server, ]
# inputs = [server, conn]
outputs = []

while True:
    readable, writeable, exceptional = select.select(inputs, outputs, inputs)
    print(readable, writeable, exceptional)

    for r in readable:
        if r is server:  # 代表来了一个新连接
            conn, addr = server.accept()
            print("来了个新连接", addr)
            inputs.append(conn)  # 是因为这个新建立的连接还没发数据过来，现在就接受的话程序就报错了,
            # 所以要想实现这个客户端发数据来时server端能知道，就需要让select 在监测这个conn
            msg_dic[conn] = queue.Queue()  # 初始化一个队列，后面存要返回给这个客户端的数据
        else:
            data = r.recv(1024)
            if data:
                print("收到数据", data)
                msg_dic[r].put(data)

                if r not in outputs:
                    outputs.append(r)  # 放入返回的连接队列里
                # r.send(data)
                # print("send done .....")
            else:
                print("客户端断开了", r)

                if r in outputs:
                    outputs.remove(r)  # 清理已断开的连接

                inputs.remove(r)  # 清理已断开的连接

                del msg_dic[r]  # 清理已断开的连接

    for w in writeable:  # 要返回给客户端的连接列表
        try:
            # w.send(msg_dic[w].get())  # 返回给客户端原数据
            next_msg = msg_dic[w].get_nowait()
        except queue.Empty:
            print("queue is empty...")
            outputs.remove(w)  # 确保下次循环的时候writeable,不返回这个已经处理完的连接
        else:
            print("sending msg .....", next_msg)
            w.send(next_msg)

    for e in exceptional:
        if e in outputs:
            outputs.remove(e)
        e.close()
        inputs.remove(e)
        del msg_dic[e]
