# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VikashItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Web1Item(scrapy.Item):
    Name = scrapy.Field()
    Caption = scrapy.Field()
    functionalarea = scrapy.Field()
    Description = scrapy.Field()
    Qualification = scrapy.Field()
    Experience = scrapy.Field()
    Salary = scrapy.Field()
    Address = scrapy.Field()
    landmark = scrapy.Field()
    mobile = scrapy.Field()
    slug = scrapy.Field()
