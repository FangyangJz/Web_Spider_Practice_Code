# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/15


import re
import requests

content = requests.get('https://book.douban.com/').text
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
results = re.findall(pattern, content)

if results:
    for result in results:
        url, name, author, date = result
        author = re.sub('\s','',author)
        date = re.sub('\s','',date)
        print(url,name,author,date)
