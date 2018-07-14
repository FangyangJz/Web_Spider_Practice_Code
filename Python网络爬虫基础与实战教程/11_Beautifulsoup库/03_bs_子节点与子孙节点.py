# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/18

html = ''' <ul class="list-col list-col5 list-express slide-item">
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/27179303/?icn=index-editionrecommend" title="伊斯坦布尔假期">
                <img src="https://img3.doubanio.com/lpic/s29587861.jpg" class=""
                  width="115px" height="172px" alt="伊斯坦布尔假期">
              </a>
            </div>
                <div class="intervenor-info">
                    <img src="https://img3.doubanio.com/f/book/ef040178fab1770d60e3f2f12ba4c7aa70714396/pics/book/partner/jd_recommend.png" class='jd-icon' width="16" height="16"/> 
                    <span>推荐</span>
                </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/27179303/?icn=index-editionrecommend"
                  title="伊斯坦布尔假期">伊斯坦布尔假期</a>
              </div>
              <div class="author">
                [法] 马克·李维
              </div>
              <div class="more-meta">
                <h4 class="title">
                  伊斯坦布尔假期
                </h4>
                <p>
                  <span class="author">
                    [法] 马克·李维
                  </span>
                  /
                  <span class="year">
                    2017-12-1
                  </span>
                  /
                  <span class="publisher">
                    湖南文艺出版社
                  </span>
                </p>
                <p class="abstract">

                  生命中总有一些征兆，指引我们相遇。
《偷影子的人》作者马克•李维疗愈之作，全球49国读者热捧，累计销量突破4000万册
神秘又充满异国风情的东方之旅，让整个欧洲为之沦陷的温情故事
调香师阿丽斯在伦敦过着无忧无虑的生活，晚上常在家款待三五好友，喧哗声屡屡引起脾气古怪的邻居戴德利的不满。然而在圣诞前夕，她的美好生活四分五裂，因为一位算命师对她预言：阿丽...
                </p>
              </div>
            </div>
          </li>'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.p.contents)   # 将所有子节点以列表的形式返回回来
print('-'*50)
print(soup.p.children)

for i,child in enumerate(soup.p.children):
    print(i,child)

print('='*50)

for child in enumerate(soup.p.children):
    print(child)

print('>'*50)

for i,child in enumerate(soup.p.descendants):
    print(i,child)