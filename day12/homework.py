# write a wrapper yourself
#def wrapper(f):
#    def inner(*args, **kwargs):
#        print('Do something before.')
#        ret = f(*args, **kwargs )
#        print('Do someting after.')
#        return ret
#    return inner
#
#@wrapper  #holiday = wrapper(holiday)
#def holiday(day):
#    print('放假了%s天'%day)
#    return '好开心'
#
#ret = holiday(10)
#print(ret)

# global
# x = 10
#
# def add1():
#     global x
#     x += 1
#     print(x)
#
# add1()
# print(x)

# nonlocal

# x = 20
#
# def add1():
#     x = 10
#     def inner():
#         nonlocal x
#         x += 1
#         print(x)
#     return inner
#
# ret = add1()
# ret()

# 1.编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），
# 要求登录成功一次，后续的函数都无需再输入用户名和密码

# flag = False
#
#
# def login(func):
#     def inner(*args, **kwargs):
#         global flag
#         if not flag:
#             username = input('Enter username:').strip()
#             passwd = input('Enter password:').strip()
#
#             with open('password.txt', mode='r', encoding='utf-8') as f:
#                 for line in f.readlines():
#                     auth_list = line.strip().split(':')
#                     if username == auth_list[0] and passwd == auth_list[1]:
#                         print('Login sucess.')
#                         flag = True
#                     else:
#                         print('Login Failed.')
#                         flag = False
#         ret = func(*args, **kwargs)
#         return ret
#     return inner
#
#
# @login
# def reply(s):
#     print('Now you can reply the topic. Add:', s)
#
#
# @login
# def write_topic(s):
#     print('You are writing a topic, the titile is :', s)
#
#
# reply('Hahaha, Are you kidding me?')
# write_topic('The first class')


# 2.编写装饰器，为多个函数加上记录调用功能，要求每次调用函数都将被调用的函数名称写入文件
# def record(func):
#     def inner(*args, **kwargs):
#         ret = func(*args, **kwargs)
#         print(func.__name__)
#         with open('call_funcs.txt', mode='a', encoding='utf-8') as f:
#             f.write(func.__name__+'\n')
#         return ret
#     return inner
#
#
# @record
# def add(a, b):
#     print(a+b)
#
#
# @record
# def minus(a, b):
#     print(a-b)
#
#
# add(5, 3)
# minus(10, 8)

# 进阶作业(选做)：
# 1.编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果
# 2.为题目1编写装饰器，实现缓存网页内容的功能：
# 具体：实现下载的页面存放于文件中，如果文件内有值（文件大小不为0），就优先从文件中读取网页内容，否则，就去下载，然后存到文件中

from urllib import request


def cache(func):
    def inner(*args, **kwargs):
        ret = func(*args, **kwargs)
        print(ret)
        with open('download.html', mode='w+', encoding='utf-8') as f:
            f.write(ret)
        return ret
    return inner

@cache # get = cache(get)
def get(url):
    response = request.urlopen(url)
    page = response.read()
    page = page.decode('utf-8')
    return page


get('http://www.baidu.com')






















