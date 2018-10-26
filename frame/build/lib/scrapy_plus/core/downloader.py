""""
    #3 downloader（1下载shuju

"""""
import requests
from scrapy_plus.http.response import Response


class Downloader(object):
    def get_response(self, request):
        if request.method == "GET":
            response = requests.get(request.url, headers=request.headers, params= request.params)
        elif request.method == "POST":
            response = requests.get(request.url, headers=request.headers, data= request.data)

        else:
            raise Exception("不支持{}请求方式".format(request.method))

        return  Response(url=response.url, code=response.status_code, headers=response.headers, body=response.content, request=request)