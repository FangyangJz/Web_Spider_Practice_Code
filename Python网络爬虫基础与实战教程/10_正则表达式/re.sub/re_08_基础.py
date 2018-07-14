# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/15


import re

content = 'Extra stings Hello 123 World_This is a Regex Demo Extra stings'
content = re.sub('\d', '1', content)
print(content)

content = re.sub('\d', 'replacement', content)
print(content)

content = 'Extra stings Hello 123 World_This is a Regex Demo Extra stings'
content = re.sub('(\d+)',r'\1 8910',content) # \1 表示把前面group(1)的内容拿过来
print(content)