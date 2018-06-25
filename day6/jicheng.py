# @Time    : 2018/6/25 16:53
# @Author  : Jennings
# @Email   : zjn@wiwi.ink


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eatting...." % self.name)

    def sleep(self):
        print("%s is sleeping...." % self.name)


class Man(People):
    def piao(self):
        print("%s is piaoing....." % self.name)

    def sleep(self):  # 重构
        People.sleep(self)
        print("Man is sleeping....")


class Woman(People):
    def get_birth(self):
        print("%s is born a baby ....." % self.name)


m1 = Man("Jennins", 22)

m1.eat()
m1.piao()
m1.sleep()

w1 = Woman("Alex", 27)
w1.get_birth()