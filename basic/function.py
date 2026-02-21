def sum(num1,num2):
	"两数之和"
	return num1+num2

# 调用函数
print(sum(5,6))

def sum(num1,num2):
    if not (isinstance(num1,(int,float)) and isinstance(num2,(int,float))):
        raise TypeError("参数必须是数字")
    return num1+num2
print(sum(1,2))

def division(num1,num2):
    a = num1 % num2
    b = (num1 - a) / num2
    return b,a

num1,num2 = division(9,4)
tuple1 = division(9,4)
print(num1,num2)
print(tuple1)

def print_user_info(name,age,sex='零'):
    print('姓名：{}'.format(name),end=' ')
    print('年龄：{}'.format(age),end=' ')
    print('性别：{}'.format(sex))
    return;

print_user_info('小明',19,'男')
print_user_info('小红',18)

def print_user_info(name,age,sex,* hobby):
    print('姓名：{}'.format(name),end=' ')
    print('年龄：{}'.format(age),end=' ')
    print('性别：{}'.format(sex),end=' ')
    print('爱好：{}'.format(hobby))
    return;

print_user_info('小明',19,'男','篮球','足球')

def print_user_info(name,age,sex,** hobby):
    print('姓名：{}'.format(name),end=' ')
    print('年龄：{}'.format(age),end=' ')
    print('性别：{}'.format(sex),end=' ')
    print('爱好：{}'.format(hobby))
    return

print_user_info(name = '小明',age = 19,sex = '男',hobby = ('篮球','足球','游泳','跑步'))

def print_user_info( name , *, age  , sex = '男' ):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex))
    return;

# 调用 print_user_info 函数
print_user_info( name = '两点水' ,age = 18 , sex = '女' )

# 这种写法会报错，因为 age ，sex 这两个参数强制使用关键字参数
# print_user_info( '两点水' , 18 , '女' )
print_user_info('两点水',age='22',sex='男')

sum = lambda num1,num2 : num1 + num2
print(sum(1,2))