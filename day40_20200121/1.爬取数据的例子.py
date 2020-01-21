#! encoding:utf-8
import requests
from multiprocessing import Pool

def get(url):
    response = requests.get(url)
    if response.status_code == 200:
        return url, response.content.decode('utf-8')

def call_back(args):
    url, content = args
    print(url, len(content))

if __name__ == '__main__':
    url_list = [
        'https://www.baidu.com',
        'https://www.langxw.com',
        'http://www.efushui.com',
        'https://www.taobao.com'
    ]
    p = Pool(5)
    for url in url_list:
        p.apply_async(get, args=(url, ), callback=call_back)
    p.close()
    p.join()