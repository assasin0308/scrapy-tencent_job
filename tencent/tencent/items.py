# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # 职位名称
    position_name = scrapy.Field()
    # 详情连接
    position_link = scrapy.Field()
    # 职位类别
    position_type = scrapy.Field()
    # 招聘人数
    people_num = scrapy.Field()
    # 工作地点
    location = scrapy.Field()
    # 发布时间
    pub_time = scrapy.Field()

