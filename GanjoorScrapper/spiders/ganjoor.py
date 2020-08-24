# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from GanjoorScrapper.items import Poem


deny_urls = [
    '/contact/',
    '/donate/',
    '/sources/',
    '/vazn/',
    '/about/',
    '/hashieha/',
    '/mundex/',
    '/random/',
]


class GanjoorSpider(CrawlSpider):
    name = 'ganjoor'
    allowed_domains = ['ganjoor.net']
    start_urls = ['http://ganjoor.net/']

    rules = (
        Rule(LinkExtractor(deny=deny_urls), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        l = ItemLoader(item=Poem(), response=response)
        l.add_xpath('author_id', '//select[@id = "author"]/option[@selected = "selected"]/@value')
        l.add_css('author', '#author option[selected="selected"]::text')
        l.add_css('source', 'h2 a[rel="bookmark"]::text')
        l.add_css('m', '.b p::text')
        l.add_css('m', '.b2 p::text')
        return l.load_item()
