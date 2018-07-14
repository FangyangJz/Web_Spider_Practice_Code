# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/13

# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功，match就返回none
# re.match(pattern, string, flags=0)

import re

# 常规匹配 ，笨方法
content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$',content)
print(result)
print(result.group())  #返回匹配结果
print(result.span())
print(len(content))
print('-'*50)

# 泛匹配
result = re.match('^Hello.*Demo$',content) #^开头 ， $结尾， .*任意字符
print(result)
print(result.group())  #返回匹配结果
print(result.span())
print('='*50)

# 目标匹配
# result = re.match('^Hello\s(\d+)\sWorld.*Demo$',content)
# print(result)
# print(result.group(1))  #返回匹配结果
# print(result.span())
