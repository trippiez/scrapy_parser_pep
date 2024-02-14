import scrapy
import re
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['http://peps.python.org/']

    def parse(self, response):
        dl_tag = response.xpath('//dl[contains(@class, "field-list")]')
        for status in dl_tag:
            text_status_tag = status.xpath('./dt[starts-with(., "Status")]')
            pep_status = text_status_tag.xpath(
                './following-sibling::dd//abbr/text()'
            ).get()
            pattern = r'^PEP (?P<number>\d+)\s–\s(?P<name>.*)$'
            title = response.xpath('//h1[@class="page-title"]/text()').get()
            re_match = re.search(pattern, title)
            if re_match is not None:
                number, name = re_match.groups()
            else:
                number, name = '', title
            data = {
                'number': number,
                'name': name,
                'status': pep_status
            }
            yield PepParseItem(data)

        pep_links = response.xpath(
            '//section[@id="numerical-index"]//tr/descendant::a/@href'
        ).getall()

        for pep_link in pep_links[:100]:
            if pep_link is not None:
                yield response.follow(pep_link, callback=self.parse)
