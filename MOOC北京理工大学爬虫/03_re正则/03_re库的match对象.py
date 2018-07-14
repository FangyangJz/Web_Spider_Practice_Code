# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/24

# match对象的属性
# .string 待匹配的文本
# .re 匹配时使用的pattern对象（正则表达式）
# .pos    正则表达式搜索文本的开始位置
# .endpos 正则表达式搜索文本的结束位置
# # match对象的方法
# .group(0)   获得匹配后的字符串
# .start()    匹配字符串在原始字符串的开始位置
# .end()      匹配字符串在原始字符串的结束位置
# .span()     返回（.start(),.end()）

import re

m = re.search(r'[1-9]\d{5}','bit 100084 tsu 100081')
print(m.string)
print(m.re)
print(m.pos)
print(m.endpos)
print(m.group(0))
print(m.start())
print(m.end())
print(m.span())