# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/21

# <>.find_all(name, attrs, recursive, string, **kwargs)
# name 对标签名称的检索字符串
# attrs 对标签属性值的检索字符串，可标注属性检索
# recursive 是否对子孙全部检索，默认True
# string  <>...</>中字符串区域的检索字符串

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
print(soup.find_all(string = 'Basic Python')) # 必须输入全才能检索到

# 想不输入全，用re方法
a = soup.find_all(string=re.compile('python'))
print(a)
