# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/21

# <>.find_all(name, attrs, recursive, string, **kwargs)
# name 对标签名称的检索字符串
# attrs 对标签属性值的检索字符串，可标注属性检索
# recursive 是否对子孙全部检索，默认True
# string  <>...</>中字符串区域的检索字符串

<tag>(...) 等价于 <tag>.find_all(...)
soup(...) 等价于 soup.find_all(...)

扩展：
<>.find()  只返回一个结果
<>.find_parents()
<>.find_parent()
<>.find_next_siblings()
<>.find_next_sibling()
<>.find_previous_siblings()
<>.find_previous_sibling()