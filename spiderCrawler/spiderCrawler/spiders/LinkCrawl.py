import scrapy
import re
import pymongo
import traceback
import logging


class CrawlSpider(scrapy.Spider):
    name = 'linkcrawl'

    custom_settings = {'FEED_EXPORT_ENCODING': 'utf-8'}

    def __init__(self, category, *args, **kwargs):
        super(CrawlSpider, self).__init__(*args, **kwargs)
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['scrapedLink']
        self.collection = db['link']
        self.start_urls = [f'https://vnexpress.net/thoi-su-p{category}']

    def parse(self, response):
        const_str = ['covid', 'F0', 'F1', 'dịch bệnh', 'giãn cách', 'xét nghiệm',
                     'tiêm', 'chống dịch', 'ổ dịch']
        const_str = [x.lower().encode() for x in const_str]

        if response.css('#automation_TV0 div.width_common.list-news-subfolder'):
            for article in response.css('#automation_TV0 div.width_common.list-news-subfolder article'):
                try:
                    title = article.css('h3 a::text').get()
                    title = title.replace('\n', '')
                    if not self.check(title, const_str):
                        continue
                    else:
                        desc = article.css('p.description a::text').get()
                        if not self.check(desc, const_str):
                            continue
                        else:
                            link = {
                                'link': article.css('a').attrib['href']
                            }
                            self.collection.insert(dict(link))
                except Exception as e:
                    logging.error(traceback.format_exc())
                    pass

        if response.css('#automation_TV1 div.width_common.list-news-subfolder'):
            for article in response.css('#automation_TV1 div.width_common.list-news-subfolder article'):
                try:
                    title = article.css('h3 a::text').get()
                    title = title.replace('\n', '')
                    if not self.check(title, const_str):
                        continue
                    else:
                        desc = article.css('p.description a::text').get()
                        if not self.check(desc, const_str):
                            continue
                        else:
                            link = {
                                'link': article.css('a').attrib['href']
                            }
                            self.collection.insert(dict(link))
                except Exception as e:
                    logging.error(traceback.format_exc())
                    pass

        next_page = response.css('a.btn-page.next-page ::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    @staticmethod
    # true if title contain string from const_str
    def check(title, const_str):
        for i in const_str:
            if re.search(i, title.lower().encode()):
                return True
            else:
                continue
        return False
