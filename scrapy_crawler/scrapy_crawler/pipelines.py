# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
from content.models import ContentHeader
from content.models import Content


class ScrapyCrawlerPipeline(object):

    def __init__(self, unique_id, content_object, *args, **kwargs):
        self.unique_id = unique_id
        self.content_object = Content.objects.get(pk=content_object)
        self.items = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            # this will be passed from django view
            unique_id=crawler.settings.get('unique_id'),
            content_object=crawler.settings.get('content_object')
        )

    def close_spider(self, spider):
        # And here we are saving our crawled data with django models.

        check_existing = ContentHeader.objects.filter(content_id=self.content_object.id)

        if len(check_existing) < 1:
            item = ContentHeader()
            item.unique_id = self.unique_id
            item.header_text = json.dumps(self.items)
            item.content_id = self.content_object
            item.save()

        else:
            check_existing.header_text = json.dump(self.items)
            check_existing.save()

    def process_item(self, item, spider):
        self.items.append(item['response'])
        return item