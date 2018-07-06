# @Time    : 2018/7/2 19:49
# @Author  : Jennings
# @Email   : zjn@wiwi.ink

class Dog(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eatting ...%s " % (self.name, food))


def bulk(self):
    print("%s is yelling...." % self.name)


# d = Dog("Alex")
# choice = input(">>>>:").strip()
# getattr(d, choice)

name = ['alex', 'jack']
data = {}
try:
    # data['name']
    # name[2]
    # open("test.txt")
    a = 1
    print(a)

except KeyError as e:
    print("没有这个key", e)
except IndexError as e:
    print("列表操作错误", e)
except Exception as e:
    print("未知错误", e)
else:
    print("一切正常")

finally:
    print("不管有错没错，都执行")

# except Exception as e:# 抓住所有错误
# #     print("出错了", e)
