# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/13


import requests

response = requests.get('https://github.com/favicon.ico')
print(type(response.text),type(response.content))
print(response.text)
print(response.content)

with open('favicon1.ico','wb') as f:
    f.write(response.content)
    f.close()