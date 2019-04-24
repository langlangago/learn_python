# 实现员工信息表
# 文件存储格式如下：
# id，name，age，phone，job
# 1,Alex,22,13651054608,IT
# 2,Egon,23,13304320533,Teacher
# 3,nezha,25,1333235322,IT
# 现在需要对这个员工信息文件进行增删改查。
# 不允许一次性将文件中的行都读入内存。
# 基础必做：
# a.可以进行查询，支持三种语法：
# select 列名1，列名2，… where 列名条件
# 支持：大于小于等于，还要支持模糊查找。
# 示例：
# select name, age where age>22
# select * where job=IT
# select * where phone like 133
# 进阶选做：
# b.可创建新员工记录，id要顺序增加
# c.可删除指定员工记录，直接输入员工id即可
# d.修改员工信息
# 语法：set 列名=“新的值” where 条件
# #先用where查找对应人的信息，再使用set来修改列名对应的值为“新的值”
# 注意：要想操作员工信息表，必须先登录，登陆认证需要用装饰器完成
# 其他需求尽量用函数实现

# 用户输入条件
    # 条件解析，分开列名和条件
# 处理文件
    # 逐行读文件，逐行处理


user_col_dict = {'id': 0, 'name': 1, 'age': 2, 'phone': 3, 'job': 4}
ROW = 0

def parse_oneline(line_list, whe_list):
    index = 0
    for k in user_col_dict:
        if k == whe_list[0]:
            index = user_col_dict[k]
    if whe_list[1] == '<':
        return whe_list[2] > line_list[index]
    elif whe_list[1] == '>':
        return  whe_list[2] < line_list[index]
    elif whe_list[1] == '=':
        return whe_list[2] == line_list[index]
    elif whe_list[1] == 'like':
        return whe_list[2] in line_list[index]
    else:
        return None


def get_results(line_list, col_list, col_len):
    results = ''
    if col_list[0].strip() == '*':
        results = ','.join(line_list)
    else:
        for i in range(col_len):
            for k in user_col_dict:
                if k == col_list[i].strip():
                    index = user_col_dict[k]
                    results += line_list[index]
                    results += ','
    return results.strip(',')


def select_file(where1, column1, len_col1):
    with open('user.txt', mode='r', encoding='utf-8') as f:
        rets = ''
        for line in f:
            user_list = line.strip().split(',')
            res = parse_oneline(user_list, where1)
            if res:
                rets += get_results(user_list, column1, len_col1)
                rets += '\n'
    return rets


def get_rows():
    with open('user.txt', mode='r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            pass
        return i+1

def insert_file(line):
    row = get_rows()
    with open('user.txt', mode='a+', encoding='utf-8') as f:
        f.write('%d,%s\n' % (row+1, line))

def parse_input():
    # sql = input('Please input the sql :').strip('select')
    # sql = 'select name, age, job where age > 24'.strip('select')
    # sql = 'select name, age, job where age like 8'.strip('select')
    # sql = 'select * where age > 22'.strip('select')
    sql = 'insert Tom,24,18088886666,CEO'
    # sql = 'delete 1'
    # sql = 'set name='Tom' where name='Alex'

    first_word = sql.split()[0]
    if first_word == 'select':
        sql_list = sql.split('where')
        col_list = sql_list[0].split(',')
        whe_list = sql_list[1].split()
        col_len = len(col_list)
        return whe_list, col_list, col_len
    elif first_word == 'insert':
        return sql.split()[1]
    elif first_word == 'delete':
        pass
    elif first_word == 'set':
        pass
    else:
        print('Sql input error.')


#where, column, len_col = parse_input()
#sql_results = select_file(where, column, len_col)
#print(sql_results)

data = parse_input()
insert_file(data)








