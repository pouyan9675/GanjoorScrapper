# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst


def remove_junks(value):
    value = value.replace('\n', '')
    value = value.replace('\t', '')
    value = value.replace('\r', '')
    return value


class Poem(scrapy.Item):
    author = scrapy.Field()
    author_id = scrapy.Field()
    source = scrapy.Field(
        input_processor = MapCompose(remove_junks),
        output_processor = TakeFirst()
    )
    m = scrapy.Field()
