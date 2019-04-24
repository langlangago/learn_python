# write in 2019.3.9 Sat
# print(callable(print))
# print(callable(str))
# a = 1
# print(callable(a))
# print(dir(str))
# help(str)

# hash  不变值可哈希，str int tuple;可变值，不合哈希 dict list
# 地点的寻址方式 hash(key) --> value
# print(hash(123123))
# print(hash('abcdefg'))
# print(hash((1,'a')))
# print(hash([1,2,3]))

# print
# print('aaaaaa\n', end='')
# print('aaaaaa\n', end='')
# print(1, 2, 3, 4, sep='|')

# 打印进度条
# import time
# print('Loading', end='')
# for i in range(10):
#     print('.', end='', flush=True)
#     time.sleep(0.5)


# import time
# for i in range(0, 101, 2):
#     time.sleep(0.1)
#     char_sum = '*'
#     per_str = '\r%s%%: %s' % (i, i * char_sum)
#     print(per_str, end='', flush=True)

# eval,exec,compile，执行字符串代码
# eval 有返回值，计算类
# exec 没有返回值，流控控制类
# complie 编译，方便调用和执行

# eval('print(1234)')
# exec('print(1234)')
#
# print(eval('1+2+3+4'))
# print(exec('1+2+3+4'))

# code = '''for i in range(10):
#         print(i)
# '''
# exec(code)

# code = 'for i in range(10): print(i)'
# com1 = compile(code,'','exec')
# exec(com1)

# code1 = '1+2+3+4+5'
# com1 = compile(code1,'','eval')
# print(eval(com1))

# code1 = 'name = input("Please enter your name:")'
# com1 = compile(code1, '', 'single')
# exec(com1)
# print(name)

# print(bin(10)) #0b
# print(oct(10)) # 0o
# print(hex(10)) # 0x

# print(divmod(10,3))
# print(round(3.1415, 2))
# print(pow(3,2))

# print(sum([1,2,3],10))

print(set([1,2,2,1]))

