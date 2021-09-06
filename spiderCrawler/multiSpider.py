import scrapy
from scrapy.crawler import CrawlerProcess
from spiderCrawler.spiders.LinkCrawl import CrawlSpider

process = CrawlerProcess(settings={
    'FEED_URI': 'link.csv',
    'FEED_FORMAT': 'csv'
})

for i in range(1, 10):
    process.crawl(CrawlSpider, i*10)

process.start()
