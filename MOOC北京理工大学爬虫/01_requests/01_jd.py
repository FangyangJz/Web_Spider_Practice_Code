# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/20


import requests

try:
    response = requests.get('https://item.jd.com/5181380.html')
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    print(response.text[:1000])

except:
    print('网页有问题')