# caculate 5+9 or 5+ 9 or 5 + 9
# content = input("Please input content:").strip()

# clist = content.split('+')
# print(int(clist[0]) + int(clist[1]))

# num = 0
# for i in clist:
#     num = num + int(i)
# print(num)

# index = content.find('+')
# a = int(content[0:index])
# b = int(content[index+1:])
# print(a+b)


# how many nums in any string ,eg:"aaabbb123123aaa"
s = input('Please input nums and alpha:')

count = 0
for i in s:
    if i.isdigit():
        count += 1

print(count)