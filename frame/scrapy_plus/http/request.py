class Request(object):
    def __init__(self, url, method="GET", headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",}, params={}, data={}):
        self.url = url
        self.method = method
        self.headers = headers
        self.params = params
        self.data = data

