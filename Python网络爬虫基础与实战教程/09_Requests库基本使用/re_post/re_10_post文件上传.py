# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/13


import requests


file = {'file':open('favicon1.ico','rb')}
response = requests.post('http://httpbin.org/post',files=file)
print(response.text)