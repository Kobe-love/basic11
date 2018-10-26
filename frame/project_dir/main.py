# from project_dir.spiders.baidu import BaiduSpider
from scrapy_plus.core.engine import Engine
from project_dir.spiders.baidu import BaiduSpider
from project_dir.spiders.douban import DoubanSpider


if __name__ == '__main__':
    # baidu = BaiduSpider()
    douban = DoubanSpider()
    engine = Engine(douban)

    engine.start()