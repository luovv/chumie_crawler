#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import scrapy
from ..tools import *
import json

class nbaBasketballinsidersSpider(scrapy.Spider):
    name = "nba_basketballinsiders"

    start_urls = [
        'http://www.basketballinsiders.com',
    ]

    def __init__(self):
        self.domain = 'http://www.basketballinsiders.com'

    def parse(self, response):
        for i in response.xpath('//li[@class="infinite-post"]'):

            image = i.xpath('div[@class="blog-layout2-img"]/a/img/@src').extract_first()
            url = i.xpath('div[@class="blog-layout2-img"]/a/@href').extract_first()
            title = i.xpath('div[@class="blog-layout2-text"]/h2/a/text()').extract_first()
            content = i.xpath('div[@class="blog-layout2-text"]/p/text()').extract_first()

            ratio = getImgRatio(image)

            yield {
                'title': title,
                'url': url,
                'image': image,
                'content': content,
                'postDate': datetime.datetime.now(),
                'tag': ['Basketball'],
                'imgRatio': ratio,
                'language': 'English'
            }
