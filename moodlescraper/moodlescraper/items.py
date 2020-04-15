# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MoodlescraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    course_assign = scrapy.Field()
    course_link = scrapy.Field()
    course_id = scrapy.Field()
    course_title = scrapy.Field()
    due_date = scrapy.Field()
    pass
