# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/3/18

import requests
import re
from bs4 import BeautifulSoup
import bs4
import numpy as np


def get_html_text(url): # 这里加参数 code='utf-8'

    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
        form = {'memberDealPosiQuotes.variety':'cs',
                'memberDealPosiQuotes.trade_type':'0',
                'year':'2018',
                'month':'2',
                'day':'08',
                'contract.contract_id':'all',
                'contract.variety_id':'cs'}  # 'cs' 是品种代码
        # r = requests.get(url, headers=headers,timeout=30)
        r = requests.post(url, data=form, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding # 这里省略可以节省时间
        return r.text
    except:
        print('获取list有问题')

if __name__ == '__main__':

    # url = 'http://www.dce.com.cn/dalianshangpin/xqsj/tjsj26/rtj/rcjccpm/index.html'
    # '/dalianshangpin/xqsj/tjsj26/rtj/rcjccpm/index.html'
    url = 'http://www.dce.com.cn/publicweb/quotesdata/memberDealPosiQuotes.html'
    html = get_html_text(url)
    print(html)