# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/24

import re

# 正则表达式的表示类型
# raw string类型，原生字符串类型，不含转义字符
# 与string不同
# 老师建议： 当正则表达式包含转义符时，使用raw string

# re库主要功能函数
# re.search() 在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
# re.search(pattern,string,flags=0)
# 常用标记：
# re.I re.IGNORECASE  忽略正则表达式的大小写，[A-Z]能匹配小写字符
# re.M re.MULTILINE   正则表达式中的^操作符能够将给定字符串的每行当作匹配开始
# re.S re.DOTALL      正则表达式中的.操作符能够匹配所有字符，默认匹配除换行外的所有字符

match = re.search(r'[0-9]\d{5}','BIT 100081 200515 352852')
if match:
    print(match)
    print(match.group(0))

# re.match()  从一个字符串的 开始位置 起匹配正则表达式，返回match对象
# re.findall() 搜索字符串，以列表类型返回 全部 能匹配的子串
# 以上格式同 re.search()

# re.split() 将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
# re.split(pattern,string,maxsplit=0,flags=0)
# maxsplit 最大分割数，剩余部分作为最后要给元素输出
print(re.split(r'[0-9]\d{5}','bit100081 tsu100084',maxsplit=1))
print('-'*100)

# re.finditer() 搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象, 迭代了所有搜索结果
# re.sub()   在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串
# count参数表示匹配的最大替换次数

# re.search('\.',ip)
# Out[35]: <_sre.SRE_Match object; span=(3, 4), match='.'>
# span 表示第一次出现，开始位置3，结束位置4


# 面向对象方法
pat = re.compile(r'[1-9]\d{5}')
rst1 = pat.search('bit 100081')
print(rst1)
print(rst1.group(0))
print('='*100)

rst2 = re.search(pat,'bit 100084')
print(rst2)
print(rst2.group(0))



