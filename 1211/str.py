#str

s = 'langXIAOwei'

s1= s.capitalize()
print(s1)

s2 = s.upper()
s3 = s.lower()
print(s2, s3)

'''
id_code = 'qweR'
user_input = input('Please input the verification code.')
if id_code.lower() == user_input.lower():
    print("passed.")
else:
    print('failed.')
'''

s4 = s.swapcase()
print(s4)

t = 'lang xiao wei'
print(t.title())

s5 = s.center(20, '*')
print(s5)

print(len(s))

print(s.startswith('lang'))
print(s.startswith('XIAO', 4))

print(s.find('X'))
print(s.find('U'))

print(s.index('X'))
# print(s.index('U'))

sb = '   Alex Lang  '
print(sb.strip())
print(sb.lstrip())
print(sb.rstrip())

# username = input('Please input name:').strip()
# if username == 'Alex':
#     print('Welcome Alex!')
# else:
#     print('Error Name.')
sc = 'Langaaa'
print(sc.count('an'))

# str ---> list
ss = 'Lang;Xiao;Wei'
print(ss.split(';'))

# format
sf = 'I am {}, my age is {}, my hobby is {}, again i am {}'.format('LangXiaowei', 31, 'running', 'Langxiaowei')
print(sf)
sf1 = 'I am {0}, my age is {1}, my hobby is {2}, again i am {0}'.format('LangXiaowei', 31, 'running')
print(sf1)
sf3 = 'I am {name}, my age is {age}, my hobby is {hobby}, again i am {name}'.format(name = 'LangXiaowei', age = 31, hobby = 'running')
print(sf3)

#replace
sr = 'I am Tom Li, he is Tom Zhang.'
print(sr.replace('Tom', 'Jack'))

#is
si1 = '123'
si2 = 'abc'
si3 = '123abc'
print(si1.isdigit())
print(si2.isalpha())
print(si3.isalnum())

# for

s_for = 'abcdefghijklmn'
for i in s_for:
    print(i)


# in
s_in = 'Like Tom and Jack'
if 'Tom' in s_in:
    print('Your have the forbidden words.')


# cut
ss = 'ABCDEFGHIJKLMN'
print(ss[0])
print(ss[0:4])
print(ss[:])
print(ss[::2])
print(ss[1::2])
print(ss[0:])
print(ss[-1])
print(ss[::-1])
print(ss[5::-1])





