# dict
#数据类型分类：可变数据类型，不可变数据类型
#不可变数据类型：int, str, bool, tuple  可哈希
#可变数据类型: list, dict, set          不可哈希
#dict key 必须是不可变数据类型 , value 任意数据类型
#dict 优点：二分查找快，存储大量的关系数据

dic = {'name':'Alex', 'age':18, 'sex':'male'}

#insert
# dic['weight'] = '80KG'
# dic.setdefault('hight','160CM')
# print(dic)

#delte
# dic.pop('age')
# dic.popitem()
# del dic['age']
# del dic
# dic.clear()
# print(dic)

#update
# dic['age'] = 19
# dic2 = {'name':'Lili', 'age':19, 'sex':'male', 'weight':'80KG'}
# dic2.update(dic)
# print(dic2)

#select
# print(dic.keys())
# print(dic.values())
# print(dic.items())
#
# for i in dic:
#     print(i)
#
# for k in dic.keys():
#     print(k)

#  for k in dic.values():
#     print(k)

# for k,v in dic.items():
#     print(k,v)

#get
print(dic['name'])
print(dic.get('name1', 'TOTO'))
