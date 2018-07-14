# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/24


import re

pattern = r'PY.*N'
text = 'PYANBNCNDN'
match = re.search(pattern,text)
print(match.group(0))

# 贪婪匹配
# re库默认采用贪婪匹配，即输出匹配最长的子串
# 所以上面的结果

# 最小匹配 看下面加?
# *?    前一个字符0次或无限次扩展，最小匹配
# +?      前一个字符1次或无限次扩展，最小匹配
# ??      前一个字符0次或1次扩展，最小匹配
# {m,n}?    扩展前一个字符m至n次（含n），最小匹配

pattern = r'PY.*?N'
text = 'PYANBNCNDN'
match = re.search(pattern,text)
print(match.group(0))
