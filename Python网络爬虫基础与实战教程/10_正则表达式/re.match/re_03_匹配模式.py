# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/13


import re

content = '''Hello 1234567 World_This
is a Regex Demo
'''

# . 可以匹配除了换行符意外的任意字符，下面加了参数re.S后，.*可以匹配任意字符
result = re.match('^He.*?(\d+).*?Demo$',content,re.S)
print(result)
print(result.group(1))