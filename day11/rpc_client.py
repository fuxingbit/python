# @Time    : 2018/7/18 18:01
# @Author  : Jennings
# @Email   : zjn@wiwi.ink

import uuid
import pika
import time


class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('106.14.3.173', '5672', 'test'))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response,   # 只要一收到消息就调用on_response
                                   no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,  # uuid随机数，做验证
                                   ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()  # 非阻塞版的start_consuming()
            print("no message....")
            time.sleep(0.5)
        return int(self.response)


fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(6)
print(" [.] Got %r" % response)
