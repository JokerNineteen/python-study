# -*- coding: utf-8 -*-
class User(object):
    def __init__(self, name = '三疯', age = 19):
        self.name = name
        self.age = age

    def __get__(self, instance, owner):
        print('获取name')
        return self.name
    def __set__(self, instance, value):
        print('设置name')
        self.name = value

class example(object):
    user = User('三疯',88)
    y = 5

if __name__ == '__main__':
    m = example()
    print(m.user)

    print('\n')

    m.user = '十九'
    print(m.user)

    print('\n')

    print(m.user)

    print('\n')

    print(m.y)