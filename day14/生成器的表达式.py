# 写于2019.3.8 15:40

# 列表推导式
# egg_list = ['鸡蛋%s' % i for i in range(10)]
# print(egg_list)
#
# print([i for i in  range(10)])
# print([i*2 for i in range(10)])

# 生成器表达式

# g = (i for i in range(10))
# print(g)
# for i in g:
#     print(i)

# 区别：扣号不一样；返回值不一样，不占内存。

# 各种推导式

# 完整的列表推导式
# mod_3 = [i for i in range(30) if i%3 ==0 ]
# print(mod_3)

# g = (i*i for i in range(30) if i%3 ==0)
# for i in g:
#     print(i)

# 取嵌套列表中，含有两个e的名字
# names = [['Jeery', 'Tim', 'Lee'],['Hee', 'Lili']]
# ret = [name for l in names for name in l if name.count('e') == 2]
# print(ret)

#字典推导式
# 交换key和value
# mcase = {'a':10, 'b':20}
# ret = {mcase[k]:k for k in mcase}
# print(ret)

# 合并字典中大小写的value
# mcase = {'a': 10, 'b': 20, 'c': 30, 'A': 40}
# ret = {k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase}
# print(ret)

# 集合推导式, 自带去重功能
ret = {i**2 for i in [1, -2, 2]}
print(ret)







