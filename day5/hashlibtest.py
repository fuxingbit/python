# @Time    : 2018/6/1419:24
# @Author  : Jennings
# @Email   : zjn@wiwi.ink

import hashlib

import hmac

# m = hashlib.md5()
# m.update(b'admin')
# print(m.hexdigest())
#
# s = hashlib.sha512()
# s.update(b'admin')
# print(s.hexdigest())

import hmac
h = hmac.new(b'12345', '宝塔镇河妖'.encode(encoding="utf-8"))
print(h.hexdigest())
