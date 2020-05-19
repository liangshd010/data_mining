# -*- coding: utf-8 -*-
import scrapy


class OloSpider(scrapy.Spider):
    name = 'olo'
    allowed_domains = ['www.hfbank.com.cn']
    start_urls = ['http://www.hfbank.com.cn/']

    def parse(self, response):
        pass
