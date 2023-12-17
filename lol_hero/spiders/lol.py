import time
from json import loads

import scrapy
from scrapy import Selector
from scrapy import Request

from lol_hero.items import LolHeroItem


class LolSpider(scrapy.Spider):
    name = "lol"
    # allowed_domains = ["101.qq.com"]
    start_urls = ["https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2838037"]

    def parse(self, response, **kwargs):
        hero_dict = loads(response.text)
        for hero in hero_dict['hero']:
            _id = hero['instance_id']
            name = hero['name']
            src = f'https://game.gtimg.cn/images/lol/act/img/skin/big_{_id}.jpg'
            item = LolHeroItem()
            item['src'] = src
            item['name'] = name
            yield item
        pass
