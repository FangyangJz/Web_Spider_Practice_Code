# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/21

# 方法一:完整解析信息的标记形式，再提取关键信息
# 优点:信息解析准确
# 缺点:提取过程繁琐，速度慢
#
# 方法二:无视标记形式，直接搜索关键信息
# 优点:提取过程简介，速度块
# 缺点:提取结果准确性与信息内容相关
#
# 方法三:结合上面2中

from bs4 import BeautifulSoup

html = '''
<html><head><title>This is a python demo page</title></head>
<body>
<p class="title"><b>The demo python introduces several python courses.</b></p>
<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a href="http://www.icourse163.org/course/BIT-268001" class="py1" id="link1">Basic Python</a> and <a href="http://www.icourse163.org/course/BIT-1001870001" class="py2" id="link2">Advanced Python</a>.</p>
</body></html>
'''

soup = BeautifulSoup(html, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))