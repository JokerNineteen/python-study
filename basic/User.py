# -*- coding: utf-8 -*-
class User(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def printUser(self):
        print('用户姓名：%s, 用户年龄：%s, 用户性别：%s' % (self.name, self.age, self.sex))

class UserVip(User):
    def printUser(self):
        print('Hello!快来瞅瞅啊这里有个vip:' + self.name)

class UserGeneral(User):
    def printUser(self):
        print('欢迎来到这里:' + self.name)

def printUser(user):
    user.printUser()

if __name__ == '__main__':
    user = User('小明', 18, '男')
    userVip = UserVip('小王', 19, '男')
    userGeneral = UserGeneral('小李', 20, '女')
    printUser(user)
    printUser(userVip)
    printUser(userGeneral)