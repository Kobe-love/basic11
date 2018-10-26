"""
2 scheduler（1 入队列
 出队列
 去重
"""""
from six.moves.queue import Queue
from scrapy_plus.utils.log import logger
# from queue import Queue

class Scheduler(object):

    def __init__(self):
        self.queue = Queue()

    def add_request(self,request):
        self.queue.put(request)

    def get_request(self):
        # request = self.queue.get_nowait()
        try:
            request = self.queue.get(False)
            return request
        except Exception as e:
            logger.info(e)



    def filter_request(self,request):
        pass