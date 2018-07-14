# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/13


import requests


# response = requests.get('https://www.12306.cn')
# print(response.status_code)
#
#  ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:748)

#====================================================================================================================

# response = requests.get('https://www.12306.cn',verify = False)
# print(response.status_code)
#
#  certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
#   InsecureRequestWarning)
# 200

# 去掉上面的警告做法如下：
from requests.packages import urllib3

urllib3.disable_warning()
response = requests.get('https://www.12306.cn',verify = False)
print(response.status_code)

# 也可以指定本地的证书进行验证，代码如下
# response = requests.get('https://www.12306.cn',cert=('path/server.crt','path/key'))

