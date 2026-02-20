print("helloKitty")
age = 19
user_name = "nineteen"
_total = 1024
MAX_SIZE = 10240
姓名 = "张三"  # 合法
π = 3.14159   # 合法

def is_valid_identifier(name):
    try:
        exec(f"{name} = None")
        return True
    except:
        return False

print(is_valid_identifier("2var"))
print(is_valid_identifier("var2"))

#!/usr/bin/python3
 
x="a"
y="b"
# 换行输出
print( x )
print( y )
 
print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()

list1 = ["Google","runoob",1998, 2025]
list2 = [ 1,2,3,4]
list3 = ["a","b","c","d"]
list4 = ['red','blue','white']
print(list1[0])
print(list2[1])
print(list3[3])
print(list1[-1])
print(list2[-2])
print(list3[-3])

print(list1[0:2])