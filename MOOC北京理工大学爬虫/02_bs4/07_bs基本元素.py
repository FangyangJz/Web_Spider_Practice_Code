# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/21


from bs4 import BeautifulSoup
# import requests

# url = 'https://python123.io/ws/demo.html'
# r = requests.get(url)

html = '''
<html><head><title>This is a python demo page</title></head>
<body>
<p class="title"><b>The demo python introduces several python courses.</b></p>
<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a href="http://www.icourse163.org/course/BIT-268001" class="py1" id="link1">Basic Python</a> and <a href="http://www.icourse163.org/course/BIT-1001870001" class="py2" id="link2">Advanced Python</a>.</p>
</body></html>
'''

soup = BeautifulSoup(html, 'html.parser')

print(soup.title)
print(soup.a)
print(soup.a.name)
print(soup.a.parent)
print(soup.a.parent.name)
print(soup.a.parent.parent.name)
print(soup.a.attrs)  # 返回的是字典
print('-'*50)

print(soup.p.string)
print(type(soup.p.string))
print('='*50)

newsoup = BeautifulSoup('<b><!--This is a comment--></b><p>This is not a comment</p>',
                        'html.parser')

print(newsoup.b.string)
print(type(newsoup.b.string))
print(newsoup.p.string)
print(type(newsoup.p.string))