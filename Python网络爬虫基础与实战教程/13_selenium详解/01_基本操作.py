# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/18

from selenium import webdriver

# browser = webdriver.Firefox()
# browser = webdriver.Edge()
# browser = webdriver.PhantomJS()
# browser = webdriver.Safari()

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
print(browser.page_source)
browser.close()