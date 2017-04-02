#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import scrapy
from ..tools import *


class overwatchPlayoverwatchSpider(scrapy.Spider):
    name = "overwatch_playoverwatch"

    start_urls = [
        'https://playoverwatch.com/en-us/blog/',
    ]

    def __init__(self):
        self.domain = 'https://playoverwatch.com'

    def parse(self, response):
        for i in response.xpath('//li[@class="blog-info media@md-min"]'):
            image = i.xpath('div[@class="blog-thumbnail media-graphic@md-min"]/a/img/@src').extract_first()
            image = image.replace('//', 'http://')
            url = i.xpath('div[@class="blog-thumbnail media-graphic@md-min"]/a/@href').extract_first()
            title = i.xpath('div[@class="blog-details media-content@md-min margin-12 margin-0@md-min margin-no-sides"]/a/text()').extract_first()
            content = i.xpath('div[@class="blog-details media-content@md-min margin-12 margin-0@md-min margin-no-sides"]/div[@class="summary"]/text()').extract_first()

            url = cleanUrl(self.domain, url)
            ratio = getImgRatio(image)

            yield {
                'title': title,
                'url': url,
                'image': image,
                'content': content,
                'postDate': datetime.datetime.now(),
                'tag': ['overwatch'],
                'imgRatio': ratio,
                'language': 'English'
            }
