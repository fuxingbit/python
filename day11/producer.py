# @Time    : 2018/7/18 11:49
# @Author  : Jennings
# @Email   : zjn@wiwi.ink

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('106.14.3.173', '5672', 'test'))
# 声明一个管道
channel = connection.channel()

# 声明queue
channel.queue_declare(queue='hello', durable=True)

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello',  # queue名字
                      body='Hello World!',
                      properties=pika.BasicProperties(delivery_mode=2,)  # 消息持久化
                      )
print(" [x] Sent 'Hello World!'")
connection.close()
