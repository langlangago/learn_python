#带参数的装饰器, 三层装饰器,达到开关的效果
# import time
#
# FLAG = False
#
# def timmer_out(FLAG):
#     def timmer(func):
#         def inner(*args, **kwargs):
#             if FLAG:
#                 start = time.time()
#                 ret = func(*args, **kwargs)
#                 end = time.time()
#                 print(end-start)
#                 return ret
#             else:
#                 ret = func(*args, **kwargs)
#                 return ret
#         return inner
#     return timmer
#
#
# @timmer_out(FLAG) # timmer_out(FLAG) 函数调用 + @timmer 装饰器， @timmer == wahaha = timmer(wahaha)
# def wahaha():
#     time.sleep(0.1)
#     print('wahahahaha.')
#
# @timmer_out(FLAG)
# def erguotou():
#     time.sleep(0.2)
#     print('erguotoutoutou.')
#
#
# wahaha()
# erguotou()


# 多个装饰器，装饰一个函数


# def wrapper1(func): # func => f
#     def inner1(*args, **kwargs):
#         print('Wrapper1, Do something before. ')
#         ret = func(*args, **kwargs)
#         print('Wrapper1, Do something after.')
#         return ret
#     return inner1
#
#
# def wrapper2(func): # func => inner1
#     def inner2(*args, **kwargs):
#         print('Wrapper2, Do something before.')
#         ret = func(*args, **kwargs)
#         print('Wrapper2, Do something after.')
#         return ret
#     return inner2
#
#
# @wrapper2  # f = wrapper2(f) => inner1 = wrapper2(inner1) => inner2
# @wrapper1  # f = wrapper1(f) = inner1
# def f():
#     print('in f.')
#     return 'Done'
#
#
# ret = f()  # f() == inner2()
# print(ret)

# 普通装饰器
def wrapper(func):
    def inner(*args, **kwargs):
        """Deractor"""
        print('This is deractor function.')
        ret = func(*args, ** kwargs)
        return ret
    return inner


@wrapper    # test = wrapper(test) = inner
def test():
    """Test"""
    print('This is test function.')


print('test function, name: %s, describe: %s' % (test.__name__, test.__doc__))  # test = inner


# 完美的装饰器
from functools import wraps


def wrapper(func):
    @wraps(func)
    def inner(*args, **kwargs):
        """Deractor"""
        print('This is deractor function.')
        ret = func(*args, ** kwargs)
        return ret
    return inner


@wrapper    # test = wrapper(test) = inner
def test():
    """Test"""
    print('This is test function.')


print('test function, name: %s, describe: %s' % (test.__name__, test.__doc__))  # test = inner
















