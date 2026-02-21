#--*- coding: utf-8 -*-
tuple1 = ('001', '002', '003')
tuple2 = 'a', 'b', 'c'
tuple3 = ()
tuple4 = (1,)
print(tuple1[1])

names1 = ['小明', '小红', '小刚', '小李']
tuple6 = ('姓名', '年龄', '性别', '职业', names1)
print(tuple6)
names1[0] = '小王'
print(tuple6)

name1 = ('一点水', '两点水', '三点水', '四点水', '五点水')

name2 = ('1点水', '2点水', '3点水', '4点水', '5点水')

list1 = [1, 2, 3, 4, 5]

# 计算元素个数
print(len(name1))
# 连接,两个元组相加
print(name1 + name2)
# 复制元组
print(name1 * 2)
# 元素是否存在 (name1 这个元组中是否含有一点水这个元素)
print('一点水' in name1)
# 元素的最大值
print(max(name2))
# 元素的最小值
print(min(name2))
# 将列表转换为元组
print(tuple(list1))