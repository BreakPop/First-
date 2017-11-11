# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector


class Spider1Spider(Spider):
    name = 'dmoz'
    allowed_domains = ['dmoz.org']
    start_urls = [
        'http://blog.csdn.net/zhaoguanghui2012/article/details/52032673'
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="directory-url"]/li')
        items = []
        for site in sites:
            item = DmozItem()
            item['title'] = site.xpath('a/text()').extract()
            item['link'] = site.xpath('a/href()').extract()
            item['desc'] = site.xpath('text()').extract()
            items.append(item)
        return items

