# @Time     :2018/7/18 下午11:04
# @Author   :Jennings
# @Email    :zjn@wiwi.ink

from redis_helper import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe()

while True:
	msg = redis_sub.parse_response()
	print(msg)