# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/8

s = '''q:
viewFlag:A
sortType:default
searchStyle:
searchRegion:city:
searchFansNum:
currentPage:1
pageSize:100'''

def str_dict(s):

    tmp_list = s.split('\n')
    dict = {}

    for i in tmp_list:

        if i :
            t_list = i.split(':')
            # print t_list
            dict[t_list[0]] = t_list[1]

    # print(dict)

if __name__ == '__main__':

    str_dict(s)