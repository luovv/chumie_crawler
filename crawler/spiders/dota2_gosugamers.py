#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import scrapy
import re


class Dota2GosugamersSpider(scrapy.Spider):
    name = "dota2_gosugamers"
    # 网站入口
    start_urls = [
        'http://www.gosugamers.net/dota2/news',
    ]
    # 通过列表页采集详情页url
    def parse(self, response):
        for i in response.xpath('//div[@class="showcase-slide"]'):
            image = i.xpath('div[@class="showcase-content"]/a/img/@src').extract_first()
            url = i.xpath('div[@class="showcase-caption"]/h2/a/@href').extract_first()
            title = i.xpath('div[@class="showcase-caption"]/h2/a/text()').extract_first()
            content = i.xpath('div[@class="showcase-caption"]/p/text()').extract_first()
            ratio = 520/860
            # 有的url是相对路径，改成绝对路径
            if not 'http' in url:
                url = 'http://www.gosugamers.net'+url
            if not 'http' in image:
                image = 'http://www.gosugamers.net'+url   

            yield {
                'title': title,
                'url': url,
                'image': image,
                'content': content,
                'crawledDate:': datetime.datetime.now(),
                'tag': ['dota2'],
                'imgRatio':ratio
            }

