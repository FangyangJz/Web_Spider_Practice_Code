# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/13


#前提本地开了代理
import requests

proxies = {
    'http':'http://ip address:port',
    'https':'https://ip address:port',
    'http':'http://user:password@ip address:port' #存在用户名和密码的代理
}

response = requests.get('url',proxies=proxies)
print(response.status_code)

# 如果用sock代理，pip install requests[socks] 安装相应模块
proxies = {
    'http':'socks5://ip address:port',
    'https':'socks5://ip address:port
}
