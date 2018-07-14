# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/13


import requests


response = requests.get('https://www.jianshu.com')
print(type(response.status_code),response.status_code)
print('-'*50)
print(type(response.headers),response.headers)
print('-'*50)
print(type(response.cookies),response.cookies)
print('-'*50)
print(type(response.url),response.url)
print('-'*50)
print(type(response.history),response.history)