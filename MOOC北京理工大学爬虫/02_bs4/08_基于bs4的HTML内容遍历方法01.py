# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/21

from bs4 import BeautifulSoup
# 标签树的下行遍历
# .contents 子节点的列表，将<tag>所有儿子节点存入列表，返回的一个迭代类型，在for里用
# .children 子节点的迭代类型，与.contents类似，用于循环遍历儿子节点 ,返回的是一个列表
# .descendants 子孙节点的迭代类型，包含所有子孙节点，用于循环遍历，返回的一个迭代类型，在for里用
html = '''
<html><head><title>This is a python demo page</title></head>
<body>
<p class="title"><b>The demo python introduces several python courses.</b></p>
<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a href="http://www.icourse163.org/course/BIT-268001" class="py1" id="link1">Basic Python</a> and <a href="http://www.icourse163.org/course/BIT-1001870001" class="py2" id="link2">Advanced Python</a>.</p>
</body></html>
'''

soup = BeautifulSoup(html, 'html.parser')
print(soup.head.contents)
print(soup.body.contents)   # 返回的是一个列表
print('-'*50)

for child in soup.body.children:
# 遍历儿子节点
    print(child)

print('='*50)

for child in soup.body.descendants:
# 遍历子孙节点
    print(child)