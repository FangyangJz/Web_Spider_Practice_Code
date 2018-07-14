# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/20


import requests

try:
    kv = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get('https://www.amazon.cn/gp/product/B06ZXRPZ77',headers=kv)
    print(r.status_code)
    print(r.encoding)
    print(r.request.headers)
    print('-'*50)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])

except:
    print('有问题')