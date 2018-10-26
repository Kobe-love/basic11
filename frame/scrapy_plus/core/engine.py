#5 engine
    #1 spider-- request-- engine
    #2 engine-request --schedle
    #3 schduler--request--engine
    #4 engine- request--downloader
    #5 downloader--response--engine
    #6 engine--response--spider
    #7 spider解析数据 result
    # 如果是request --schduler
    # 如果是item -- pipeline
from datetime import datetime

from scrapy_plus.http.request import Request
from scrapy_plus.utils.log import logger
from .spider import Spider
from  .scheduler import Scheduler
from .downloader import Downloader
from .pipeline import Pipeline
# from .middlewares.downloader_middlewares import DownloaderMiddleware
from scrapy_plus.middlewares.downloader_middlewares import DownloaderMiddleware
from scrapy_plus.middlewares.spider_middlewares import SpiderMiddleware
# from .middlewares.spider_middlewares import SpiderMiddleware


class Engine(object):

    def __init__(self,spider):
        # self.url = url
        self.spider_middleware = SpiderMiddleware()
        self.downloader_middleware = DownloaderMiddleware()
        self.spider = spider
        self.scheduler = Scheduler()
        self.downloader = Downloader()
        self.pipeline= Pipeline()
        self.total_request_num = 0
        self.total_response_num = 0
    def start(self):
        start_time = datetime.now()
        # print(3333)
        self._start_engine()
        end_time = datetime.now()
        # print(1111)
        logger.info('总时间{}'.format((end_time-start_time).total_seconds()))
        # print(222)

    def _request(self):
        request = self.scheduler.get_request()
        self.total_request_num += 1
        if request is None:
            return
        request = self.downloader_middleware.process_request(request)
        response = self.downloader.get_response(request)
        self.downloader_middleware.process_response(response)
        # response = self.spider_middleware.process_response(response)
        self.spider_middleware.process_response(response)
        results = self.spider.parse(response)
        for result in results:

            if isinstance(result, Request):
                self.spider_middleware.process_request(request)
                self.scheduler.add_request(result)

            else:
                self.pipeline.process_item(result)
        self.total_response_num += 1

    def _start_engine(self):
        requests = self.spider.start_requests()
        for request in requests:
            request = self.spider_middleware.process_request(request)
            self.scheduler.add_request(request)
        while True:
            self._request()
            if self.total_response_num >= self.total_request_num:
                return

