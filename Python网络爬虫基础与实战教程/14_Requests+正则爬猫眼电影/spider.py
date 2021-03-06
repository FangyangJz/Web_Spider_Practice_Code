# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/18
import json
from multiprocessing import Pool
import requests
from requests.exceptions import RequestException
import re

def get_one_page(url,headers):

    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None

    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern,html)

    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'actor':item[3].strip()[3:],# 去掉 主演:
            'time':item[4].strip()[5:],
            'score':item[5]+item[6]
        }

def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:         # 别忘了加 encoding='utf-8'
        f.write(json.dumps(content, ensure_ascii=False)+'\n')  # ensure_ascii=False 保证写入的中文不是编码
        f.close()


def main(offset):

    url = 'http://maoyan.com/board/4?offset='+str(offset)
    headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}
    html = get_one_page(url,headers)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':

    # 普通办法
    # for i in range(10):
    #     main(i*10)

    # 多进程秒抓办法
    pool = Pool()
    pool.map(main, [i*10 for i in range(10)])
