# write at 2019.3.14 16:00

# import sys
# sys.setrecursionlimit(30000)
# n = 0
# def story():
#     print('Long long ago, ther is a mountain.')
#     global n
#     n += 1
#     print(n)
#     story()
#
# story()

# RecursionError: maximum recursion depth exceeded while calling a Python object
# 递归的最大深度默认是997,是Python从内存角度出发，做的限制


# 求年龄,前一个比上一个大2岁，最后一个人40岁
def age(n):
    if n == 4:
        return 40
    elif 0 < n < 4:
        return age(n+1) + 2

print(age(2))
