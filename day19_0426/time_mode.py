import time
# print(time.time()) # 时间戳时间 ，给电脑看的
# print(time.strftime('%Y-%m-%d %H:%M:%S')) # 字符串格式化时间，给人看的
# print(time.localtime()) # 结构化时间，方便取值和计算

#时间戳和结构化时间的转换
t = time.time()
print(t)
print(time.localtime())
print(time.gmtime())
print(time.localtime(t))
print(time.localtime(1500000000))
print(time.mktime(time.localtime())) # struc_time --> timestamp

# 结构化时间转成字符串格式化时间
print(time.strptime('2019-11-11', '%Y-%m-%d'))
print(time.strftime('%Y-%m-%d', time.localtime(1500000000)))

# 字符串时间和时间戳时间不能直接转换，要经过接过话时间struc_time转换一次

#结构换时间、时间戳时间转成%a %b %c %H:%M:%S 串, asctime, ctime
print(time.asctime(time.localtime()))  # 结构化时间转换用asctime
print(time.ctime(time.time()))         # 时间戳时间转换用ctime

# 总结
# strtime --(strptime)--> struct_time --(mktime)--> timestamp
# strtime <--(strftime)-- struct_time <--(localtime)-- timestamp
# struct_time --(asctime)--> chuan_time
# timestamp --(ctime)--> chuan_time