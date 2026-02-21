class ClassA():
    var1 = '三疯'

    @classmethod
    def fun1(cls):
        print('原来的var1值：' + cls.var1)
        cls.var1 = '三疯1'
        print('修改后的var1值：' + cls.var1)
        cls.var2 = '三疯2'
        print('添加的var2值：' + cls.var2)

ClassA.fun1()

class ClassB(object):
    var1 = '三疯'

    def fun1(self):
        print('原来的var1值：' + self.var1)

a = ClassB()
a.fun1()

def newFun1(self):
    print('性别男，爱好女')

ClassB.fun1 = newFun1

a.fun1()