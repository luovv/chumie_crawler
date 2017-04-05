#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import scrapy
from ..tools import *
import json

class footballDongqiudiSpider(scrapy.Spider):
    name = "football_dongqiudi"

    start_urls = [
        'https://m.dongqiudi.com/api/mobile/tab/1/archives',
    ]

    def __init__(self):
        self.domain = 'https://m.dongqiudi.com/'

    def parse(self, response):
        item = json.loads(response.body_as_unicode())
        for i in item['list']['articles']:
            image = i['litpic']
            url = 'http://www.dongqiudi.com/share/article/'+str(i['aid'])
            title = i['title']
            content = i['description']

            url = cleanUrl(self.domain, url)
            ratio = getImgRatio(image)

            if content is None:
                content=''

            yield {
                'title': title,
                'url': url,
                'image': image,
                'content': content,
                'postDate': datetime.datetime.now(),
                'tag': ['football'],
                'imgRatio': ratio,
                'language': 'Chinese'
            }
