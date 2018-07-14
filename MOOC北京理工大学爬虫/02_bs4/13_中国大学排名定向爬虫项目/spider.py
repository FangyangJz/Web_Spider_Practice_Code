# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/21


import requests
from bs4 import BeautifulSoup
import bs4

def get_html_text(url):

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except:
        print('爬取有问题')

def fill_univ_list(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children: # find('tbody')换成tbody 可行？ -- 可行
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')  # <tag>(...) 等价于 <tag>.find_all(...)
            # print(tds)
            ulist.append([tds[0].string, tds[1].string, tds[3].string])

def print_univ_list(ulist, num):
    tlp = "{0:^10}\t{1:{3}^10}\t{2:^10}"   # chr(12288) 中文空格 去填充{3}
    print(tlp.format("排名", '学校名称', '总分', chr(12288)))  #{:^6} 老师用这种写法会报错
    for i in range(num):
        u = ulist[i]
        print(tlp.format(u[0], u[1], u[2], chr(12288)))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html'
    html = get_html_text(url)
    fill_univ_list(uinfo, html)
    print_univ_list(uinfo,20)


if __name__ == '__main__':
    main()
