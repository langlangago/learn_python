# print(dir([]))

## 双下方法
# print([1].__add__([2]))
# print([1]+[2])

#能循环的
# list, tuple, dict, str, set , range(),  enumerate枚举, f = open()
# set1 = set(dir([])) & set(dir({})) & set(dir(range(10))) & set(dir(''))
# print(set1)

#不可迭代的
# for i in 123:
#     print(i)
# print('__iter__' in dir(int))
# print('__iter__' in dir(str))

# #只要能被for循环的，一定拥有__iter__方法
# print([].__iter__())
# #可循环的数据类型，执行了__iter__方法后，就是一个迭代器

# l = [1, 2, 3]
# iterator = l.__iter__()
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())

#可迭代协议 --> 只要含有__iter__方法的都是可迭代的
#迭代器协议 --> 内部含有__next__ 和__iter__方法的就是迭代器
# print('__next__' in dir([]))
# print('__iter__' in dir([]))
# 由上可知，列表是可迭代的，但他不是迭代器，[].__iter__才是迭代器

#迭代器的好处，省内存，一个一个取值，可以把所有值都取到。


# 生成器
# 生成器函数 -- 我们自己写的迭代器函数
# 生成器表达式lamada
