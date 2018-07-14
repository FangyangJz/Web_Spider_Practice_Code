# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/18


from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.get('https://www.taobao.com')
browser.get('https://www.python.org')
browser.back()
time.sleep(1)
browser.forward()
browser.close()