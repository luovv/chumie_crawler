#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import scrapy
from ..tools import *


class Dota2ThescoreesportsSpider(scrapy.Spider):
    name = "dota2_thescoreesports"
    # 网站入口
    # user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
    start_urls = [
        'http://www.thescoreesports.com/dota2/news',
    ]

    def __init__(self):
        self.domain = 'http://www.thescoreesports.com'

    def parse(self, response):
        for i in response.xpath('//div[@class="article-tile article-tile--has-image"]'):
            image = i.xpath('a/div/img/@src').extract_first()
            url = i.xpath('a/@href').extract_first()
            title = i.xpath('a/div/div/div[@class="article-tile__headline ff-condensed"]/text()').extract_first()
            content = i.xpath('a/div/div/div[@class="article-tile__summary"]/text()').extract_first()

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
