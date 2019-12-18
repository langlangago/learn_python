# encoding:utf-8

# __str__, __repr__ 用于解释说明，看起来好懂一点
# str() 转换成字符串 ，== __str__
# repr() 原形毕露，原形显示,==  __repr__
# print(1, '1')
# print(repr(1), repr('1'))

# class Teacher:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return 'This is a Teacher object:%s' % self.__dict__
#      def __repr__(self):
#         return str(self.__dict__)
#
# alex = Teacher('alex', 22)
# print(alex) # print一个对象的时候，就是调用a.__str__方法
# # 如果类没有自己的__str__方法，就调用父类(object)的__str__方法
# print(repr(alex))
# object里有一个__str__方法，一旦被调用就返回这个方法的内存地址
# l = [1, 2, 3, 4] #  l 是list类的一个对象，list类里重新实现了__str__方法，让print后看起来好看一点。
# print(l)

# %s str() print 实际上走的都是__str__
# %r repr() 实际上都是走的__repr__
# __str__没有的时候，可以使用__repr__; __repr__没有的时候，不能使用__str__，就只能使用父类的__repr__

# print(obj), str(), %s 的时候，实际上都是调用了内部的__str__方法，那么他返回的必定是一个字符串；
# 如果自己类中没有__str__方法，会先找自己类中的__repr__替代，如没有__repr__方法，就只能使用父类object的__str__
# repr(),%r 会找__repr__，如果没有，直接找父类的。


# __len__ --> len()
#内置方法有很多，不一定都在object里
#比如，不是所有的对象都能求长度len,所以可以自己实现自己的len
#  class Classes:
#      def __init__(self, name, student):
#          self.name = name
#          self.student = []
#      def __len__(self):
#          return len(self.student)
#      def __str__(self):
#          return 'classes'
#  py_s9 = Classes('python全栈9期', [])
#  py_s9.student.append('alex')
#  py_s9.student.append('tom')
#  print(len(py_s9))
#  print(py_s9)

# __del__
# 析构函数，再删除一个对象之前进行一些收尾工作
# class A:
#    def __del__(self, f):
#        self.f.close()
# a = A()
# a.f = open() # 打开文件 1、 在操作系统中打开了一个文件，2、拿到了文件句柄并放入内存
# del a # 拿到文件句柄，既执行了方法（关闭了文件），又删除了文件句柄

# __call__ ,--> () 相当于调用__call__内置方法
class A:
    def __init__(self,name):
        self.name = name
    def __call__(self):
        '''
        打印这个对象中的所有属性
        :return:
        '''
        for k in self.__dict__:
            print(k,self.__dict__[k])
a = A('alex')()  # 可调用,()相当于执行 __call__内置方法













