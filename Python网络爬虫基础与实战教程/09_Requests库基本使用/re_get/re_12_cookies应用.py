# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/13


import requests

# 以下三行获取不到设置的cookies，是因为相当于分别发了两次get，用不同的浏览器
requests.get("http://httpbin.org/cookies/set/number/123456789")
response = requests.get('http://httpbin.org/cookies')
print(response.text)
print('-'*50)

# 维持会话信息 改进如下
s = requests.session()
s.get('http://httpbin.org/cookies/set/number/123456789')
response = s.get('http://httpbin.org/cookies')
print(response.text)