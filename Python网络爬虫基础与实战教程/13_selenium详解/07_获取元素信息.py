# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/18


from selenium import webdriver
from selenium.webdriver import ActionChains


browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print('-'*50)
# 获取属性
print(logo.get_attribute('class'))
print('='*50)

# 获取文本
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)
print('-'*50)

# 获取ID、位置、标签名、大小
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)