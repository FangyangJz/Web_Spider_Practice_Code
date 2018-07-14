# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/13


import re

# 贪婪模式
content = 'Helo 12344596 World_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo$', content)   # 前面的.*匹配掉了1234459
print(result)
print(result.group(1))  # group(1)指里面的(), group()返回整个字符串

# 非贪婪模式
content = 'Helo 12344596 World_This 4568 is a Regex Demo'
result = re.match('^He.*?(\d+).*?(\d+).*Demo$', content)   # 多了一个.*? 表示尽可能少的匹配,当匹配到数字时，就停止.*匹配
print(result)
print(result.group(1))
print(result.group(2))
