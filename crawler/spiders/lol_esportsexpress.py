#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import scrapy
from ..tools import *


class LolEsportsexpressSpider(scrapy.Spider):
    name = "lol_esportsexpress"

    start_urls = [
        'http://esportsexpress.com/category/league-of-legends/',
    ]

    def __init__(self):
        self.domain = 'http://esportsexpress.com'

    def parse(self, response):
        for i in response.xpath('//li[@class="element"]'):
            image = i.xpath('article/div[@class="entry-thumb"]/a/img/@src').extract_first()
            url = i.xpath('article/div[@class="entry-thumb"]/a/@href').extract_first()
            title = i.xpath('article/div[@class="entry-content"]/header/h4/a/text()').extract_first()
            content = i.xpath('article/div[@class="entry-content"]/p/text()').extract_first()

            url = cleanUrl(self.domain, url)
            image = cleanUrl(self.domain, image)
            ratio = getImgRatio(image)

            yield {
                'title': title,
                'url': url,
                'image': image,
                'content': content,
                'postDate': datetime.datetime.now(),
                'tag': ['League of Legends'],
                'imgRatio': ratio,
                'language': 'English'
            }
