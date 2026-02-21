# -*- coding: UTF-8 -*-

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
    	# Forward iterator
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
    	# Reverse iterator
        n = 1
        while n <= self.start:
            yield n
            n += 1

for rr in reversed(Countdown(30)):
    print(rr)
for rr in Countdown(30):
    print(rr)

names = ['小明', '小红', '小刚', '小李']
ages = [18, 19, 20, 21]
sex = ['男', '女', '男', '女']
for name,age,sex in zip(names,ages,sex):
    print(name,age,sex)

dict1 = dict(zip(names,ages,sex))
print(dict1)