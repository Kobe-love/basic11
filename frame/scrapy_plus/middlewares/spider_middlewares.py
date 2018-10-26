class SpiderMiddleware(object):
    def process_request(self,request):
        print('Spider-中间件--request')
        return request

    def process_response(self,response):
        print('Spider-中间件--response')
        return response
