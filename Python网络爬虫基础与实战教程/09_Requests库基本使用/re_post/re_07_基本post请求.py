# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/13


import requests

data = {'name':'fangya','age':22}
response = requests.post('http://httpbin.org/post',data=data)
print(response.text)
print('-'*50)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}
response = requests.post('http://httpbin.org/post',data=data,headers=headers)
print(response.json())