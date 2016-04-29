# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BasicScrappingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class LanguageItem(scrapy.Item):
	"""Basic Scrapy Item to find informations about languages"""
	title = scrapy.Field()
	link = scrapy.Field()
	language = scrapy.Field()
	desc = scrapy.Field()