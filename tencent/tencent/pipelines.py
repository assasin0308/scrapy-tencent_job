# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
class TencentPipeline(object):
    def __init__(self):
        self.filename = open('tencent.json','w')

    def process_item(self, item, spider):
        json_txt = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.filename.write(json_txt.encode('utf-8'))
        return item

    def spider_close(self):
        self.filename.close()