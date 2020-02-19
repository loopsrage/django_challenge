# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class HeaderspiderSpider(CrawlSpider):
    """Spider for extracting h1-3 tags from a site"""
    name = 'headerspider'

    def __init__(self, *args, **kwargs):
        # Overwriting init to allow passing variables from django views to spiders
        self.url = kwargs.get('url')
        self.domain = kwargs.get('domain')
        self.start_urls = [self.url]
        self.allowed_domains = [self.domain]

        HeaderspiderSpider.rules = [
            Rule(LinkExtractor(unique=True), callback='parse_item')
        ]
        super(HeaderspiderSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        item = {'response': response.xpath('/html/body/*[self::h1 or self::h2 or self::h3]/text()').getall()}
        return item


