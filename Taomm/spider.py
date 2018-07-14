# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/8


import requests
from str_dict import str_dict
from json import loads
import re

def get_user_list():

    data = '''q:
viewFlag:A
sortType:default
searchStyle:
searchRegion:city:
searchFansNum:
currentPage:1
pageSize:100
'''

    response = requests.post('https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8', data = str_dict(data))
    html = response.text
    # print html
    result = loads(html)
    # print result
    return result['data']['searchDOList']


def get_album_list(userid):

    response = requests.get('https://mm.taobao.com/self/album/open_album_list.htm?_charset=utf-8&user_id%20={}'.format(userid))
    html = response.text
    reg = r'<a class="mm-first" href="//mm.taobao.com/self/album_photo.htm(.*?)" target="_blank">'
    # 正则表达式 需要熟练使用
    # print (html)
    urlist = set(re.findall(reg,html)) #set 去重
    return urlist

def get_photo_list(url):

    response = requests.get('https://mm.taobao.com/album/json/get_album_photo_list.htm{}'.format(url))
    html = response.text
    result = loads(html)
    return result['picList']


for user in get_user_list():
    userid = user['userId']
    urllist = get_album_list(userid)

    for i in urllist:
        for n in get_photo_list(i):
            print (n['picUrl'][:-14])

    # break