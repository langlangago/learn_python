# str --> bytes encode
s = '儿歌'
# s = 'abcd'
b = s.encode('utf-8')
print(b)
# bytes --> str, decode
s1 = b.decode('utf-8')
print(s1)

# s = '儿歌'
# # s = 'abcd'
# b = s.encode('utf-8')
# print(b)
# # bytes --> str, decode
# s1 = b.decode('gbk')
# print(s1)