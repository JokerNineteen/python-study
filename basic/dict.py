names = ['小明', '小红', '小刚', '小李']

# names_dict = [['小明','13812345678'], ['小红','1381234567'], ['小刚','1381234566'], ['小李','1381234565']]

names_dict = {'小明':'13812345678', '小红':'1381234567', '小刚':'1381234566', '小李':'1381234565'}
print(names_dict['小明'])

names_dict['三疯'] = '13812345674'
print(names_dict)
names_dict['小明'] = '2'
print(names_dict)

del names_dict['小明']
print(names_dict)
names_dict.clear()
print(names_dict)
del names_dict