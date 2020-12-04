# -*- coding: utf-8 -*-
import scrapy
import re

from scrapy.http import Request
# from tutorial.items import DmozItem


class DpSpider(scrapy.Spider):
    name = "dzdp_spider"
    allowed_domains = ["dianping.com"]

    #start_urls = ['http://www.dianping.com/search/category/2/10/r2578p1']
    start_urls = []
    for i in range(1,51):
        start_urls.append('http://www.dianping.com/shanghai/ch10/p'+str(i))

    handle_httpstatus_list = [404,403]

    def parse(self,response):
        print('_0_________')
        print(response.url)
        if response.status == 403:
            print ('meet 403, sleep 600 sconds')
            import time
            time.sleep(6)
            yield Request(response.url,callback=self.parse)
        #404,页面不存在，直接范围即可
        elif response.status == 404:
            print('meet 404,return')
        else:
            
            hxs = scrapy.Selector(response)
