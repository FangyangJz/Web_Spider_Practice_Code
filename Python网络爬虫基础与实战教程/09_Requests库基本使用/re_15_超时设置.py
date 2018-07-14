# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/13


import requests
from requests.exceptions import ReadTimeout

response = requests.get('https://www.baidu.com',timeout=1)
# 注意：timeout等号这里不能加空格
print(response.status_code)


try:
    response = requests.get('http://httpbin.org/get',timeout=0.2)
    print(response.status_code)
except ReadTimeout:
    print('timeout')