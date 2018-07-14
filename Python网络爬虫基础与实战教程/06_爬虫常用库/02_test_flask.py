# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Fangyang  time:2017/12/15


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_worl():
    return 'Hello World'


if __name__ == '__main__':
    app.run()