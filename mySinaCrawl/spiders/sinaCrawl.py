# -*- coding: utf-8 -*-
import scrapy


class SinacrawlSpider(scrapy.Spider):
    name = 'sinaCrawl'
    allowed_domains = ['m.weibo.cn']
    start_urls = ['http://m.weibo.cn/']

    def parse(self, response):
        pass
