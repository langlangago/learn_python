
# print('\n b')
# print(r'\n b')


import re

# findall 从前往后找到所有匹配项，并返回给list
# ret = re.findall('[a-z]*', 'we are familly')
# print(ret)

# .*?x  直到匹配到x停止匹配
#ret = re.findall('.*?x', 'aaaaaaaxbbbb')
#print(ret)

# search 从前往后找到第一个就返回，返回值调用group方法。如果没找到就返回None，没有group方法
# ret = re.search('a', 'we are familly')
# if ret:
#     print(ret.group())

# match 从头开始匹配，匹配到就返回，并调用group方法。如果从头没匹配上，返回None
# ret = re.match('w', 'we are familly')
# if ret:
#     print(ret.group())

# split 分割
# ret = re.split('[ab]', 'abcd')
# print(ret)

# sub 替换, 替换n次
# ret = re.sub('\d', 'H', 'B2B B2C', 1)
# # print(ret)
#
# # subn, replace, return tuple
# ret = re.subn('\d', 'H', 'B2B B2C')
# print(ret)

# finditer ,return a iter
# ret = re.finditer('\d', 'B2B3B2C')
# for i in ret:
#     print(i.group())
