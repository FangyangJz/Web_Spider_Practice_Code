# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/13


import requests
import json

response = requests.get('http://httpbin.org/get')
print(type(response.text))

# 下面这两句等价
print(response.json())
print(json.loads(response.text))

print(type(response.json()))

