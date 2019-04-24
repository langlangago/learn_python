# li = ['Tom', 'Jack', 'Alex']

# CURL append insert extend
# while  1:
#     s = input('name or quit :').strip()
#     if  s == 'quit':
#         break;
#     else:
#         li.append(s)
#
# print(li)

# li.insert(1, 'Lili')
# li.extend('LiLi')
# print(li)

# delete remove clear del
# print(li.pop(1))
# print(li)

# li.remove('Alex')
# print(li)

# li.clear()
# print(li)

# del li
# del li[-1]
# print(li)

# update
#li[0] = 'LangXiaowei'
# li[0:2] = [1, 2, 3, 'Haha', 'Lili'] # 可迭代
# print(li)

# select
# for i in li:
#     print(i)

# normal methods
# print(len(li))
# print(li.count('Alex'))
# print(li.index('Alex'))

# sort
# li = [1,9, 5, 2, 6, 8, 0]
# #li.sort()
# #li.sort(reverse=True)
# li.reverse()
# print(li)


li = ['jack', 'alex', 123, ['lili', 'lilei']]
print(li[1][1])
li[0] = li[0].capitalize()
print(li)
li[1] = li[1].replace('l', 'lll')
print(li)
print(li[3][1])












