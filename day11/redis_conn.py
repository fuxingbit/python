# @Time    : 2018/7/18 17:10
# @Author  : Jennings
# @Email   : zjn@wiwi.ink

import redis

pool = redis.ConnectionPool(host='106.14.3.173', port=6379)
r = redis.Redis(connection_pool=pool)
r.set('name', 'zlx')
print(r.get('name'))
