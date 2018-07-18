# @Time    : 2018/7/18 16:01
# @Author  : Jennings
# @Email   : zjn@wiwi.ink

# 不同的消费者接受特定的消息
# 启动时加消息级别，python direct_publisher.py error

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('106.14.3.173', '5672', 'test'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()