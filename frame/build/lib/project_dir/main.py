# from project_dir.spiders.baidu import BaiduSpider
from scrapy_plus.core.engine import Engine
from spiders.baidu import BaiduSpider


if __name__ == '__main__':
    spider = BaiduSpider()
    engine = Engine(spider)

    engine.start()