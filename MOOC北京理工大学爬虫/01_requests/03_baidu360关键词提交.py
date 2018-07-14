# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/20


import requests

kv = {'wd':'Python'}
r = requests.get('http://www.baidu.com/s',params=kv)
print(r.status_code)
print(r.request.url)
print(len(r.text))
# print(r.text)