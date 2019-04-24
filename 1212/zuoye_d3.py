
#1. change list element
#li = [2, 3, 'k',['qwe', 20,['k1', ['tt', 3, '1']], 89], 'ab', 'adv']

#li[3][2][1][0] = li[3][2][1][0].upper()


#not allow words
li = ['fuck', 'diu', 'nimei']
new_li = []
content = input("please input the content:").strip()
for i in li:
    if i in content:
        l = len(i)
        content = content.replace(i, '*'*l)
print(content)