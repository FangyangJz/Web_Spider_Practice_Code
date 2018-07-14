# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/13


import requests


response = requests.get('https://www.baidu.com')
print(response.cookies)
for key, value in response.cookies.items():
    print(key + '=' + value)