# -*- coding: utf-8 -*-


class User(object):
    def __new__(cls, *args, **kwargs):
        print('__new__被调用')
        print(args)
        return super(User,cls).__new__(cls)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'User: %s, %s' % (self.name, self.age)

    def __getattr__(self, name):
        print('__getattr__被调用')
        return super(User, self).__getattr__(name)
    def __setattr__(self, name, value):
        print('__setattr__被调用')
        return super(User, self).__setattr__(name, value)
    def __delattr__(self, name):
        print('__delattr__被调用')
        return super(User, self).__delattr__(name)
    def __getattribute__(self, name):
        print('__getattribute__被调用')
        return super(User, self).__getattribute__(name)

if __name__ == '__main__':
    print(dir(User('三疯',19)))
    user = User('三疯',19)
    # 设置属性值，会调用 __setattr__
    user.attr1 = True
    # 属性存在,只有__getattribute__调用
    user.attr1
    try:
        # 属性不存在, 先调用__getattribute__, 后调用__getattr__
        user.attr2
    except AttributeError:
        pass
    # __delattr__调用
    del user.attr1

user = User('三疯',19)