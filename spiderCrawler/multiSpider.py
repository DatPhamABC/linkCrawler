import scrapy
from scrapy.crawler import CrawlerProcess
from spiderCrawler.spiders.LinkCrawl import CrawlSpider

process = CrawlerProcess(
#     settings={
#     'FEED_URI': 'link.csv',
#     'FEED_FORMAT': 'csv'
# }
)

for i in range(0, 20):
    pageCount = 50
    process.crawl(CrawlSpider, i*pageCount+1)

process.start()
