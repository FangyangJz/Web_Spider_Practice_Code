# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/12

import requests

response = requests.get('https://www.baidu.com')
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)

