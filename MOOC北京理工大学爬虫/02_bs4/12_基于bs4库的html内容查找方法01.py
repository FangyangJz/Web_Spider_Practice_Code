# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/21

# <>.find_all(name, attrs, recursive, string, **kwargs)
# name 对标签名称的检索字符串


from bs4 import BeautifulSoup
import re

html = '''
<html><head><title>This is a python demo page</title></head>
<body>
<p class="title"><b>The demo python introduces several python courses.</b></p>
<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a href="http://www.icourse163.org/course/BIT-268001" class="py1" id="link1">Basic Python</a> and <a href="http://www.icourse163.org/course/BIT-1001870001" class="py2" id="link2">Advanced Python</a>.</p>
</body></html>
'''

soup = BeautifulSoup(html, 'html.parser')
print(soup.find_all('a'))
print('-'*100)
print(soup.find_all(['a','b']))
print('='*100)

for tag in soup.find_all(True): #name为True，查找了所有标签
    print(tag.name)

print('='*100)

for tag in soup.find_all(re.compile('b')):
    print(tag.name)