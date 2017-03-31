#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import scrapy
from ..tools import *



class Dota2GosugamersSpider(scrapy.Spider):
    name = "dota2_gosugamers"
    start_urls = [
        'http://www.gosugamers.net/dota2/news',
    ]

    def __init__(self):
        self.domain = 'http://www.gosugamers.net'

    def parse(self, response):
        for i in response.xpath('//div[@class="showcase-slide"]'):
            image = i.xpath('div[@class="showcase-content"]/a/img/@src').extract_first()
            url = i.xpath('div[@class="showcase-caption"]/h2/a/@href').extract_first()
            title = i.xpath('div[@class="showcase-caption"]/h2/a/text()').extract_first()
            content = i.xpath('div[@class="showcase-caption"]/p/text()').extract_first()
            # 有的url是相对路径，改成绝对路径
            url = cleanUrl(self.domain, url)
            image = cleanUrl(self.domain, image)
            ratio = getImgRatio(image)

            yield {
                'title': title,
                'url': url,
                'image': image,
                'content': content,
                'postDate': datetime.datetime.now(),
                'tag': ['dota2'],
                'imgRatio': ratio,
                'language': 'English'
            }

