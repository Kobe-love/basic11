class Request(object):
    def __init__(self, url, method="GET", headers={}, params={}, data={}):
        self.url = url
        self.method = method
        self.headers = headers
        self.params = params
        self.data = data