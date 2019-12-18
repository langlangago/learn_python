#! encoding:utf-8

# 反射，字符串直接当变量名或者函数名用，直接调用。
# hasattr,getattr,delattr
class Teacher:
    dic = {'查看学生信息':'show_student', '查看讲师信息':'show_teacher'}
    def show_student(self):
        print('Show student.')
    def show_teacher(self):
        print('Show teacher.')
    @classmethod    #强制一个方法变成类的方法
    def foo(cls):
        print('Hahaha.')

if hasattr(Teacher, 'dic'):
    ret = getattr(Teacher, 'dic')   #Teacher.dic 类名.属性；字符串和属性名相同
    print(ret)
if hasattr(Teacher, 'foo'):
    ret2 = getattr(Teacher, 'foo')  #Teacher.foo 类名.方法：字符串和方法名相同
    print(ret2)
    ret2()

alex = Teacher()
for ke in Teacher.dic:
    print(ke)
key = input('输入需求:')
print(Teacher.dic[key]) # 字符串和方法名相同
ret3 = getattr(alex, Teacher.dic[key])  # getattr的返回值，如果是属性那就返回值，如果是方法那么返回方法的地址（名）
ret3()  # 方法的地址（名字），加上括号就能调用了。

# 通过反射
# 对象名 获取对象属性 和 普通方法
# 类名  获取 静态属性，静态方法，类方法

# 普通方法 self
# 静态方法 @staticmethod
# 类方法 @classmethod
# 属性方法 @property
