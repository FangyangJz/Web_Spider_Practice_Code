# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/13

import requests

response = requests.get('http://httpbin.org/get')
print(response.text)
print('-'*50)

# 带参数get请求
response = requests.get('http://httpbin.org/get?name=germey&age=22')
print(response.text)
print('='*50)

# 上面方法比较繁琐，推荐做法如下：
data = {
    'name':'fanguya',
    'age':29
}
response = requests.get('http://httpbin.org/get',params=data)
print(response.headers)