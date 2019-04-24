# = is point to a sam addr; copy is copy the first layer ,to a new addr
#deepcopy is copy more  than one layer,  all to a new  addr

# =
# l1 = [1, 2, 3]
# l2 = l1
# l2.append('a')
# print(l1, id(l1))
# print(l2, id(l2))

#copy
# l1 = [1, 2, 3]
# l2 = l1.copy()
# print(l1, id(l1))
# print(l2, id(l2))
# l2.append('a')
# print(l1, id(l1))
# print(l2, id(l2))

# l1 = [1,2,3,[4,5,6],3]
# l2 = l1.copy()
# print(l1, id(l1))
# print(l2, id(l2))
#
# l1.append('a')
# print(l1, id(l1))
# print(l2, id(l2))
#
# l1[3].append('a')
# print(l1[3], id(l1[3]))
# print(l2[3], id(l2[3]))
#
# print(id(l1[2]), id(l2[4]))

#deepcopy
# import copy
# li1 = [1,2,[4,5,6],3]
# li2 = copy.deepcopy(li1)
# print(id(li1), id(li2))
# li1[2].append('a')
# print(li1,li2)

# [:] qian copy
# li1 = [1,[1],2,3,4]
# li2 = li1[:]
# li1[1].append('a')
# print(li1, li2)
# print(li1 is li2)

li = ['name', 'age', 'sex']
for i in enumerate(li):
    print(i)

li = ['name', 'age', 'sex']
for index, i in enumerate(li, 1):
    print(index, i)










