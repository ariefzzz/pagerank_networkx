# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PtatrunojoyoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ItemTugasAkhir(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    link_keluar = scrapy.Field()
    situsKe = scrapy.Field()
    linkKe = scrapy.Field()
    deep = scrapy.Field()