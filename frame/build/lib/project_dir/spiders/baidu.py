from scrapy_plus.core.spider import Spider

# if __name__ == '__main__':
class BaiduSpider(Spider):
    # start_url = 'https://www.jd.com'
    start_urls = {'https://www.jd.com','https://www.baidu.com'}
