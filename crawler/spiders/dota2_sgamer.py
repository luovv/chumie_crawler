#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import scrapy
from ..tools import *
import re


class Dota2SgamerSpider(scrapy.Spider):
    name = "dota2_sgamer"
    # 网站入口
    start_urls = [
        'http://dota2.sgamer.com/',
    ]

    def __init__(self):
        self.domain = 'http://dota2.sgamer.com'

    def parse(self, response):
        for i in response.xpath('//li[@class="index-new"]'):
            url = i.xpath('div[@class="news-list"]/h2[@class="tit"]/a/@href').extract_first()
            image = i.xpath('a[@class="img"]/img/@src').extract_first()

            url = cleanUrl(self.domain, url)
            image = cleanUrl(self.domain, image)
            ratio = getImgRatio(image)

            if not 'video' in url:
                # 请求详情页callback到parse_detail
                request = scrapy.Request(url, callback=self.parse_detail)
                request.meta['url'] = url
                request.meta['image'] = image
                request.meta['ratio'] = ratio
                yield request

    def parse_detail(self, response):
        url = response.meta['url']
        image = response.meta['image']
        ratio = response.meta['ratio']
        content=response.xpath('//div[@class="text"]').extract_first()
        dr = re.compile(r'<[^>]+>', re.S)
        content = dr.sub('', content)
        content = content.replace('\n', '')
        content = content.replace('\t', '')
        content = content.replace('\r', '')
        yield {
            'title': response.xpath('//h1/text()').extract_first(),
            'url': url,
            'image': image,
            'content': content,
            'postDate': datetime.datetime.now(),
            'tag': ['dota2'],
            'imgRatio': ratio,
            'language':'Chinese'
        }

