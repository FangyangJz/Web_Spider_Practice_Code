# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/8

######################### python 3 code 如下：

# import urllib.request
#
# response = urllib.request.urlopen('http://www.baidu.com')
# print (response.read().decode('utf-8'))

#######################################



######################### python 2 code 如下：

import urllib

response = urllib.urlopen('http://www.baidu.com')
print (response.read().decode('utf-8'))

########################################################