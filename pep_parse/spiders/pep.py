import scrapy
from scrapy.http import HtmlResponse

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response: HtmlResponse):

        all_links = response.css('a[href^="/pep-"]::attr(href)').getall()
        for link in all_links:
            yield response.follow(
                response.urljoin(link),
                callback=self.parse_pep, )

    def parse_pep(self, response: HtmlResponse):
        title = response.css('.page-title::text').get()
        status = response.css('dt:contains("Status") + dd > abbr::text').get()
        if title:
            number, name = title.split(' – ', maxsplit=1)
            number = number.split()[1]
            pep_item = {
                'number': number,
                'name': name,
                'status': status, }
            yield PepParseItem(pep_item)
