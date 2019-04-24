# 写于 2019.03.05 17:46

# 生成器取值的方法有：__next__(), for , 强制类型转换list(iterator), send()
# 生成器取值的另一个方法：send()函数
# def generate():
#     print(1)
#     message = yield 'a'
#     print(message)
#     print(2)
#     yield 'b'
#
# g = generate()
# ret = g.__next__()
# print(ret)
# ret = g.send('QQ')
# print(ret)

# send 获取下一个值的效果和next基本一致
# send 在获取下一个值的同时，给上一个yield位置传递一个数据
# 使用send注意事项：
# 在第一次使用生成器的时候，用的是__next__获取值；最后一个yield不能接受外部的值。

# 移动平均值，比如：打枪，5抢总共几环，平均值几环；6枪总共几环，平均值几环。
# 每增加一个数，算一下平均值。

# 例子：10 20 30 40
# avg: 10 15 20 25


#预激活生成器的装饰器

# def init(func):
#     def inner(*args, **kwargs):
#         g = func(*args, **kwargs)
#         g.__next__()
#         return g
#     return inner
#
# @init  # generate = init(generate) = inner
# def generate():
#     count = 0
#     sum = 0
#     avg = 0
#     while True:
#         num = yield avg
#         sum += num
#         count += 1
#         avg = sum/count
#
# avg_g = generate()
# avg1 = avg_g.send(10)
# print(avg1)
# avg2 = avg_g.send(20)
# print(avg2)
# avg3 = avg_g.send(30)
# print(avg3)


#python3, yield from

def generate():
    a = 'abcde'
    b = '12345'
    yield from a
    yield from b

g = generate()
for i in g:
    print(i)
