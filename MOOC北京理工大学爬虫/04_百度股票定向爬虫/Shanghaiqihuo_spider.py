# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/3/16


import requests
import re
from bs4 import BeautifulSoup
import bs4
import numpy as np


def get_html_text(url): # 这里加参数 code='utf-8'

    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
        r = requests.get(url, headers=headers,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding # 这里省略可以节省时间
        return r.text
    except:
        print('获取list有问题')

def url_generator(date):
    '''url生成, date格式为 '20180316' '''
    head = 'http://www.czce.com.cn/portal/DFSStaticFiles/Future/'
    middle = date[:4] + '/' + date
    tail = '/FutureDataHolding.htm'
    return head + middle + tail

def main():

    # future_daily_holding_url = url_generator('20180316')

 # 为了调试程序, 避免每次从网站下载数据, 将数据下载到本地存成html.txt文件
    url = 'http://www.shfe.com.cn/data/dailydata/kx/pm20180308.dat'
    html = get_html_text(url)
    # 后期不需要存到本地可以去掉下面这两句
 #    with open('html.txt','w', encoding='utf-8') as f:
 #        f.write(html)

    print(html)


if __name__ == '__main__':
    main()