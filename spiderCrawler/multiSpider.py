from scrapy.crawler import CrawlerProcess
from spiderCrawler.spiders.LinkCrawl import CrawlSpider
from scrapy.utils.project import get_project_settings


process = CrawlerProcess()
totalPageCount = 15
setting = get_project_settings()
spiderPageCount = setting.get('CLOSESPIDER_PAGECOUNT')

for i in range(1, totalPageCount, spiderPageCount):
    if i + spiderPageCount >= totalPageCount:
        setting.update({
            'CLOSESPIDER_PAGECOUNT': totalPageCount - i + 1
        })
        spiderPageCount = setting.get('CLOSESPIDER_PAGECOUNT')
        process = CrawlerProcess(setting)

    process.crawl(CrawlSpider, i)

process.start()
