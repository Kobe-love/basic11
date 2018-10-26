#1爬虫的工作原理
#1 目标url
#2 发送request -- response
#3 解析数据 -- data
#4 保存数据

#2 scrapy的工作原理
    #1spider(1初始化url,2初始化请求对象3 解析shuju

    #2 scheduler（1 入队列 出队列 去重
    #3 downloader（1下载shuju
    #4 pipeline （传递数据
    #5 engine
    #1 spider-- request-- engine
    #2 engine-request --schedle
    #3 schduler--request--engine
    #4 engine- request--downloader
    #5 downloader--response--engine
    #6 engine--response--spider
    #7 spider解析数据 result
    # 如果是request --schduler
    # 如果是item -- pipeline
