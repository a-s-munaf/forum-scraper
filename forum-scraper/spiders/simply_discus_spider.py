import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class SimplyDiscusSpider(CrawlSpider):
    name = "simplydiscus"
    allowed_domains = ['forum.simplydiscus.com']
    start_urls=[
        'http://forum.simplydiscus.com/forum.php'
    ]

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('forumdisplay\.php', 'forum\.php' ))),
        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('showthread\.php')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        filename = response.url
        print filename
