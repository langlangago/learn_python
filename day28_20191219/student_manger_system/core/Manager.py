from core.my_pickle import  MyPickle
from conf.config import *
from core.teacher import Teacher

class Manager:
    menu = [('创建讲师账号','create_teacher'),('创建学生账号','create_student'),
            ('查看学校','show_school'),('查看讲师','show_teacher'),('查看课程','show_course'),
            ('创建班级','create_class'),('查看班级','show_class'),
            ('为班级指定老师','bind_class_teacher'),('退出','exit')]
    def __init__(self, name):
        # 管理员可能操作教师，班级，课程，学校的文件，就先实例化。
        # 拿到的是类似文件描述符, pickle_obj
        self.name = name
        self.teacher_obj_pickle = MyPickle(teacher_obj)
        self.course_obj_pickle = MyPickle(course_obj)
        self.school_obj_pickle = MyPickle(schoolinfo)
        self.class_obj_pickle = MyPickle(classes_obj)

    @staticmethod
    def userinfo_handle(content):
        with open(userinfo, 'a') as f:
            f.write('\n%s' % content)

    # 要进行反射,根据传入的pickle_obj操作读取相应文件
    def show(self, pickle_obj):
        pickle_obj = getattr(self, pickle_obj)
        load_g = pickle_obj.loaditer()
        for obj_line in load_g:
            for i in obj_line.__dict__.keys():
                print(i,obj_line.__dict__[i])

    def show_teacher(self):
        self.show('teacher_obj_pickle')

    def show_course(self):
        self.show('course_obj_pickle')

    def show_school(self):
        self.show('school_obj_pickle')

    def show_class(self):
        self.show('class_obj_pickle')

    def create_teacher(self):
        # 输入讲师姓名，密码，存入userinfo文件
        # 输入讲师所在的学校，实例化一个讲师对象，存入讲师对应的文件中
        print('in create_teacher func.')
        teacher_name = input('请输入要创建讲师的姓名：')
        teacher_pwd = input('请输入要创建讲师的密码：')
        school = input('学校：')
        content = '%s|%s|Teacher' % (teacher_name, teacher_pwd)
        Manager.userinfo_handle(content)
        teacher = Teacher(teacher_name, school)
        self.teacher_obj_pickle.dump(teacher)
        print('创建讲师成功。')

    def create_class(self):
        pass