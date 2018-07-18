# @Time    : 2018/7/18 11:55
# @Author  : Jennings
# @Email   : zjn@wiwi.ink

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    '106.14.3.173', '5672', 'test'))
channel = connection.channel()


channel.queue_declare(queue='hello', durable=True)  # durable=True 队列持久化


def callback(ch, method, properties, body):
    print(ch, method, properties)
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 确认


channel.basic_qos(prefetch_count=1)  # 按机器处理速度分配，不轮训
# 消费消息
channel.basic_consume(callback,  # 如果收到消息，就调用callback函数来处理消息
                      queue='hello',
                      # no_ack=True,   # no acknowledge,处不处理完都不给服务器发信息确认
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()