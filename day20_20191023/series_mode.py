# 序列化模块，方便将数据结构转化成字符换，之后就方便存储和传输
# 比如：字典类型数据结构，存文件存的是字符串，网络传输：先转换成字符串，再转成bytes类型传输。

# json  通用
# pickle 可以转化所有类型的数据结构，但是只能自己解开
# shelve 句柄可以直接操作

# json
# dumps 序列化, loads 反序列号，直接操作内存数据
# dump, load, 是操作文件里的数据,序列化后写入，or 读出后反序列化
# 只能序列化 数字、字符串、列表、字典、元组、不能集合。

# import json
# d = {'k1':'v1', 'k2':'v2'}
# str_d = json.dumps(d)
# print(type(str_d), str_d)
# dict_d = json.loads(str_d)
# print(type(dict_d), dict_d)
#
# f = open('json_dump.txt', 'w')
# json.dump(d, f)  # 序列化，之后写
# f.close()

# f = open('json_dump.txt')
# dict_d2 = json.load(f)  # 反序列化，之后读
# f.close()
# print(type(dict_d2), dict_d2)


# pickle 方法同上，序列化后是bytes数据类型，支持分批次load

# shelve 类似open，打开文件拿到文件句柄，然后利用字典形式写数据。


