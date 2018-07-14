# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/21


XML(extensible markup language)
用尖括号标签表达的一种形式
<tag>xxxxx</tage>
<name/>
<!--comment-->
-----------------------------------------------------------------
JSON(Javascript Object Notation)
有类型的键值对 "key":"value" ,value是数字不用""
并列用[]  "name":["北京", "中关村"]
嵌套用{}  "name":{"newname":"beijing","oldname":"zhongguancun"}
------------------------------------------------------------------
YAML(YAML Ain't Markup language)
无类型的键值对  key:value
name:北京  没有双引号

所属用缩进表示
name:
    newname:beijing
    oldname:zhongguancun

用-表示并列关系
name:
    -北京
    -上海

用|表示整块数据，#表示注释
text:|
kasjdflkjsalkfjlaskjfasldkfj

总结
key:value
key:#comment
-value1
-value2
key:
    subkey:subvalue
