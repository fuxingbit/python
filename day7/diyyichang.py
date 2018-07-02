# @Time    : 2018/7/2 20:32
# @Author  : Jennings
# @Email   : zjn@wiwi.ink

class ZjnException(Exception):
    def __init__(self, msg):
        self.message = msg
    # def __str__(self):
    #     return self.message


try:
    raise ZjnException('我的异常')
except ZjnException as e:
    print(e)
