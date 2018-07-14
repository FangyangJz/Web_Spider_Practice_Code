# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/18

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')

input_first = browser.find_element_by_id('q') #查找单个元素
# input_first = browser.find_element(By.ID,'q')  #自己试了一下，By.ID没有定义

input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first,input_second,input_third)
