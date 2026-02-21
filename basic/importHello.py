# -*- coding: utf-8 -*-
from hello import Hello

h = Hello()
h.hello()

print(type(Hello))
print(type(h))

def printHello(self, name='py'):
    print('Hello, %s' % name)

Hello = type('Hello', (object,), dict(hello=printHello))
h = Hello()
h.hello()
print(type(Hello))
print(type(h))