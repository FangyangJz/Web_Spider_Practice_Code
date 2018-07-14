# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/18

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://weibo.com')
time.sleep(2)

input = browser.find_element_by_class_name('W_input')
input.send_keys('景方阳')
input = browser.find_element_by_class_name('enter_psd')
input.send_keys('naomoe1988lcy')
button = browser.find_element_by_class_name('W_btn_a btn_32px')
button.click()
