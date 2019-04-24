# li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# dic = {}
# li1 = []
# li2 = []
# for i in li:
#     if i > 66:
#         li1.append(i)
#     elif i < 66:
#         li2.append(i)
# print(li1, li2)
# dic['k1'] = li1
# dic['k2'] = li2
# print(dic)

#shopping bus
# li = ['mobilephone', 'computer', 'mouse', 'display']
#
#
# flag = True
# while flag:
#     for i in li:
#         print(li.index(i) + 1, i)
#     s = input('Please input the shangpin num(enter q to quit):').strip()
#     if s.upper() == 'Q':
#         flag = False
#     if s.isdigit():
#         if 0 < int(s) < len(li) + 1 :
#             print(li[int(s)-1])
#         else:
#             print('You input  the wrong number.')
#             continue
#     else:
#         print('Please enter the number only.')
#         continue
#



# = , == , is, id()
# li1 = [1, 2, 3]
# li2 = li1
# print(li2 is li1)
# print(id(li1), id(li2))

#python3 default character code utf8
# str: s = 'alxe', 01010101 unicode
# bytes: s = b'alex'  01010110  utf8 gbk ascii
#
# unicode can not strore and transation
# bytes can store and transation


# s1 = 'alex'
# s2 = b'alex'
# print(s1, type(s1))
# print(s2, type(s2))

# encode str -- > bytes
# s1 = 'alex'
# s11 = s1.encode('utf-8')
# print(s11,type(s11))
#
# s2 = '中国'
# s22 = s2.encode('utf-8')
# s23 = s2.encode('gbk')
# print(s2, type(s2))
# print(s22, type(s22))
# print(s23, type(s23))

# 目的：（1）启动程序后，让用户输入工资，然后打印商品列表
# （2）允许用户根据商品编号购买商品
# （3）用户选择商品后，检测余额是否够，够直接扣款，不够就提醒
# （4）可随时退出，退出时打印已购买商品和余额

goods = [('macbook', 10000),
         ('iphone', 8000),
         ('ipad', 4000),
         ('iwatch', 2000),
         ('ipod', 1000),
         ('mouse', 500),
         ('keyboard', 700),
         ('pen', 300)
         ]
flag = True
shopping_backet = []
sallary = int(input("Please input your sallary:").strip())
balance = sallary

for i in goods:
    print('{}\t{}\t\t{}'.format(goods.index(i)+1, i[0],i[1]))

while flag:
    num = input('Please chose which good to buy(enter q to quit):').strip()
    if num.isdigit():
        index = int(num)
        if 0 < index < len(goods) + 1:
            if ( balance >= goods[index-1][1] ):
                print("You have  buy the \033[1;m {} \033[0m ,coast \033[1;m {} \033[0myuan.".format(goods[index-1][0], goods[index-1][1]))
                shopping_backet.append(goods[index-1][0])
                balance  -= goods[index-1][1]
                print('Your balance now is \033[1;m {} \033[0m'.format(balance))
            else:
                print('You have no enough momeny.')
                flag = False
        else:
            print('You have  entered the wrong num.')
            continue
    elif num.upper() ==  'Q':
        print('Bye Bye.')
        flag = False
    else:
        print('Please enter the goods number.')


print('Finnaly, You  have by \033[1;m {} \033[0m ,coast \033[1;m {} \033[0m yuan'.format(shopping_backet, sallary - balance))



enumerate()














