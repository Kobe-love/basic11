#1spider(1初始化url,2初始化请求对象3 解析shuju
from scrapy_plus.http.request import Request
from scrapy_plus.items import Item


class Spider(object):
    start_urls = {}

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url)

    def parse(self,response):
        return Item(response.url)