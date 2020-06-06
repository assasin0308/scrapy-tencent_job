# -*- coding: utf-8 -*-
import scrapy


class TencentJobSpider(scrapy.Spider):
    name = 'tencent_job'
    allowed_domains = ['tencent.com']
    start_urls = ['http://tencent.com/']

    def parse(self, response):
        pass
