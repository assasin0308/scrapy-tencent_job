# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class TencentJobSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    url = 'https://careers.tencent.com/search.html?index='
    offset = 1
    start_urls = [
        url + str(offset)
    ]


    def parse(self, response):
        jobs = []
        for each in response.xpath('//div[@class="recruit-list"]'):
            item = TencentItem()
            # 职位名称
            item['position_name'] = each.xpath('./a/h4/text()').extract()[0]
            # 职位类别
            item['position_type'] = each.xpath('/a/p/span[3]/text()').extract()[0]
            # 工作地点
            item['location'] = each.xpath('/a/p/span[2]/text()').extract()[0]
            # 发布时间
            item['pub_time'] = each.xpath('/a/p/span[4]/text()').extract()[0]

            print item['position_name']
            print item['position_type']
            print item['location']
            print item['pub_time']

            yield item
            # jobs.append(item)

        if self.offset < 10:
            self.offset += 1

        # return jobs
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
