# write at 2019.3.13 16:00

# lambda  --max min filter map sorted 都有key参数

# def aad(x,y):
#     return x*y

# 函数名，定义匿名函数关键字，参数，返回值
# aad = lambda x, y: x*y
# print(aad(3, 2))


# dic = {'k1':100, 'k2':200, 'k3':300}
# print(max(dic, key=lambda x:dic[x]))

# d = lambda x: x*2
# t = lambda x: x*3
# x = 2
# x = d(x)
# x = t(x)
# x = d(x)
# print(x)


# (('a'), ('b')) [(('c'), ('d')) --> {'a':'c'}, {'b','d'}]
# 匿名函数 == 内置函数 max min sorted filter map
# zip
# t1 = (('a'), ('b'))
# t2 = (('c'), ('d'))
#
# ret = zip(t1, t2)
# # def func(t):
# #     return {t[0]:t[1]}
#
# res = map(lambda t: {t[0], t[1]}, ret)
# print(list(res))

def multipliers():
    return [lambda x: i*x for i in range(0, 4)]

print([m(2) for m in multipliers()])

# res = [lambda x: i*x for i in range(0, 4)]
#                  0*x 1*x 2*x 3*x

















