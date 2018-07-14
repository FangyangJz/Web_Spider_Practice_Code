# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/20


import requests
import os

# 简易代码如下：
# path = 'D:\Python Project in D\WebSpider\MOOC北京理工大学爬虫\dd.jpg'
# url = 'http://image.nationalgeographic.com.cn/2017/1220/20171220113734898.jpg'
# r = requests.get(url)
# print(r.status_code)
#
# with open(path,'wb') as f:
#     f.write(r.content)
#
# f.close()

# 完整代码如下：
url = 'http://image.nationalgeographic.com.cn/2017/1220/20171220113734898.jpg'
root = "D:\Python Project in D\WebSpider\MOOC北京理工大学爬虫//"
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)

    if not os.path.exists(path):
        r = requests.get(url)

        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')

    else:
        print('文件已经存在')

except:
    print('爬取失败')