from lxml import etree
from bs4 import BeautifulSoup

import re
import json


class Response(object):
    def __init__(self, url, code, headers, body, request):
        self.url = url
        self.code = code
        self.headers = headers
        self.body = body
        self.request = request

    #多解析方法
    #1.xpath
    def xpath(self,rule):
        html_data = etree.HTML(self.body)
        result_list = html_data.xpath(rule)
        return result_list
    #2.bs4
    def bs4_selecct(self,selector):
        soup = BeautifulSoup(self.body,'lxml')
        result = soup.select(selector=selector)
    #3.re
    def re_find_all(self,pattern,data):
        if data is None:
            self._data = self.body
        return re.findall(pattern,self._data)
    #4.json
    @property
    def json(self):
        #self.body 必须是标准的json格式
        return json.loads(self.body)