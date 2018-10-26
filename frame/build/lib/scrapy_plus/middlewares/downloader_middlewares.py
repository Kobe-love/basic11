class DownloaderMiddleware(object):
    def process_request(self, request):
        print('Downloader-中间件--request')
        return request

    def process_response(self, response):
        print('Downloader-中间件--response')
        return response
