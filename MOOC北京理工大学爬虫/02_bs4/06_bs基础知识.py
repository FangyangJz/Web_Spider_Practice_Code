# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/21

# 两种引入方式，第一种常用
# from bs4 import BeautifulSoup
# import bs4

# soup = BeautifulSoup("<html></html>","html.parser")
# soup2 = BeautifulSoup(open("D://demo.html"),"html.parser")

bs4  的 html 解析器 BeautifulSoup(mk,'html.parser')
lxml 的 html 解析器 BeautifulSoup(mk,'lxml')
lxml 的 xml 解析器 BeautifulSoup(mk,'xml')
html5lib 的解析器 BeautifulSoup(mk,'html5lib')  需要pip install html5lib

BeautifulSoup 类的基本元素
Tag  标签，最基本的信息组织单元，分别用<>和</>标明开头和结尾
Name 标签的名字，<p>...</p>的名字是'p'，格式：<tag>.name
Attributes 标签的属性，字典形式组织，格式：<tag>.attrs
NavigableString 标签内非属性字符串，<>...</>中字符串，格式：<tag>.string
Comment 标签内字符串的注释部分，一种特殊的Comment类型