from operator import truediv

str1 = 'Hello Kitty'
iter1 = iter(str1)

list1 = [1,2,3,4,5,6,7,8,9,10]
iter2 = iter(list1)

tuple1 = (1,2,3,4,5,6,7,8,9,10)
iter3 = iter(tuple1)
# for 循环遍历迭代器对象
for x in iter1 :
    print ( x , end = ' ' )

print('\n')

for x in iter2 :
    print ( x , end = ' ' )

print('\n')

while True:
    try:
        print(next(iter3), end = ' ')
    except StopIteration:
        break