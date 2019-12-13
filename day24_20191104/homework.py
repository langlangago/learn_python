#! encoding=utf-8
import pickle

class School:
    def __init__(self, name):
        self.name = name

class Banji:
    def __init__(self, name, cou_name, tea_name):
        self.name = name
        self.course_name = cou_name
        self.teacher_name = tea_name

class Student:
    def __init__(self, name, sch_name, cla_name):
        self.name = name
        self.school_name = sch_name
        self.class_name = cla_name

class Teacher:
    def __init__(self, name, sch_name):
        self.name = name
        self.school_name = sch_name

class Course:
    def __init__(self, name, sch_name, period, price):
        self.name = name
        self.school_name = sch_name
        self.period = period
        self.price = price

# beijing = School('beijing')
# shanghai = School('shanghai')
# linux = Course('linux', beijing, 12, 20000)
# python = Course('python', beijing, 18, 30000)
# go = Course('go', shanghai, 15, 25000)
# class_s1 =  Banji('s1')
# class_s2 = Banji('s2')
# alex = Student('alex', beijing, class_s1)
# tom = Student('tom', shanghai, class_s2)
# teacher_li = Teacher('lilei', beijing)
# teacher_han = Teacher('hanmeimei', shanghai)
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
        print('You can create teacher,create banji,create course,create student.')
        cmd = input('Please chose one command(eg: create teacher):').strip()
        if cmd == 'create teacher':
            teacher = input('Please input teacher name, school_name( , as sep ):').strip()
            info = create_teacher(teacher.split(',')[0], teacher.split(',')[1])
            save_file(info)
            read_file()
        elif cmd == 'create banji':
            banji = input('Plase input banji name:').strip()
            info = create_banji(banji)
            save_file(info)
            read_file()
        elif cmd == 'create course':
            course = input('Plase input course name,school name,priod,price(, as sep):').strip()
            info = create_course(course.split(',')[0], course.split(',')[1], course.split(',')[2], int(course.split(',')[3]))
            save_file(info)
            read_file()
        elif cmd == 'create student':
            student = input('Plase input student name, school name, class name(, as sep):').strip()
            info = create_student(student.split(',')[0], student.split(',')[1], student.split(',')[2])
            save_file(info)
            read_file()
        else:
            print('You command is invaild,exit.')
    elif username == 'alex' and passwd == '123456':
        pass
    elif username == 'lilei' and passwd == '123456':
        pass
    else:
        print('Your username or password is wrong, please check it.')
        return 1


login('admin', 'admin')
