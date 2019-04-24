#tuple
# can select , for; son can not be changed ,grandson can be changed.

# tu = (1, 3, 5, ['Alex', 'Tom', 'Jack'], 'Sasa')
# print(tu[1])
# print(tu[3])
# for i in tu:
#     print(i)
#
# tu[3][0] = 'Haha'
# print(tu)


# s = 'Alex'
# print('-'.join(s))

# convert list to string,use join
# li = ['I', 'am', 'a', 'boy']
# print(' '.join(li))

# convert string to list,  user splite
# s = 'I am  a boy'
# print(s.split())

# range
# for i in range(10):
#     print(i)
#
# for i in range(0,10,2):
#     print(i)

# for i in range(10,0,-2):
#     print(i)

# error ,return None
# for i in range(0, 10, -1):
#     print(i)



li = [1, 2, 3, 4, 5, ['Tom', 'Lili', 'Jack'], 6, 7, 8, 'Sasa']
l = len(li)
for i in range(0,l):
    if type(li[i]) == list:
        for  j in li[i]:
            print(j)
    else:
        print(li[i])












