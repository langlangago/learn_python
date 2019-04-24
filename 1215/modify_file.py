# mofify a file content

with open('name.txt', mode='r+', encoding='utf-8') as f, \
        open('name2.txt', mode='w', encoding='utf-8') as f2:
    for line in f:
        if 'Jack' in line:
            line = line.replace('Jack', 'Lisa')
        f2.write(line)

import os
os.remove('name.txt')
os.rename('name2.txt', 'name.txt')

