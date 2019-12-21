class Manger:
    menu = [('创建讲师账号','create_teacher'),('创建学生账号','create_student'),
            ('创建课程','create_course'),('查看课程','show_course'),
            ('创建班级','create_class'),('查看班级','show_class'),
            ('绑定班级','bind_class'),('退出','quit')]
    def __init__(self, name):
        self.name = name

    def create_teacher(self):
        print('in create_teacher func.')

manager = Manger('alex')
menu_list = []
for i in list(enumerate(manager.menu, 1)):
    print(i[0],i[1][0])
    menu_list.append(i[1][1])

num = input('请输入编号：')
getattr(manager, menu_list[int(num)-1])()
