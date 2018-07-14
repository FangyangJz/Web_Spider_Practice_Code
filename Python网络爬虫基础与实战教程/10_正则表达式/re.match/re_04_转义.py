# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/15

import re

content='price is $5.00'
result = re.match('price is $5.00',content)
print(result)
result = re.match('price is \$5\.00',content)
print(result)