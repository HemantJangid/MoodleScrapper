# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import MoodlescraperItem


class MoodleSpiderSpider(scrapy.Spider):
    name = 'moodle'
    allowed_domains = ['moodle.suas.ac.in']
    start_urls = ['http://moodle.suas.ac.in/']

    def parse(self, response):
        return FormRequest.from_response(response, formdata={
            'username': 'hemantjangid',
            'password': 'hj@3885J'
        }, callback=self.start_scraping)

    def start_scraping(self, response):
        items = MoodlescraperItem()
        courses = response.css('div.coursebox')
        for course in courses:
            course_title = course.css('h2.title a::text').extract_first()
            course_id = course.css('div.coursebox::attr(id)').extract_first().strip('course-')
            id_selector = 'div#region_' + course_id + '_assign_caption'
            course_link = course.css('h2.title a::attr(href)').extract_first()
            course_assign = course.css(id_selector).css('::text').extract_first()
            if course_assign is not None:
                value = course.css('.name a::text').extract_first()
                due_date = course.css('.info::text').extract_first().strip('Due date: ')
                items['course_assign'] = value
                items['due_date'] = due_date
            else:
                items['course_assign'] = 'no assignment available'
                items['due_date'] = 'Not available'
            items['course_title'] = course_title
            items['course_id'] = course_id
            items['course_link'] = course_link
            yield items

