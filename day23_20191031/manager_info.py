#! encoding=utf-8
import pickle

class School:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, name, school_name, period, price):
        self.name = name
        self.school_name = school_name
        self.period = period
        self.price = price

class Te qacher:
    def __init__(self, name, school_name):
        self.name = name
        self.school_name = sch_name

class Banji:
    def __init__(self, name, course_name, teacher_name):
        self.name = name
        self.course_name = course_name
        self.teacher_name = teacher_name

class Student:
    def __init__(self, name, school_name, class_name):
        self.name = name
        self.school_name = school_name
        self.class_name = class_name
l = []
d = {}

def create_teacher(tea_name, sch_name):
    t = Teacher(tea_name, sch_name)
    d['name'] = t.name
    d['school_name'] = t.school_name
    l.append('teacher')
    l.append(d)
    return l

def create_banji(cla_name, cou_name, tea_name):
    b = Banji(cla_name, cou_name, tea_name)
    d['name'] = b.name
    l.append('banji')
    l.append(d)
    return l

def create_course(cou_name, school_name, period, price):
    c = Course(cou_name, school_name, period, price)
    d['name'] = c.name
    d['school_name'] = c.school_name
    d['period'] = c.period
    d['price'] = c.price
    l.append('course')
    l.append(d)
    return l

def create_student(stu_name, sch_name, ban_name):
    s = Student(stu_name, sch_name, ban_name)
    d['name'] = s.name
    d['school_name'] = s.school_name
    d['class_name'] = s.class_name
    l.append('student')
    l.append(d)
    return l

def save_file(data):
    with open('info.txt', 'ab') as f:
        pickle.dump(data, f)

def read_file():
    with open('info.txt', 'rb') as f:
        try:
            while True:
                print(pickle.load(f))
        except EOFError:
            print('........Already Read all data.')

def login(username, passwd):
    if username == 'admin' and passwd == 'admin':
        print('Welcome to students manager system.')
        s_str = input('Please create school first(eg:school_name):').strip()
        s = School(s_str)
        d['name'] = s_str
        l.append('school')
        l.append(d)


        c_str = input('Please create course second(eg:course_name,period,price)').strip()
        c_list = c_str.split(',')
        c = Course(c_listp[0], s.name, c_alist[1], c_list[2])

        t_str = input('Please create teacher third(eg:teacher_name)').strip()
        t = Teacher(t_str, s.name)

        b_str = input('Plase create class forth(eg:class_name)').strip()
        b = Banji(b_str, c.name, t.name)

        stu_str = input('Please create student finnaly(eg:student_name)').strip('')
        stu = Student(stu_str, s.name, b.name)



#         if cmd == 'create teacher':
#             teacher = input('Please input teacher name, school_name( , as sep ):').strip()
#             info = create_teacher(teacher.split(',')[0], teacher.split(',')[1])
#             save_file(info)
#             read_file()
#         elif cmd == 'create banji':
#             banji = input('Plase input banji name:').strip()
#             info = create_banji(banji)
#             save_file(info)
#             read_file()
#         elif cmd == 'create course':
#             course = input('Plase input course name,school name,priod,price(, as sep):').strip()
#             info = create_course(course.split(',')[0], course.split(',')[1], course.split(',')[2], int(course.split(',')[3]))
#             save_file(info)
#             read_file()
#         elif cmd == 'create student':
#             student = input('Plase input student name, school name, class name(, as sep):').strip()
#             info = create_student(student.split(',')[0], student.split(',')[1], student.split(',')[2])
#             save_file(info)
#             read_file()
#         else:
#             print('You command is invaild,exit.')
    elif username == 'alex' and passwd == '123456':
        pass
    elif username == 'lilei' and passwd == '123456':
        pass
    else:
        print('Your username or password is wrong, please check it.')
        return 1


login('admin', 'admin')
