# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/13


import requests
from requests.exceptions import ReadTimeout,HTTPError,ConnectionError


try:
    response = requests.get('http://httpbin.org/get', timeout = 0.4)
    print(response.status_code)

except ReadTimeout:
    print('time out')

except HTTPError:
    print('http error')

# except RequestException:
#     print('error')

except ConnectionError:
    print('网络不通啊')