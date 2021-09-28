from scrapy.crawler import CrawlerProcess
from spiderCrawler.spiders.LinkCrawl import CrawlSpider
from scrapy.utils.project import get_project_settings


class mulSpider:
    def __init__(self, totalPageCount):
        self.totalPageCount = totalPageCount

    def spiderProcess(self):
        process = CrawlerProcess()
        setting = get_project_settings()
        spiderPageCount = setting.get('CLOSESPIDER_PAGECOUNT')

        for i in range(1, self.totalPageCount, spiderPageCount):
            if i + spiderPageCount >= self.totalPageCount:
                setting.update({
                    'CLOSESPIDER_PAGECOUNT': self.totalPageCount - i + 1
                })
                spiderPageCount = setting.get('CLOSESPIDER_PAGECOUNT')
                process = CrawlerProcess(setting)

            process.crawl(CrawlSpider, i)

        process.start()