class Response(object):
    def __init__(self, url, code, headers, body, request):
        self.url = url
        self.code = code
        self.headers = headers
        self.body = body
        self.request = request