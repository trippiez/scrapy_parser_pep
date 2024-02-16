import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import PEP_SPIDER_URL
from pep_parse.xpath_queries import (DL_TAG_XPATH, PEP_LINKS_XPATH,
                                     PEP_STATUS_XPATH, PEP_TITLE_XPATH,
                                     TEXT_XPATH)


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = (PEP_SPIDER_URL, )
    start_urls = [f'https://{PEP_SPIDER_URL}/']

    def parse(self, response):
        pep_links = response.xpath(PEP_LINKS_XPATH).getall()
        for pep_link in pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        dl_tag = response.xpath(DL_TAG_XPATH)
        for status in dl_tag:
            pep_status = status.xpath(PEP_STATUS_XPATH).get()

        title = response.xpath(PEP_TITLE_XPATH + TEXT_XPATH).get().split()

        number = title[1]
        name = ' '.join(title[3:])

        data = {
            'number': number,
            'name': name,
            'status': pep_status
        }
        yield PepParseItem(data)
