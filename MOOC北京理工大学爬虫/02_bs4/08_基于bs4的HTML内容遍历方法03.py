# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/21

from bs4 import BeautifulSoup
# 标签树的平行遍历
# 前提是都在同一个父节点下
# .next_sibling 返回按照HTML文本顺序的下一个平行节点标签
# .previous_sibling 返回按照HTML文本顺序的上一个平行节点标签
# 后面2个返回的是迭代类型，只能用在for in 里
# .next_siblings 迭代类型，返回按照HTML文本顺序的后续所有平行节点标签
# .previous_siblings 迭代类型，返回按照HTML文本顺序的前序所有平行节点标签

html = '''
<html><head><title>This is a python demo page</title></head>
<body>
<p class="title"><b>The demo python introduces several python courses.</b></p>
<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a href="http://www.icourse163.org/course/BIT-268001" class="py1" id="link1">Basic Python</a> and <a href="http://www.icourse163.org/course/BIT-1001870001" class="py2" id="link2">Advanced Python</a>.</p>
</body></html>
'''

soup = BeautifulSoup(html, 'html.parser')
print(soup.a.next_sibling) # .string的avigableNString类型也算一个兄弟标签
print(soup.a.next_sibling.next_sibling)
print('-'*50)
print(soup.a.previous_sibling)
print(soup.a.previous_sibling.previous_sibling)

for sibling in soup.a.next_siblings:
    # 遍历后续节点
    print(sibling)
print(type(sibling))
print(type(soup.a.next_sibling))
print(type(soup.a.next_siblings))

print('='*50)

for sibling in soup.a.previous_siblings:
    # 遍历前续节点
    print(sibling)
