import scrapy
import re
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_links = response.xpath(
            '//section[@id="numerical-index"]'
            '//tr/following::a[1]/@href[starts-with(., "pep")]'
        ).getall()
        if pep_links:
            for pep_link in pep_links:
                if pep_link is not None:
                    yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        dl_tag = response.xpath('//dl[contains(@class, "rfc2822")]')
        for status in dl_tag:
            pep_status = status.xpath(
                './dt[starts-with(., "Status")]'
                '/following-sibling::dd//abbr/text()').get()

            title = response.xpath('//h1[@class="page-title"]').extract_first()
            title_text = scrapy.Selector(
                text=title).xpath('//text()').extract()
            title = ''.join(title_text)

            pattern = r'^PEP (?P<number>\d+)\s–\s(?P<name>.*)$'
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
