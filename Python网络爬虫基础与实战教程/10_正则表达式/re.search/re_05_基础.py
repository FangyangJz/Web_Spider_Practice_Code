# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/15

# 能用search方法就不用match方法，因为match方法限定头部必须匹配

import re

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.match('Hello.*?(\d+).*?Demo',content)
print(result)

result = re.search('Hello.*?(\d+).*?Demo',content)
print(result)
print(result.group(1))