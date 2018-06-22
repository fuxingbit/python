# @Time    : 2018/6/19 17:17
# @Author  : Jennings
# @Email   : zjn@wiwi.ink


class Role(object):
    n = 0    #类变量
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        '''
        构造函数，在实例化时做一些类的初始化操作。
        :param name:
        :param role:
        :param weapon:
        :param life_value:
        :param money:
        '''
        self.name = name          #实例变量（静态属性），作用域就是实例本身
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self):                    #类的方法、功能，（动态属性）
        print("shooting...")

    def got_shot(self):
        print("ah...,I got shot...")

    def buy_gun(self, gun_name):
        print("just bought %s" % gun_name)

print(Role.n)


# 生成一个角色
r1 = Role('Alex', 'police', 'AK47')
# del r1.weapon
print(r1.n, r1.name)
# 生成一个角色
r2 = Role('Jack', 'terrorist', 'B22')
