#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import scrapy
from ..tools import *
import json

class overwatchBlizzardSpider(scrapy.Spider):
    name = "overwatch_blizzard"

    start_urls = [
        'http://ow.blizzard.cn/action/article/main-body?t=1491155180646',
    ]

    def __init__(self):
        self.domain = 'http://ow.blizzard.cn'

    def parse(self, response):
        item = json.loads(response.body_as_unicode())
        for i in item['data']['news']['news_List']:
            image = i['thumbnailUrl']
            url = i['linkUrl']
            title = i['title']
            content = i['description']

            url = cleanUrl(self.domain, url)
            ratio = getImgRatio(image)

            yield {
                'title': title,
                'url': url,
                'image': image,
                'content': content,
                'postDate': datetime.datetime.now(),
                'tag': ['守望先锋'],
                'imgRatio': ratio,
                'language': 'Chinese'
            }