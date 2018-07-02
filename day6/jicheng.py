# @Time    : 2018/6/25 16:53
# @Author  : Jennings
# @Email   : zjn@wiwi.ink


# class People:(经典类)
class People(object):  # 新式类
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def eat(self):
        print("%s is eatting...." % self.name)

    def sleep(self):
        print("%s is sleeping...." % self.name)


class Relation(object):
    def __init__(self, n1, n2):
        print("init in relation")

    def make_friends(self, obj):
        print("%s making friend with %s " % (self.name, obj.name))
        self.friends.append(obj.name)


class Man(People, Relation):
    def __init__(self, name, age, money):
        # 给Man新加一个参数
        # People.__init__(self, name, age)
        super(Man, self).__init__(name, age)  # 新式类写法

        self.money = money
        print("%s 一出生就有 %s 块钱" % (self.name, self.money))

    def piao(self):
        print("%s is piaoing....." % self.name)

    def sleep(self):  # 重构
        People.sleep(self)
        print("Man is sleeping....")


class Woman(People, Relation):
    def get_birth(self):
        print("%s is born a baby ....." % self.name)


m1 = Man("Jennins", 22, 10)

# m1.eat()
# m1.piao()
# m1.sleep()

# w1 = Woman("Alex", 27)
# # w1.get_birth()
#
# m1.make_friends(w1)
# w1.name = "cheng3pao"
# print(m1.friends[0])


# python2 的经典类按深度优先继承，新式类按广度优先来继承
# python3 经典类和新式类都按广度优先继承
