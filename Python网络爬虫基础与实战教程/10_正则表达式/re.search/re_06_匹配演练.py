# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/15

import re

html='''<div class="search-info">
            <ul class="hot-search">
                                <li>
                                        <a class="key" href="/search?key=潘美辰《好久都没有》">潘美辰《好久..</a>
                 </li>
                                <li>
                                        &nbsp;
                                        <a class="key" href="/album/560556360">ACE《千灯愿》</a>
                 </li>
                                <li>
                                        &nbsp;
                                        <a class="key" href="/search?key=二珂《带着音乐去旅行》">二珂《带着音..</a>
                 </li>
                                <li>
                                        &nbsp;
                                        <a class="key" href="/search?key=Scream - Michael Jackson">Scream - Mic..</a>
                 </li>
                                <li>
                                        &nbsp;
                                        <a class="key" href="/search?key=薛之谦">薛之谦</a>
                 </li>
                                <li>
                                        &nbsp;
                                        <a class="key" href="/search?key=五月天">五月天</a>
                 </li>
                                <li>
                                        &nbsp;
                                        <a class="key" href="/search?key=赵传《看不见的地方》">赵传《看不见..</a>
                 </li>
                                <li>
                                        &nbsp;
                                        <a class="key" href="/search?key=《战狼2》电影原声带">《战狼2》电..</a>
                 </li>
                                <li>
                                        &nbsp;
                                        <a class="key" href="/search?key=周杰伦">周杰伦</a>
                 </li>
                                <li>
                                        &nbsp;
                                        <a class="key" href="/search?key=李宗盛">李宗盛</a>
                 </li>
                                <li>
                                        &nbsp;
                                        <a class="key" href="/search?key=成都">成都</a>
                 </li>
                                <li>
                                        &nbsp;
                                        <a class="key" href="/search?key=带你去旅行">带你去旅行</a>
                 </li>
                                <li>
                                        &nbsp;
                                        <a class="key" href="/search?key=莫文蔚">莫文蔚</a>
                 </li>
                                <li>
                                        &nbsp;
                                        <a class="key" href="/search?key=陈奕迅">陈奕迅</a>
                 </li>
                                <li>
                                        &nbsp;
                                        <a class="key" href="/search?key=轻音乐">轻音乐</a>
                 </li>
                                <li>
                                        &nbsp;
                                        <a class="key" href="/search?key=刀郎">刀郎</a>
                 </li>
                                <li>
                                        &nbsp;
                                        <a class="key" href="/search?key=凤凰传奇">凤凰传奇</a>
                 </li>
'''

result = re.search('<a class.*?ey=(.*?)".*?>(.*?)</a>', html, re.S)
if result:
    print(result.group(1),result.group(2))