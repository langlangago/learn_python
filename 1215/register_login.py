#homework, three times login from file.
print("Welcome, Please Regist First.")
username = input("Please enter username:")
password = input('Please enter password:')
with open('password.txt', mode='w', encoding='utf-8') as f:
    # f.write(username)
    # f.write(';')
    # f.write(password)
    f.write('{};{}'.format(username, password))
print("Regist Sucessfully!")

print("Welcome, You can login now.")
with open('password.txt', mode='r+', encoding='utf-8') as f:
    li = f.readline().split(';')

count = 0
flag = True
while flag :
    user1 = input("Please input your username:")
    passwd1 = input('Please input your password:')
    if li[0] == user1 and li[1] == passwd1:
        print('Login Sucess!')
        flag = False
    else:
        print('Wrong username or password .')
        count +=1
        if count < 3:
            flag = True
        else:
            flag = False
            print('You have failed three time, forbidden to login now.')


#langxiaowei,123456