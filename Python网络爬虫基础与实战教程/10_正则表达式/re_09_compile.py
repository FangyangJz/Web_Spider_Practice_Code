# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/15

import re

# 复用正则表达式方法

content = 'Hello 123 World_This is a Regex Demo Extra stings'
pattern = re.compile('Hello.*Demo',re.S)
result = re.match(pattern,content)
print(result)