# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/12


import requests

# http://httpbin.org/ 测试网站

requests.post('http://httpbin.org/post')
requests.put('http://httpbin.org/put')
requests.head('http://httpbin.org/')
requests.options('http://httpbin.org/')