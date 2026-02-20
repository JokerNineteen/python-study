name1 = '小明'
name2 = '小红'
name3 = '小刚'
name4 = '小李'

names = ['小明', '小红', '小刚', '小李']
print(names[0])  # 输出列表中的第一个元素
print(names[0:2])
print(names[:2])
print(names[1:2])

names.append('小王')  # 在列表末尾添加一个元素
print(names)

del(names[0])  # 删除列表中的第一个元素
print(names)

user = ['小明', 18, '男', '学生']
print('用户姓名：', user[0])
print(user)

print('用户信息的长度：', len(user))

print(user[0], user[1], user[2], user[3])

user.insert(0, 'ID001')  # 在列表的开头插入一个元素
print(user)

user.pop()
print(user)

user.pop(1)  # 删除列表中的第二个元素
print(user)

user[2] = '女'  # 修改列表中的第三个元素
print(user)

newUser = [['小明', 18, '男', '学生'], ['小红', 19, '女', '学生'], ['小刚', 20, '男', '学生'], ['小李', 21, '女', '学生']]
print(newUser)
