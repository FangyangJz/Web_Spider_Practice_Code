# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/13

import requests
from requests.auth import HTTPBasicAuth

r = requests.get('url',auth={'user':'password'})
print(r.status_code)