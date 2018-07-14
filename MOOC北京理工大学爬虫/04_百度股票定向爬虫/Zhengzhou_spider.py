# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2018/3/16


import requests
from bs4 import BeautifulSoup
import bs4
import pandas as pd
import numpy as np

from pymongo import *
import json


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

def numstring_to_int(numstring):
    '''将数字字符串中的逗号去掉'''
    return int(numstring.replace(',',''))

def head_format_deal(list1):
    '''把品种那行字符串分列, 并转成字典'''
    dict_xx = {}
    list1 = list1[0].split()
    list1 = [x.split('：') for x in list1]
    for i in list1:
        dict_xx.update({i[0]: [i[1]]})
    return dict_xx

def get_tables(tbody):
    '''获得DataFrame格式的tables, 第一行需要处理下'''
    for tr in tbody:

        if isinstance(tr, bs4.element.Tag):

            tr_contents = tr.find_all('td')
            list1 = []

            for i in range(len(tr_contents)):

                list1.append(tr_contents[i].string)

            # 接下来将列表类型的结果转化成字典结构, 为后面入库做准备
            dict_data = {}
            # 判断 品种和日期 , 转成字典形式
            if '日期' in list1[0]:
                # print(head_format_deal(list1))
                dict_data.update(head_format_deal(list1))
                # print(dict_data)
                # 将品种 日期 赋值给dict_data_head用于保留结果
                dict_data_head = dict_data
                df_head = pd.DataFrame(dict_data_head)

            elif '名次' in list1[0]:
                # columns 选择分支
                columns = list1
                # columns 里面有重名的, 后面转成json存数据库会很麻烦
                # 所以要在这里处理一下
                columns[3] = '增减量0'
                columns[4] = '持买会员'
                columns[6] = '增减量1'
                columns[7] = '持卖会员'
                columns[9] = '增减量2'

                df_temp = pd.DataFrame(np.array([0] * 10).reshape(1, 10), columns=columns)
                df_temp_all = pd.concat([df_head, df_temp], axis=1)

            elif '合计' in list1[0]:
                '''一张表最后行, 完成, 出口'''
                df_data = pd.DataFrame(np.array(list1).reshape(1, 10), columns=columns)
                # data 和 head品种日期 合并
                df_data_onerow = pd.concat([df_head, df_data], axis=1)
                df_temp_all = pd.concat([df_temp_all, df_data_onerow], axis=0,ignore_index=True)

                # TODO 函数出口在此
                yield df_temp_all

            else:
                # data 选择分支
                df_data = pd.DataFrame(np.array(list1).reshape(1, 10), columns=columns)
                # data 和 head品种日期 合并
                df_data_onerow = pd.concat([df_head, df_data], axis=1)
                df_temp_all = pd.concat([df_temp_all, df_data_onerow], axis=0)
                # print(df_data_onerow)

def main():

    future_daily_holding_url = url_generator('20180316')
 # 为了调试程序, 避免每次从网站下载数据, 将数据下载到本地存成html.txt文件
 #    html = get_html_text(future_daily_holding_url)
    # 后期不需要存到本地可以去掉下面这两句
 #    with open('html.txt','w', encoding='utf-8') as f:
 #        f.write(html)
    with open('html.txt', 'r',encoding='utf-8') as f:
        html = f.read()

    # soup = BeautifulSoup(html, 'html.parser')
    soup = BeautifulSoup(html, 'lxml')
    soup.prettify()
    tbody = soup.body.table.tr.td.table

    for i in get_tables(tbody):
        # i 是yield 出来的 DataFrame 表格
        i = i.drop([0])
        print(i)

        client = MongoClient('mongodb://localhost:27017')
        db = client.TushareData
        db.zhengzhou.insert(json.loads(i.to_json(orient='records')))


if __name__ == '__main__':
    main()