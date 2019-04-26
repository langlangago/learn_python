import re
from urllib.request import urlopen


url = 'https://movie.douban.com/top250?start=0&filter='
response = urlopen(url)
html = response.read().decode('utf-8')

regex = '<li>.*?<div class="item">.*?<div class="pic">.*?<em class="">(?P<id>\d+)</em>.*?' \
      '<span class="title">(?P<title>.*?)</span>.*?<span class="rating_num" .*?>(?P<rating_num>.*?)</span>.*?' \
      '<span>(?P<comment_num>\d+)人评价</span>'

# ret = re.findall(regex, html, re.S)
# for i in ret:
#         print(i)

com = re.compile(regex, re.S)
ret = com.finditer(html)
for i in ret:
        print('id: %s, title: %s, rating_num: %s, comment_num:%s' % (i.group('id'), i.group('title'), i.group('rating_num'), i.group('comment_num')))

