# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/24

# 在优化教程里，老师教了print 显示进度的方法

import requests
import re
from bs4 import BeautifulSoup
import traceback


def get_html_text(url):  # 这里加参数 code='utf-8'

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding  # 这里省略可以节省时间
        return r.text
    except:
        print('东方财富获取股票list有问题')


def get_stock_list(list, stockurl):
    html = get_html_text(stockurl)  # 'GB2312'
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')

    for i in a:
        try:
            href = i.attrs['href']
            list.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue

    print('a标签遍历后加入到list中')


def get_stock_info(list, stockurl, fpath):
    """

    :rtype: object
    :param list: 
    :param stockurl: 
    :param fpath: 
    """
    for stock in list:
        url = stockurl + stock + ".html"
        html = get_html_text(url)

        try:
            if html == '':
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class': 'stock-bets'})

            name = stockInfo.find(attrs={'class': 'bets-name'})
            infoDict.update({'股票名称': name.text.split()[0]})

            key_list = stockInfo.find_all('dt')
            value_list = stockInfo.find_all('dd')

            for i in range(len(key_list)):
                key = key_list[i].text
                val = value_list[i].text
                infoDict[key] = val

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')

        except:
            traceback.print_exc()
            continue


def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'  # sz002439.html'
    output_file = 'D:\\baidustock.txt'
    slist = []

    get_stock_list(slist, stock_list_url)
    get_stock_info(slist, stock_info_url, output_file)


if __name__ == '__main__':
    main()
