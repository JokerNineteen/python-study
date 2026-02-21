# -*- coding: utf-8 -*-
for char in 'Hello Kitty':
    print(char, end = '')
print('\n')

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list1:
    print(i, end = ' ')
print('\n')

dict1 = {'小明':'13812345678', '小红':'1381234567', '小刚':'1381234566', '小李':'1381234565'}

for key in dict1:
    print(key,end=' ')

print('\n')

for value in dict1.values():
    print(value, end = ' ')

print('\n')

for x , y  in [('小明','13812345678'), ('小红','1381234567'), ('小刚','1381234566'), ('小李','1381234565')]:
    print(x, y)
