# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/25

# 生成器 yield 更节省空间，更快的响应速度，使用灵活

def gen_yield(n):
    for i in range(n):
        yield i**2

def gen_return(n):
        return n**2

def square(n):
    ls = [i**2 for i in range(n)]
    return ls

#########################################

for i in gen_yield(5):
    print(i)

print('-'*50)

for j in range(5):
    print(gen_return(j))

print('='*50)

for i in square(5):
    print(i)

