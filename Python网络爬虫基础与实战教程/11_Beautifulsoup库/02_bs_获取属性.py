# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/15

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
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/27176647/?icn=index-editionrecommend" title="吃瓜时代的儿女们">
                <img src="https://img3.doubanio.com/lpic/s29590893.jpg" class=""
                  width="115px" height="172px" alt="吃瓜时代的儿女们">
              </a>
            </div>
                <div class="intervenor-info">
                    <img src="https://img3.doubanio.com/f/book/ef040178fab1770d60e3f2f12ba4c7aa70714396/pics/book/partner/jd_recommend.png" class='jd-icon' width="16" height="16"/> 
                    <span>推荐</span>
                </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/27176647/?icn=index-editionrecommend"
                  title="吃瓜时代的儿女们">吃瓜时代的儿女们</a>
              </div>
              <div class="author">
                刘震云
              </div>
              <div class="more-meta">
                <h4 class="title">
                  吃瓜时代的儿女们
                </h4>
                <p>
                  <span class="author">
                    刘震云
                  </span>
                  /
                  <span class="year">
                    2017-11-1
                  </span>
                  /
                  <span class="publisher">
                    长江文艺出版社
                  </span>
                </p>
                <p class="abstract">

                  《吃瓜时代的儿女们》是著名作家刘震云暌违五年的又一力作。
四个素不相识的人，农村姑娘牛小丽，省长李安邦，县公路局长杨开拓，市环保局副局长马忠诚，四人不一个县，不一个市，也不一个省，更不是一个阶层；但他们之间，却发生了极为可笑和生死攸关的联系。八竿子打不着的事，穿越大半个中国打着了。于是，眼看他起高楼，眼看他宴宾客，眼看他楼塌了。
深陷其中的人...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/27202502/?icn=index-editionrecommend" title="个体崛起">
                <img src="https://img1.doubanio.com/lpic/s29613638.jpg" class=""
                  width="115px" height="172px" alt="个体崛起">
              </a>
            </div>
                <div class="intervenor-info">
                    <img src="https://img3.doubanio.com/f/book/ef040178fab1770d60e3f2f12ba4c7aa70714396/pics/book/partner/jd_recommend.png" class='jd-icon' width="16" height="16"/> 
                    <span>推荐</span>
                </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/27202502/?icn=index-editionrecommend"
                  title="个体崛起">个体崛起</a>
              </div>
              <div class="author">
                陈立飞
              </div>
              <div class="more-meta">
                <h4 class="title">
                  个体崛起
                </h4>'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')

# 获取属性
# print(soup.a.attrs['title'])
# print(soup.a['href'])

# 获取内容
print(soup.p.span.string) # 获取第一个p标签里面的内容,层层嵌套
print('-'*50)
print(soup.li.a)
print('-'*50)
print(soup.li.a['href']) # 获取属性

