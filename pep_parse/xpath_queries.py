PEP_LINKS_XPATH = ('//section[@id="numerical-index"]'
                   '//tr/following::a[1]/@href[starts-with(., "pep")]')

PEP_STATUS_XPATH = ('./dt[starts-with(., "Status")]'
                    '/following-sibling::dd//abbr/text()')

PEP_TITLE_XPATH = '//h1[@class="page-title"]'

TEXT_XPATH = '//text()'

DL_TAG_XPATH = '//dl[contains(@class, "rfc2822")]'
