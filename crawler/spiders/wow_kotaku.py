#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import scrapy
from ..tools import *


class wowKotakuSpider(scrapy.Spider):
    name = "wow_kotaku"

    start_urls = [
        'http://kotaku.com/tag/world-of-warcraft',
    ]

    def __init__(self):
        self.domain = 'https://kotaku.com'

    def parse(self, response):
        for i in response.xpath('//div[@class="post-wrapper js_post-wrapper "]'):
            image = i.xpath('article/div[@class="item__content js_item-content"]/figure/a/div/picture/source[1]/@data-srcset').extract_first()
            url = i.xpath('article/header/h1[@class="headline entry-title js_entry-title"]/a/@href').extract_first()
            title = i.xpath('article/header/h1[@class="headline entry-title js_entry-title"]/a').extract_first()
            title = removeAllTags(title)
            content = i.xpath('article/div[@class="item__content js_item-content"]/div').extract_first()
            content = removeAllTags(content)
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

