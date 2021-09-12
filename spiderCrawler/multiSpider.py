from scrapy.crawler import CrawlerProcess
from spiderCrawler.spiders.LinkCrawl import CrawlSpider
from scrapy.utils.project import get_project_settings


process = CrawlerProcess()
totalPageCount = 653
setting = get_project_settings()
spiderPageCount = setting.get('CLOSESPIDER_PAGECOUNT')

for i in range(1, totalPageCount + 1, spiderPageCount):
    if i + spiderPageCount > totalPageCount + 1:
        setting.update({
            'CLOSESPIDER_PAGECOUNT': totalPageCount - i
        })
        process = CrawlerProcess(setting)

    process.crawl(CrawlSpider, i)

process.start()
