from scrapy.spiders import Spider
from scrapy.selector import Selector

from dirbot.items import Website


class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoztools.net"]
    start_urls = [
        "http://dmoztools.net/Computers/Programming/Languages/Python/Books/",
        "http://dmoztools.net/Computers/Programming/Languages/Python/Resources/",
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html
        Use the `check` command to run the contract checks.

        @url http://dmoztools.net/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        nodes = response.xpath('//div[contains(@class, "site-item")]/div[contains(@class, "title-and-desc")]')
        items = []

        for node in nodes:
            item = Website()
            item['name'] = node.xpath('a/div[contains(@class, "site-title")]/text()').re_first('^[\s\r\n]*(.*[^\s])[\s\r\n]*')
            item['url'] = node.xpath('a/@href').extract_first()
            item['description'] = node.xpath('div[contains(@class, "site-descr")]/text()').re_first('^[\s\r\n]*(.*)[\s\r\n]*')
            items.append(item)

        return items
