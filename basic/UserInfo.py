# -*- coding: utf-8 -*-
class UserInfo(object):
    lv = 5

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print('用户名：%s, 年龄：%s, 等级：%s' % (self.name, self.age, self.lv))

    def get_name(self):
        return self.name

class UserInfo2(UserInfo):
    pass

if __name__ == '__main__':
    user2 = UserInfo2('小明', 18)
    user2.show_info()
    print(user2.get_name())