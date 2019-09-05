#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : day.py
# Author: MuNian
# Date  : 2019/7/27


import requests
from lxml import etree

count = 1

def Bqb_data(page):

    global count

    # 网页的地址
    url = 'https://fabiaoqing.com/biaoqing/lists/page/{}.html'.format(page)

    # 请求网页后台服务器 并且得到服务器响应的数据
    response_data = requests.get(url).text

    html = etree.HTML(response_data)
    # xpath 元素获取数据
    # //*[@id="bqb"]/div[1]/div[2]/a/img
    # //*[@id="bqb"]/div[1]/div[3]/a/img
    # page = int(input('请输入你要抓取的个数:'))
    # for word in range(1, page):
    #     bqb = html.xpath('//*[@id="bqb"]/div[1]/div[{}]/a/img/@data-original'.format(word))
    #     print(bqb)

    # 通过类选择器来定位数据
    bqb = html.xpath('//*[@id="bqb"]/div[1]/div[@class="tagbqppdiv"]/a/img/@data-original')
    for i in bqb:
        # 发送二次请求 请求图片的地址
        url_image = requests.get(i)
        # a 追加  b 进制文件读写方式
        with open('热门表情包/{}.gif'.format(count), 'ab') as f:
            f.write(url_image.content)
        count += 1


page = int(input('请输入你要抓取的个数:'))
for word in range(1, page):
    Bqb_data(word)