#nesting functions
# def max(a, b):
#     return a if a > b else b
#
# def my_max(a, b, c):
#     x = max(a, b)
#     y = max(x, c)
#     return  y
#
# print(my_max(7, 5, 6))

# a = 1
#
# def outer():
#     a = 1
#     def inner():
#         a = 2
#         print(a)
#         print('inner')
#         def inner2():
#             # print(a ,b)
#             # global a
#             nonlocal a
#             a += 1
#             print('inner2')
#         inner2()
#         print('inner a :{}'.format(a))
#     inner()
#     print('outer a :{}'.format(a))
#
# outer()
# print('global a: {}'.format(a))



def func():
    print('aaa')

f2 = func
print(func, f2)

l = [func, f2]
for i in l:
    i()

def wahaha(f):
    f()
    return f

res = wahaha(func)
print(res)


























