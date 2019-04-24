# write at 2019.3.10 17:00

# reversed 函数，返回一个反向的迭代器，保留原列表。
# l = [1, 2, 3, 4]
# # l.reverse()
# # print(l)
# l2 = reversed(l)
# print(l2)

# slice 切片，不好用
# l = [1,2,3,4,5,6]
# sli2 = slice(1,5,2)
# print(l[sli2])
# print(l[1:5:2])

# bytes 转换成bytes类型，二进制字节流
# print(bytes('你好', encoding='GBK').decode('GBK'))  # str --> bytes --> str  unicode --> GBK
# print(bytes('你好', encoding='UTF-8'))              # str --> bytes  unicode --> utf8

# python中字符文件是以str保存的，照片和视频等二进制文件以bytes类型存储
# 网络编程，只能传二进制bytes
# html 爬取到的内容也是bytes

# bytearray 字节数组，方便修改某个字节的内容
# b_array = bytearray('你好', encoding='UTF-8')
# print(b_array[0])

# repr 输出原类型的数据 %r
# i = 'egg'
# print('HAHA%r' % i)
# print(repr('1'))
# print(repr(1))


# all() 只要有一个是假，整体就是False
# print(all([1,2,0]))
# print(all([1,2,[]]))
# print(all([1,2,'abc']))

# any()  可迭代对象中，只要有一个真，结果就是True
# print(any([True,0,[]]))


## zip 拉链函数
#l1 = [1, 2, 3, 4]
#l2 = ['a,', 'b', 'c', 'd']
#print(zip(l1,l2))
#for i in zip(l1,l2):
#    print(i)

# filter 过滤，拿真值
#def is_odd(x):
#    return x % 2 == 1
#
#li = filter(is_odd, [1,2,3,4,5,6,7])
#for i in li:
#    print(i)
#
#ret = [i for i in [1,2,3,4,5,6,7] if i % 2 == 1]
#print(ret)


#import math
#def func(x):
#    return math.sqrt(x) % 1 == 0
#
#ret = filter(func, range(1,101))
#for i in ret:
#    print(i)
#
## map 映射，将可迭代的数据代入前面的函数，然后返回经函数处理后的值
#ret = map(abs, [1,-2,4,-5,7])
#for i in ret:
#    print(i)






# sort

# l = [1, -2, 5, -10, 7]
# print(sorted(l,key=abs))
# print(sorted(l,key=abs,reverse=True))
#
# l2 = ['', 'Hello word!',[1,2,3]]
# print(sorted(l2,key=len))

# max 求可迭代的参数的最大值，
# key，一次循环可迭代参数的每个值，送到key=lambda进行计算，将结果返回给key，以key的值为标准算最大值
# d1 = {'name': 'egon', 'price': 100}
# d2 = {'name': 'rdw', 'price': 666}
# d3 = {'name': 'zat', 'price': 1}
#
# l1 = [d1, d2, d3]
# a = max(l1, key=lambda x: x['name'])
# b = max(l1, key=lambda x: x['price'])
# print(a)
# print(b)














