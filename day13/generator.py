# 只要含有yield关键字的函数，就是生成器
# yield 和 return 不用同时用

# def genarate():
#     print(1)
#     yield 'a'
#     print(2)
#     yield 'b'
#     yield 'c'

# 生成器函数，返回值是生成器
# ret =  genarate()
# print(ret)
# ret.__iter__()
# ret.__next__()
# print(ret.__next__())
# print(ret.__next__())
# print(ret.__next__())
# for i in ret:
#     print(i)

#生产20万个娃哈哈
# def wahaha():
#     for i in range(200000):
#         yield  '哇哈哈哈 %s' % i
#
# g = wahaha()
#
# for i in g:
#     print(i)
#

#取前50个娃哈哈
# def wahaha():
#     for i in range(200000):
#         yield '哇哈哈哈 %s' % i
#
#
# g = wahaha()
#
# count = 0
# for i in g:
#     count += 1
#     print(i)
#     if count > 50:
#         break
#
# print(g.__next__())

# for 循环内部生成了一个迭代器
# l = [1, 2, 3, 4]
# for i in l:
#     print(i)


