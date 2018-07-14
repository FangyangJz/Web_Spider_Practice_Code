# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/24


import re
import requests

def get_html_text(url):

    try:
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
        r = requests.get(url,headers=headers,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('爬取网页有问题')

def parse_page(ilt,html):
    try:
        pattern_price = r'"view_price":"\d+"'
        pattern_title = r'"raw_title":".*?"'
        price_list = re.findall(pattern_price,html)
        title_list = re.findall(pattern_title,html)

        for i in range(len(price_list)):
            price = eval(price_list[i].split(':')[1])
            title = eval(title_list[i].split(':')[1])
            ilt.append([price,title])

    except:
        print('')

def print_goods_list(ilt):
    tplt = '{0:4}\t{1:8}\t{2:16}'
    print(tplt.format('序号', '价格', '商品名称'))
    count = 0

    for g in ilt:
        count += 1
        print(tplt.format(count, g[0], g[1]))

def main():
    goods = '水'
    page_num = 2
    start_url = 'https://s.taobao.com/search?q='+goods
    infolist = []

    for i in range(page_num):
        try:
            url = start_url+'&s='+str(44*i)
            print(url)
            # break
            html = get_html_text(url)
            print(html)
# TODO 这里 html获取有问题，伪造headers后第一次成功爬取，后面就无法爬到正确html
            parse_page(infolist, html)
        except:
            continue

    print_goods_list(infolist)

if __name__ == '__main__':
    main()