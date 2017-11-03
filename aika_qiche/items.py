# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AikaQicheItem(scrapy.Item):
	cat = scrapy.Field()
	comp_name = scrapy.Field()
	comp_url = scrapy.Field()
	phone = scrapy.Field()
	addr = scrapy.Field()
	intro = scrapy.Field()
	short = scrapy.Field()
	jibie = scrapy.Field()
