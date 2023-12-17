# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import requests
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class LolHeroPipeline:
    def process_item(self, item, spider):
        self.save_image(item['src'], item['name'])
        return item

    def save_image(self, url, name):
        file_name = f"{name}.jpg"
        res = requests.get(url)
        if 200 == res.status_code:
            with open(fr"D:\code\python_project\lol_hero\img\{file_name}", "wb") as file:
                file.write(res.content)
