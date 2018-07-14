# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/21

from bs4 import BeautifulSoup
# 标签树的上行遍历
# .parent 节点的父亲标签
# .parents 节点先辈标签的迭代类型，用于循环遍历先辈节点

html = '''
<html><head><title>This is a python demo page</title></head>
<body>
<p class="title"><b>The demo python introduces several python courses.</b></p>
<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a href="http://www.icourse163.org/course/BIT-268001" class="py1" id="link1">Basic Python</a> and <a href="http://www.icourse163.org/course/BIT-1001870001" class="py2" id="link2">Advanced Python</a>.</p>
</body></html>
'''

soup = BeautifulSoup(html, 'html.parser')
print(soup.title.parent)
print(soup.html.parent)  # html 的父标签就是他自己
print(soup.parent)  #soup的父标签是空的
print('-'*50)

for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
