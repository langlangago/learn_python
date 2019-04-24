#work 1  delete jishu
# li = [00, 11, 22, 33, 44, 55, 66, 77]
#
# for i in range(0,len(li)//2):
#     li.pop(i+1)
#
# print(li)
#
# dict

#work 2 delete key which has 'k'
dic ={'k1':'v1', 'k2':'v2', 'a3':'v3', 'a4':'v4'}

#wrong  ,ictionary changed size during iteration
# for i in dic:
#     if 'k' in i:
#         del dic[i]
# print(dic)

#methods 1
# li =[]
# for i in dic:
#     if 'k' in i:
#         li.append(i)
# for i in li:
#     del dic[i]
# print(dic)

#methods 2
# dic2 = {}
# for i in dic:
#     if 'k' not in  i:
#         dic2[i] = dic[i]
# dic = dic2
# print(dic)

#tuple
# tu1 = ('abc')
# tu2 = ('adb',)
# print(tu1, type(tu1))
# print(tu2, type(tu2))

# str, int,list,dict,set ---> bool ,which is True
#0,'',[],{},() --- > bool , False
# other -- > bool ,True