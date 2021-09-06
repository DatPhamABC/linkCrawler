import scrapy
import re


class CrawlSpider(scrapy.Spider):
    name = 'linkcrawl'
    custom_settings = {'FEED_EXPORT_ENCODING': 'utf-8',
                       'CLOSESPIDER_PAGECOUNT': 30}

    def __init__(self, category, *args, **kwargs):
        super(CrawlSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f'https://vnexpress.net/thoi-su-p{category}']

    def parse(self, response):
        const_str = ['covid', 'F0', 'F1', 'dịch', 'giãn']
        const_str = [x.lower().encode() for x in const_str]

        for article in response.css('#automation_TV0 div.width_common.list-news-subfolder'):
            title = article.css('h3.title-news a::text').get()
            title = title.replace('\n', '')
            if not self.check(title, const_str):
                continue
            else:
                desc = article.css('p.description a::text').get()
                if not self.check(desc, const_str):
                    continue
                else:
                    link = article.css('a').attrib['href']
                    yield {
                        'link': link
                    }

        if response.css('#automation_TV1 div.width_common.list-news-subfolder'):
            auto1 = response.css('#automation_TV1 div.width_common.list-news-subfolder')
            for article in auto1:
                title = article.css('h3.title-news a::text').get()
                title = title.replace('\n', '')
                if not self.check(title, const_str):
                    continue
                else:
                    desc = article.css('p.description a::text').get()
                    if not self.check(desc, const_str):
                        continue
                    else:
                        link = article.css('a').attrib['href']
                        yield {
                            'link': link
                        }

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
